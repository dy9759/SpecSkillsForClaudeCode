#!/usr/bin/env python3
"""
SpecSkills本地备份管理器
管理从Claude插件市场同步到本地的技能备份
"""

import os
import sys
import shutil
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class LocalBackupManager:
    """本地备份管理器"""

    def __init__(self):
        # 路径配置
        self.source_dir = Path("/Users/chauncey2025/.claude/plugins/marketplaces/myspecskills")
        self.backup_dir = Path("/Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108/local-skills-backup")
        self.config_file = Path(__file__).parent / "backup_config.json"

        # 加载配置
        self.load_config()

    def load_config(self):
        """加载备份配置"""
        default_config = {
            "last_backup": None,
            "backup_history": [],
            "skill_info": {}
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
        """保存备份配置"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ 保存配置失败: {e}")

    def get_skill_info(self, skill_path: Path) -> Dict:
        """获取技能信息"""
        skill_name = skill_path.name

        info = {
            "name": skill_name,
            "path": str(skill_path),
            "size": 0,
            "files": [],
            "last_modified": None,
            "has_skill_md": False,
            "has_readme": False,
            "has_examples": False,
            "has_license": False
        }

        try:
            # 计算目录大小
            for root, dirs, files in os.walk(skill_path):
                for file in files:
                    file_path = Path(root) / file
                    if file_path.exists():
                        info["size"] += file_path.stat().st_size
                        rel_path = file_path.relative_to(skill_path)
                        info["files"].append(str(rel_path))

                        # 检查重要文件
                        file_name = file.lower()
                        if file_name == "skill.md":
                            info["has_skill_md"] = True
                        elif file_name.startswith("readme"):
                            info["has_readme"] = True
                        elif file_name.startswith("example"):
                            info["has_examples"] = True
                        elif file_name.startswith("license"):
                            info["has_license"] = True

            # 获取最后修改时间
            info["last_modified"] = datetime.fromtimestamp(
                skill_path.stat().st_mtime
            ).isoformat()

        except Exception as e:
            print(f"⚠️  获取技能信息失败 {skill_name}: {e}")

        return info

    def create_backup(self) -> bool:
        """创建本地备份"""
        print("🚀 开始创建本地备份...")

        if not self.source_dir.exists():
            print(f"❌ 源目录不存在: {self.source_dir}")
            return False

        # 确保备份目录存在
        self.backup_dir.mkdir(parents=True, exist_ok=True)

        # 获取源目录中的技能
        source_skills = []
        for item in self.source_dir.iterdir():
            if item.is_dir() and item.name not in ['.DS_Store']:
                source_skills.append(item)

        print(f"📋 发现 {len(source_skills)} 个技能")

        success_count = 0
        failed_count = 0

        for skill_path in source_skills:
            skill_name = skill_path.name
            backup_path = self.backup_dir / skill_name

            try:
                print(f"🔄 备份技能: {skill_name}")

                # 如果备份目录已存在，先删除
                if backup_path.exists():
                    shutil.rmtree(backup_path)

                # 复制技能目录
                shutil.copytree(skill_path, backup_path)

                # 更新技能信息
                self.config["skill_info"][skill_name] = self.get_skill_info(backup_path)

                print(f"✅ 备份成功: {skill_name}")
                success_count += 1

            except Exception as e:
                print(f"❌ 备份失败 {skill_name}: {e}")
                failed_count += 1

        # 更新配置
        self.config["last_backup"] = datetime.now().isoformat()

        backup_record = {
            "timestamp": self.config["last_backup"],
            "total_skills": len(source_skills),
            "success_count": success_count,
            "failed_count": failed_count
        }
        self.config["backup_history"].append(backup_record)

        # 保留最近10次备份记录
        if len(self.config["backup_history"]) > 10:
            self.config["backup_history"] = self.config["backup_history"][-10:]

        self.save_config()

        # 输出统计
        print(f"\n📊 备份完成统计:")
        print(f"   总计: {len(source_skills)}")
        print(f"   成功: {success_count}")
        print(f"   失败: {failed_count}")

        return failed_count == 0

    def restore_backup(self, skill_name: str = None) -> bool:
        """恢复备份到插件市场"""
        print("🔄 开始恢复备份...")

        if not self.backup_dir.exists():
            print(f"❌ 备份目录不存在: {self.backup_dir}")
            return False

        # 确保目标目录存在
        self.source_dir.mkdir(parents=True, exist_ok=True)

        if skill_name:
            # 恢复单个技能
            backup_path = self.backup_dir / skill_name
            target_path = self.source_dir / skill_name

            if not backup_path.exists():
                print(f"❌ 备份技能不存在: {skill_name}")
                return False

            try:
                print(f"🔄 恢复技能: {skill_name}")

                if target_path.exists():
                    shutil.rmtree(target_path)

                shutil.copytree(backup_path, target_path)
                print(f"✅ 恢复成功: {skill_name}")
                return True

            except Exception as e:
                print(f"❌ 恢复失败 {skill_name}: {e}")
                return False
        else:
            # 恢复所有技能
            backup_skills = []
            for item in self.backup_dir.iterdir():
                if item.is_dir() and item.name not in ['.DS_Store']:
                    backup_skills.append(item)

            print(f"📋 发现 {len(backup_skills)} 个备份技能")

            success_count = 0
            failed_count = 0

            for skill_path in backup_skills:
                skill_name = skill_path.name
                target_path = self.source_dir / skill_name

                try:
                    print(f"🔄 恢复技能: {skill_name}")

                    if target_path.exists():
                        shutil.rmtree(target_path)

                    shutil.copytree(skill_path, target_path)
                    print(f"✅ 恢复成功: {skill_name}")
                    success_count += 1

                except Exception as e:
                    print(f"❌ 恢复失败 {skill_name}: {e}")
                    failed_count += 1

            # 输出统计
            print(f"\n📊 恢复完成统计:")
            print(f"   总计: {len(backup_skills)}")
            print(f"   成功: {success_count}")
            print(f"   失败: {failed_count}")

            return failed_count == 0

    def compare_directories(self) -> Dict:
        """比较源目录和备份目录"""
        print("🔍 比较源目录和备份目录...")

        result = {
            "source_only": [],
            "backup_only": [],
            "different": [],
            "identical": []
        }

        # 获取源目录技能
        source_skills = set()
        if self.source_dir.exists():
            for item in self.source_dir.iterdir():
                if item.is_dir() and item.name not in ['.DS_Store']:
                    source_skills.add(item.name)

        # 获取备份目录技能
        backup_skills = set()
        if self.backup_dir.exists():
            for item in self.backup_dir.iterdir():
                if item.is_dir() and item.name not in ['.DS_Store']:
                    backup_skills.add(item.name)

        # 分析差异
        result["source_only"] = list(source_skills - backup_skills)
        result["backup_only"] = list(backup_skills - source_skills)

        # 检查共同技能的差异
        common_skills = source_skills & backup_skills
        for skill_name in common_skills:
            source_path = self.source_dir / skill_name
            backup_path = self.backup_dir / skill_name

            source_info = self.get_skill_info(source_path)
            backup_info = self.config["skill_info"].get(skill_name, {})

            # 简单比较：文件数量和总大小
            if (len(source_info["files"]) != len(backup_info.get("files", [])) or
                abs(source_info["size"] - backup_info.get("size", 0)) > 1024):
                result["different"].append(skill_name)
            else:
                result["identical"].append(skill_name)

        return result

    def status(self):
        """显示备份状态"""
        print("📊 本地备份状态")
        print("=" * 50)

        # 源目录状态
        if self.source_dir.exists():
            source_skills = [d for d in self.source_dir.iterdir()
                           if d.is_dir() and d.name not in ['.DS_Store']]
            print(f"源目录技能数量: {len(source_skills)}")
        else:
            print("源目录不存在")

        # 备份目录状态
        if self.backup_dir.exists():
            backup_skills = [d for d in self.backup_dir.iterdir()
                           if d.is_dir() and d.name not in ['.DS_Store']]
            print(f"备份目录技能数量: {len(backup_skills)}")
        else:
            print("备份目录不存在")

        # 最近备份
        if self.config["last_backup"]:
            last_backup = datetime.fromisoformat(self.config["last_backup"])
            print(f"最近备份时间: {last_backup.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("从未备份")

        # 比较差异
        comparison = self.compare_directories()

        if comparison["source_only"]:
            print(f"仅在源目录中: {', '.join(comparison['source_only'])}")

        if comparison["backup_only"]:
            print(f"仅在备份中: {', '.join(comparison['backup_only'])}")

        if comparison["different"]:
            print(f"有差异的技能: {', '.join(comparison['different'])}")

        if comparison["identical"]:
            print(f"相同的技能: {len(comparison['identical'])}")

    def clean_backup(self):
        """清理备份目录"""
        if self.backup_dir.exists():
            try:
                shutil.rmtree(self.backup_dir)
                print(f"🗑️  已清理备份目录: {self.backup_dir}")

                # 重置配置
                self.config["skill_info"] = {}
                self.config["last_backup"] = None
                self.save_config()

            except Exception as e:
                print(f"❌ 清理失败: {e}")
        else:
            print("备份目录不存在，无需清理")

    def list_skills(self, detailed: bool = False):
        """列出技能信息"""
        if not self.backup_dir.exists():
            print("备份目录不存在")
            return

        skills = [d for d in self.backup_dir.iterdir()
                 if d.is_dir() and d.name not in ['.DS_Store']]

        print(f"📋 备份中的技能 ({len(skills)}个):")
        print("-" * 50)

        for skill_name in sorted([s.name for s in skills]):
            skill_info = self.config["skill_info"].get(skill_name, {})

            if detailed:
                print(f"\n🎯 {skill_name}")
                print(f"   大小: {skill_info.get('size', 0):,} 字节")
                print(f"   文件数: {len(skill_info.get('files', []))}")
                print(f"   修改时间: {skill_info.get('last_modified', 'N/A')}")

                # 检查重要文件
                indicators = []
                if skill_info.get('has_skill_md'): indicators.append("✅ SKILL.md")
                if skill_info.get('has_readme'): indicators.append("📖 README")
                if skill_info.get('has_examples'): indicators.append("📝 Examples")
                if skill_info.get('has_license'): indicators.append("📄 License")

                if indicators:
                    print(f"   包含: {' '.join(indicators)}")
            else:
                print(f"  • {skill_name}")


def main():
    """主函数"""
    manager = LocalBackupManager()

    if len(sys.argv) < 2:
        print("用法:")
        print("  python manage_local_backup.py backup      # 创建备份")
        print("  python manage_local_backup.py restore     # 恢复所有备份")
        print("  python manage_local_backup.py restore xxx # 恢复指定技能")
        print("  python manage_local_backup.py status      # 显示状态")
        print("  python manage_local_backup.py compare     # 比较目录")
        print("  python manage_local_backup.py list        # 列出技能")
        print("  python manage_local_backup.py list-detailed # 详细列出技能")
        print("  python manage_local_backup.py clean       # 清理备份")
        return

    command = sys.argv[1].lower()

    if command == "backup":
        manager.create_backup()
    elif command == "restore":
        skill_name = sys.argv[2] if len(sys.argv) > 2 else None
        manager.restore_backup(skill_name)
    elif command == "status":
        manager.status()
    elif command == "compare":
        comparison = manager.compare_directories()
        print("📊 目录比较结果:")
        print(f"  仅在源目录: {comparison['source_only']}")
        print(f"  仅在备份中: {comparison['backup_only']}")
        print(f"  有差异: {comparison['different']}")
        print(f"  相同: {comparison['identical']}")
    elif command == "list":
        manager.list_skills(False)
    elif command == "list-detailed":
        manager.list_skills(True)
    elif command == "clean":
        manager.clean_backup()
    else:
        print(f"❌ 未知命令: {command}")


if __name__ == "__main__":
    main()