# SpecSkills本地备份管理器

用于管理从Claude插件市场(`myspecskills`)同步到本地的技能备份工具集。

## 🎯 功能概述

### ✨ 主要功能
- **🔄 双向同步**: 源目录 ↔ 本地备份
- **📊 智能比较**: 检测文件差异和变更
- **🗂️ 技能管理**: 详细的技能信息管理
- **⏰ 历史记录**: 保留备份历史和统计
- **🛡️ 安全操作**: 完善的错误处理和恢复机制

## 📁 目录结构

```
/Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108/
├── local-skills-backup/              # 本地备份目录
│   ├── architecture-skill/           # 系统架构师技能
│   ├── backend-dev-skill/            # 后端开发技能
│   ├── code-test-review-skill/       # 代码测试审查技能
│   ├── context-engineering-skill/     # 上下文工程师技能
│   ├── frontend-web-dev-skill/       # 前端Web开发技能
│   ├── prd-skill/                    # PRD大师技能
│   ├── prompt-engineer-skill/        # 提示工程师技能
│   └── skill-forge-skill/            # 技能锻造师技能
├── manage_local_backup.py            # 备份管理脚本
├── backup_config.json               # 备份配置文件
└── LOCAL_BACKUP_README.md           # 本文档
```

## 🚀 使用方法

### 基本命令

```bash
# 进入项目目录
cd /Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108

# 创建本地备份
python3 manage_local_backup.py backup

# 查看备份状态
python3 manage_local_backup.py status

# 列出所有技能
python3 manage_local_backup.py list

# 详细列出技能信息
python3 manage_local_backup.py list-detailed
```

### 恢复操作

```bash
# 恢复所有备份到插件市场
python3 manage_local_backup.py restore

# 恢复指定技能
python3 manage_local_backup.py restore prd-skill
```

### 高级功能

```bash
# 比较源目录和备份目录
python3 manage_local_backup.py compare

# 清理本地备份
python3 manage_local_backup.py clean
```

## 📊 状态输出示例

### 基本状态
```
📊 本地备份状态
==================================================
源目录技能数量: 8
备份目录技能数量: 8
最近备份时间: 2025-11-15 10:47:00
相同的技能: 8
```

### 技能列表
```
📋 备份中的技能 (8个):
--------------------------------------------------
  • architecture-skill
  • backend-dev-skill
  • code-test-review-skill
  • context-engineering-skill
  • frontend-web-dev-skill
  • prd-skill
  • prompt-engineer-skill
  • skill-forge-skill
```

### 详细技能信息
```
📋 备份中的技能 (8个):
--------------------------------------------------

🎯 architecture-skill
   大小: 103,482 字节
   文件数: 6
   修改时间: 2025-11-15 10:47:00
   包含: ✅ SKILL.md 📖 README 📝 Examples 📄 License

🎯 prd-skill
   大小: 37,621 字节
   文件数: 4
   修改时间: 2025-11-15 10:47:00
   包含: ✅ SKILL.md 📖 README 📝 Examples 📄 License
```

## 🔍 智能比较功能

### 比较结果
```
📊 目录比较结果:
  仅在源目录: []
  仅在备份中: []
  有差异: []
  相同: ['architecture-skill', 'backend-dev-skill', ...]
```

### 比较逻辑
- **文件数量差异**: 检测文件增删
- **大小差异**: 检测文件内容变更（阈值1KB）
- **时间戳**: 记录最后修改时间
- **重要文件**: 检查SKILL.md、README.md等关键文件

## 📝 配置文件

### backup_config.json 结构
```json
{
  "last_backup": "2025-11-15T10:47:00.123456",
  "backup_history": [
    {
      "timestamp": "2025-11-15T10:47:00.123456",
      "total_skills": 8,
      "success_count": 8,
      "failed_count": 0
    }
  ],
  "skill_info": {
    "prd-skill": {
      "name": "prd-skill",
      "path": "/path/to/prd-skill",
      "size": 37621,
      "files": ["SKILL.md", "README.md", "examples.md", "LICENSE.txt"],
      "last_modified": "2025-11-15T10:47:00.123456",
      "has_skill_md": true,
      "has_readme": true,
      "has_examples": true,
      "has_license": true
    }
  }
}
```

## 🛠️ 高级用法

### 1. 自动化备份脚本

```bash
#!/bin/bash
# auto_backup.sh

cd /Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108

# 创建备份
python3 manage_local_backup.py backup

# 检查结果
if [ $? -eq 0 ]; then
    echo "✅ 备份成功"
else
    echo "❌ 备份失败"
    exit 1
fi

# 提交到Git（如果有变更）
if git diff --quiet local-skills-backup/; then
    echo "📝 无变更，无需提交"
else
    git add local-skills-backup/
    git commit -m "🔄 Auto backup skills - $(date)"
    echo "📝 已提交到Git"
fi
```

### 2. 定时备份

```bash
# 添加到crontab（每天凌晨2点备份）
0 2 * * * cd /Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108 && python3 manage_local_backup.py backup >> backup.log 2>&1
```

### 3. 技能完整性检查

```bash
#!/bin/bash
# check_integrity.sh

echo "🔍 检查技能完整性..."

python3 manage_local_backup.py list-detailed | grep -E "(包含:|大小:)"

# 检查每个技能是否有SKILL.md
for skill in local-skills-backup/*/; do
    if [ ! -f "$skill/SKILL.md" ]; then
        echo "⚠️  缺少SKILL.md: $skill"
    fi
done
```

## 🔧 故障排除

### 常见问题

1. **权限错误**
   ```bash
   chmod +x manage_local_backup.py
   ```

2. **目录不存在**
   ```bash
   mkdir -p local-skills-backup
   ```

3. **配置文件损坏**
   ```bash
   rm backup_config.json
   python3 manage_local_backup.py status  # 重新生成
   ```

### 调试模式

```python
# 在manage_local_backup.py中添加调试输出
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 使用场景

### 1. 开发环境备份
- 在开发新技能前创建备份
- 定期同步最新的技能状态
- 保护重要的技能配置

### 2. 团队协作
- 共享标准化的技能集
- 统一团队的技能版本
- 快速恢复工作环境

### 3. 版本管理
- 跟踪技能变更历史
- 回滚到之前的版本
- 比较不同版本的差异

### 4. 灾难恢复
- 插件市场损坏时快速恢复
- 迁移到新的环境
- 离线使用技能

## 🎯 最佳实践

### 备份策略
1. **定期备份**: 建议每天或每周备份一次
2. **重要节点**: 在重大变更前手动备份
3. **版本标记**: 使用Git标记重要版本
4. **异地备份**: 考虑将备份推送到远程仓库

### 管理建议
1. **定期清理**: 删除过期的备份文件
2. **文档更新**: 及时更新README和配置
3. **监控告警**: 设置备份失败的告警
4. **测试恢复**: 定期测试恢复功能

### 团队协作
1. **统一标准**: 团队使用相同的备份策略
2. **共享配置**: 将配置文件纳入版本控制
3. **文档同步**: 保持文档与实际状态一致
4. **培训使用**: 确保团队成员了解使用方法

---

**提示**: 建议将`local-skills-backup`目录纳入Git版本控制，这样既能保护您的技能备份，又能与团队共享最新版本。