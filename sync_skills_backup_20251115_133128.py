#!/usr/bin/env python3
"""
SpecSkills同步管理器
自动监控和同步SpecSkills项目中的技能到Claude插件市场
"""

import os
import sys
import shutil
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Optional

class SpecSkillsSyncManager:
    """SpecSkills同步管理器"""

    def __init__(self):
        # 路径配置
        self.source_root = Path("/Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108")
        self.target_root = Path("/Users/chauncey2025/.claude/plugins/marketplaces/myspecskills")
        self.config_file = Path(__file__).parent / "sync_config.json"

        # 支持的技能目录模式
        self.skill_patterns = [
            "*-skill",           # xxx-skill 目录
            "skills",            # skills 子目录
        ]

        # 排除的目录
        self.exclude_dirs = {
            ".git", ".DS_Store", "__pycache__", "node_modules",
            ".claude", "SuperClaude", ".bmad-core", ".serena",
            "openspec", "awesome-claude-skills-integration.md"
        }

        # 技能标识文件
        self.skill_identifiers = ["SKILL.md", "README.md", "examples.md"]

        # 加载配置
        self.load_config()

    def load_config(self):
        """加载同步配置"""
        default_config = {
            "last_sync": None,
            "skill_hashes": {},
            "sync_history": []
        }

        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except Exception as e:
                print(f"⚠️  配置文件损坏，使用默认配置: {e}")
                self.config = default_config
        else:
            self.config = default_config
            self.save_config()

    def save_config(self):
        """保存同步配置"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ 保存配置失败: {e}")

    def get_file_hash(self, file_path: Path) -> str:
        """计算文件哈希值"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return ""

    def get_directory_hash(self, dir_path: Path) -> str:
        """计算目录哈希值（基于关键文件）"""
        hash_input = ""

        # 只计算关键文件的哈希
        for identifier in self.skill_identifiers:
            file_path = dir_path / identifier
            if file_path.exists():
                hash_input += self.get_file_hash(file_path)

        # 递归计算子目录的重要文件
        for root, dirs, files in os.walk(dir_path):
            root_path = Path(root)

            # 跳过排除的目录
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]

            for file in files:
                if file.endswith(('.md', '.yaml', '.yml', '.json', '.txt')):
                    file_path = root_path / file
                    try:
                        rel_path = file_path.relative_to(dir_path)
                        hash_input += f"{rel_path}:{self.get_file_hash(file_path)}"
                    except:
                        continue

        return hashlib.md5(hash_input.encode()).hexdigest()

    def discover_skills(self) -> List[Path]:
        """发现所有技能目录"""
        skills = []

        if not self.source_root.exists():
            print(f"❌ 源目录不存在: {self.source_root}")
            return skills

        # 查找所有符合模式的目录
        for item in self.source_root.iterdir():
            if not item.is_dir() or item.name in self.exclude_dirs:
                continue

            # 检查是否为技能目录
            if self.is_skill_directory(item):
                skills.append(item)

        # 递归查找子目录中的技能
        for root, dirs, files in os.walk(self.source_root):
            root_path = Path(root)

            # 跳过排除的目录
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]

            for dir_name in dirs:
                dir_path = root_path / dir_name
                if self.is_skill_directory(dir_path):
                    if dir_path not in skills:  # 避免重复
                        skills.append(dir_path)

        return sorted(skills)

    def is_skill_directory(self, dir_path: Path) -> bool:
        """判断是否为技能目录"""
        # 检查目录名模式
        dir_name = dir_path.name

        # 模式1: xxx-skill
        if dir_name.endswith("-skill"):
            return True

        # 模式2: skills 目录
        if dir_name == "skills":
            return True

        # 模式3: 包含技能标识文件
        for identifier in self.skill_identifiers:
            if (dir_path / identifier).exists():
                return True

        return False

    def needs_sync(self, skill_path: Path) -> bool:
        """检查技能是否需要同步"""
        skill_name = skill_path.name
        current_hash = self.get_directory_hash(skill_path)
        last_hash = self.config["skill_hashes"].get(skill_name, "")

        return current_hash != last_hash

    def sync_skill(self, skill_path: Path) -> bool:
        """同步单个技能"""
        skill_name = skill_path.name
        target_path = self.target_root / skill_name

        try:
            print(f"🔄 同步技能: {skill_name}")

            # 创建目标目录
            target_path.mkdir(parents=True, exist_ok=True)

            # 复制文件，排除不必要的目录
            for item in skill_path.iterdir():
                if item.name in self.exclude_dirs:
                    continue

                if item.is_file():
                    target_file = target_path / item.name
                    shutil.copy2(item, target_file)
                elif item.is_dir():
                    target_dir = target_path / item.name
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.copytree(item, target_dir,
                                  ignore=shutil.ignore_patterns('.DS_Store', '__pycache__'))

            # 更新哈希
            self.config["skill_hashes"][skill_name] = self.get_directory_hash(skill_path)

            print(f"✅ 技能同步成功: {skill_name}")
            return True

        except Exception as e:
            print(f"❌ 技能同步失败 {skill_name}: {e}")
            return False

    def remove_obsolete_skills(self, current_skills: List[Path]):
        """移除目标目录中已不存在的技能"""
        if not self.target_root.exists():
            return

        target_skills = {d.name for d in self.target_root.iterdir() if d.is_dir()}
        current_skill_names = {skill.name for skill in current_skills}

        obsolete_skills = target_skills - current_skill_names

        for skill_name in obsolete_skills:
            try:
                skill_path = self.target_root / skill_name
                shutil.rmtree(skill_path)
                print(f"🗑️  移除过时技能: {skill_name}")

                # 从配置中移除
                if skill_name in self.config["skill_hashes"]:
                    del self.config["skill_hashes"][skill_name]

            except Exception as e:
                print(f"❌ 移除技能失败 {skill_name}: {e}")

    def sync_all(self, force: bool = False) -> Dict[str, int]:
        """同步所有技能"""
        print("🚀 开始SpecSkills同步...")

        # 发现技能
        skills = self.discover_skills()
        print(f"📋 发现 {len(skills)} 个技能")

        # 统计信息
        stats = {
            "total": len(skills),
            "synced": 0,
            "skipped": 0,
            "failed": 0
        }

        # 同步每个技能
        for skill_path in skills:
            skill_name = skill_path.name

            if force or self.needs_sync(skill_path):
                if self.sync_skill(skill_path):
                    stats["synced"] += 1
                else:
                    stats["failed"] += 1
            else:
                print(f"⏭️  跳过未变更技能: {skill_name}")
                stats["skipped"] += 1

        # 移除过时技能
        self.remove_obsolete_skills(skills)

        # 更新配置
        self.config["last_sync"] = datetime.now().isoformat()
        sync_record = {
            "timestamp": self.config["last_sync"],
            "stats": stats
        }
        self.config["sync_history"].append(sync_record)

        # 保留最近10次同步记录
        if len(self.config["sync_history"]) > 10:
            self.config["sync_history"] = self.config["sync_history"][-10:]

        self.save_config()

        # 输出统计
        print(f"\n📊 同步完成统计:")
        print(f"   总计: {stats['total']}")
        print(f"   同步: {stats['synced']}")
        print(f"   跳过: {stats['skipped']}")
        print(f"   失败: {stats['failed']}")

        return stats

    def status(self):
        """显示同步状态"""
        print("📊 SpecSkills同步状态")
        print("=" * 50)

        # 发现技能
        skills = self.discover_skills()
        print(f"源目录技能数量: {len(skills)}")

        # 检查目标目录
        if self.target_root.exists():
            target_skills = [d for d in self.target_root.iterdir() if d.is_dir()]
            print(f"目标目录技能数量: {len(target_skills)}")
        else:
            print("目标目录不存在")

        # 最近同步
        if self.config["last_sync"]:
            last_sync = datetime.fromisoformat(self.config["last_sync"])
            print(f"最近同步时间: {last_sync.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("从未同步")

        # 需要更新的技能
        need_update = [skill for skill in skills if self.needs_sync(skill)]
        print(f"需要更新的技能: {len(need_update)}")

        if need_update:
            print("\n🔄 需要更新的技能:")
            for skill in need_update:
                print(f"  - {skill.name}")

    def clean(self):
        """清理目标目录"""
        if self.target_root.exists():
            try:
                shutil.rmtree(self.target_root)
                print(f"🗑️  已清理目标目录: {self.target_root}")

                # 重置配置
                self.config["skill_hashes"] = {}
                self.config["last_sync"] = None
                self.save_config()

            except Exception as e:
                print(f"❌ 清理失败: {e}")
        else:
            print("目标目录不存在，无需清理")


def main():
    """主函数"""
    manager = SpecSkillsSyncManager()

    if len(sys.argv) < 2:
        print("用法:")
        print("  python sync_skills.py sync     # 同步所有技能")
        print("  python sync_skills.py status   # 显示状态")
        print("  python sync_skills.py clean    # 清理目标目录")
        print("  python sync_skills.py force    # 强制同步所有")
        return

    command = sys.argv[1].lower()

    if command == "sync":
        manager.sync_all()
    elif command == "force":
        manager.sync_all(force=True)
    elif command == "status":
        manager.status()
    elif command == "clean":
        manager.clean()
    else:
        print(f"❌ 未知命令: {command}")


if __name__ == "__main__":
    main()