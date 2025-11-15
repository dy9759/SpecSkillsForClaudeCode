# SpecSkills同步管理器

自动监控和同步SpecSkills项目中的技能到Claude插件市场的智能管理工具。

## 🚀 功能特性

### ✨ 智能同步
- **增量更新**: 只同步有变更的技能，节省时间和资源
- **哈希检测**: 基于文件内容哈希的变更检测，精确可靠
- **自动发现**: 智能识别项目中的所有技能目录
- **版本控制**: 记录同步历史，支持回滚操作

### 📁 灵活的技能识别
- **目录模式**: 支持 `xxx-skill` 目录命名
- **标识文件**: 通过 `SKILL.md`、`README.md` 等文件识别技能
- **子目录支持**: 递归查找子目录中的技能
- **排除机制**: 自动排除不必要的文件和目录

### 🛡️ 安全可靠
- **备份保护**: 不会影响源文件
- **错误处理**: 完善的异常处理机制
- **回滚支持**: 可清理和重新同步
- **配置持久化**: 自动保存同步状态

## 📦 安装和使用

### 1. 基本使用

```bash
# 进入项目目录
cd /Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108

# 查看帮助
./sync_skills.sh help

# 查看同步状态
./sync_skills.sh status

# 同步所有技能（仅同步有变更的）
./sync_skills.sh sync

# 强制同步所有技能
./sync_skills.sh force
```

### 2. 高级功能

```bash
# 安装到系统（创建命令行工具）
./sync_skills.sh install

# 设置自动同步（每5分钟检查一次）
./sync_skills.sh auto

# 停止自动同步
./sync_skills.sh no-auto

# 清理目标目录
./sync_skills.sh clean

# 卸载系统安装
./sync_skills.sh uninstall
```

### 3. Python脚本直接使用

```bash
# 基本命令
python3 sync_skills.py sync      # 同步技能
python3 sync_skills.py status    # 查看状态
python3 sync_skills.py force     # 强制同步
python3 sync_skills.py clean     # 清理目录
```

## 🗂️ 目录结构

### 源目录（SpecSkills项目）
```
/Users/chauncey2025/Documents/GitHub/SpecSkillsForClaudeCode1108/
├── prd-skill/                    # PRD大师技能
├── architecture-skill/           # 系统架构师技能
├── frontend-web-dev-skill/       # 前端开发技能
├── backend-dev-skill/            # 后端开发技能
├── code-test-review-skill/       # 代码测试审查技能
├── context-engineering-skill/     # 上下文工程师技能
├── prompt-engineer-skill/        # 提示工程师技能
├── skill-forge-skill/            # 技能锻造师技能
└── ...
```

### 目标目录（Claude插件市场）
```
/Users/chauncey2025/.claude/plugins/marketplaces/myspecskills/
├── prd-skill/                    # 同步的PRD技能
├── architecture-skill/           # 同步的架构技能
├── frontend-web-dev-skill/       # 同步的前端技能
└── ...
```

## ⚙️ 配置文件

同步管理器使用JSON配置文件保存状态：

```json
{
  "last_sync": "2024-01-15T10:30:00",
  "skill_hashes": {
    "prd-skill": "a1b2c3d4...",
    "architecture-skill": "e5f6g7h8..."
  },
  "sync_history": [
    {
      "timestamp": "2024-01-15T10:30:00",
      "stats": {
        "total": 8,
        "synced": 3,
        "skipped": 5,
        "failed": 0
      }
    }
  ]
}
```

## 🔍 技能识别规则

### 1. 目录命名模式
- `xxx-skill`: 以 `-skill` 结尾的目录
- `skills`: 名为 `skills` 的目录

### 2. 标识文件
- `SKILL.md`: 技能定义文件
- `README.md`: 说明文档
- `examples.md`: 使用示例

### 3. 排除的目录
- `.git`, `.DS_Store`, `__pycache__`
- `.claude`, `SuperClaude`, `.bmad-core`
- `openspec`, `node_modules`

## 📊 状态输出示例

```
📊 SpecSkills同步状态
==================================================
源目录技能数量: 9
目标目录技能数量: 7
最近同步时间: 2024-01-15 10:30:00
需要更新的技能: 2

🔄 需要更新的技能:
  - prd-skill
  - architecture-skill
```

## 🚀 同步过程示例

```
🚀 开始SpecSkills同步...
📋 发现 9 个技能
🔄 同步技能: prd-skill
✅ 技能同步成功: prd-skill
🔄 同步技能: architecture-skill
✅ 技能同步成功: architecture-skill
⏭️  跳过未变更技能: frontend-web-dev-skill
...

📊 同步完成统计:
   总计: 9
   同步: 2
   跳过: 7
   失败: 0
```

## 🛠️ 自动化设置

### 设置定时任务
```bash
# 每分钟检查一次（开发时）
*/1 * * * * cd /path/to/project && ./sync_skills.sh sync >/dev/null 2>&1

# 每5分钟检查一次（生产环境）
*/5 * * * * cd /path/to/project && ./sync_skills.sh sync >/dev/null 2>&1

# 每小时检查一次
0 * * * * cd /path/to/project && ./sync_skills.sh sync >/dev/null 2>&1
```

### Git Hook集成
```bash
# 在 .git/hooks/post-commit 中添加
#!/bin/bash
cd "$(git rev-parse --show-toplevel)"
./sync_skills.sh sync
```

## 🔧 故障排除

### 常见问题

1. **权限错误**
   ```bash
   chmod +x sync_skills.sh
   ```

2. **Python不可用**
   ```bash
   # 确保python3在PATH中
   which python3
   export PATH="$PATH:/usr/local/bin"
   ```

3. **目标目录权限**
   ```bash
   # 确保Claude插件目录可写
   mkdir -p ~/.claude/plugins/marketplaces/myspecskills
   chmod 755 ~/.claude/plugins/marketplaces/myspecskills
   ```

### 调试模式

```python
# 在sync_skills.py中添加调试输出
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 重置配置

```bash
# 删除配置文件重新开始
rm sync_config.json
./sync_skills.sh status
```

## 📝 开发说明

### 扩展功能
- 修改 `skill_patterns` 添加新的目录模式
- 修改 `skill_identifiers` 添加新的标识文件
- 修改 `exclude_dirs` 调整排除规则

### 自定义同步逻辑
```python
def custom_sync_logic(self, skill_path: Path):
    # 自定义同步逻辑
    pass
```

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个工具！

## 📄 许可证

本项目采用Apache 2.0许可证。

---

**提示**: 建议定期运行 `./sync_skills.sh status` 来监控同步状态，或在开发过程中设置自动同步以保持技能的最新状态。