# 📁 SpecSkills项目根目录整理计划

**整理目标**: 创建清晰、专业、易于维护的项目结构
**整理时间**: 2025-11-15 13:40:00

## 🔍 当前根目录问题分析

### 文件混乱现状
- **根目录文件过多**: 35个文档/配置/脚本文件散落在根目录
- **缺乏逻辑分组**: 报告、脚本、配置、文档混杂在一起
- **命名不一致**: 时间戳文件、临时文件、正式文档混合
- **维护困难**: 难以快速定位特定类型的文件

### 文件分类统计
- **项目技能目录**: 8个 (-skill 目录)
- **配置文件**: .gitignore, .mcp.json, CLAUDE.md
- **管理脚本**: 5个 .py/.sh 文件
- **文档报告**: 20+个 .md 文件
- **临时目录**: 5个 aitmpl-* 目录
- **系统目录**: .git, .claude, .serena, .specify

## 🎯 目标目录结构设计

```
SpecSkillsForClaudeCode1108/
├── 📁 docs/                     # 所有文档和报告
│   ├── 📁 reports/              # 安装和分析报告
│   │   ├── FINAL_INSTALLATION_REPORT.md
│   │   ├── PROJECT_CONTENTS_STATISTICS.md
│   │   ├── UPDATED_PROJECT_CONTENTS_STATISTICS.md
│   │   └── *SYNC_REPORT*.md
│   ├── 📁 guides/               # 安装和使用指南
│   │   ├── README.md (主README)
│   │   ├── COMPLETE_SKILLS_INSTALLATION_GUIDE.md
│   │   └── AITMPL_INSTALLATION_SUMMARY.md
│   ├── 📁 references/           # 参考资料和能力图谱
│   │   ├── CAPABILITIES_ATLAS.md
│   │   ├── awesome-claude-skills-integration.md
│   │   ├── AGENTS.md
│   │   └── SKILLS_GAP_ANALYSIS.md
│   └── 📁 project/              # 项目管理和变更日志
│       ├── EXTERNAL_UPDATES.md
│       └── PROJECT_INITIALIZATION_REPORT.md
├── 📁 scripts/                  # 所有管理脚本
│   ├── 📁 management/           # 备份和同步管理
│   │   ├── manage_local_backup.py
│   │   ├── sync_skills.py
│   │   └── sync_anthropic_skills.py
│   ├── 📁 installation/         # 安装相关脚本
│   │   ├── install_all_missing_skills.sh
│   │   ├── install_aitmpl_batch.sh
│   │   └── download_aitmpl_agents.py
│   └── 📁 monitoring/           # 监控和维护
│       ├── cron_status.sh
│       └── claude_code_env.sh
├── 📁 config/                   # 配置文件
│   ├── .mcp.json
│   ├── CLAUDE.md
│   └── .gitignore
├── 📁 logs/                     # 日志文件
│   ├── aitmpl_download.log
│   └── (其他日志文件)
├── 📁 temp/                     # 临时文件和下载
│   ├── aitmpl-downloads/
│   ├── aitmpl-install-logs/
│   └── (其他临时文件)
├── 🎯 Core Skills/              # 核心技能目录 (保持现有)
├── 🏢 anthropics-skills/        # Anthropic官方技能 (已存在)
├── 📦 local-skills-backup/      # 本地备份技能 (已存在)
├── 🤖 .claude/                  # Claude组件 (已存在)
├── 🔧 .serena/.specify/.bmad-core/ # AI工具 (已存在)
└── 📁 .git/                     # Git目录 (已存在)
```

## 📋 整理执行步骤

### 第一阶段: 创建新目录结构
1. 创建主要目录: docs/, scripts/, config/, logs/, temp/
2. 创建子目录: docs/reports/, docs/guides/, docs/references/
3. 创建脚本子目录: scripts/management/, scripts/installation/, scripts/monitoring/

### 第二阶段: 移动文件
1. **移动文档报告** → docs/reports/
2. **移动使用指南** → docs/guides/
3. **移动参考资料** → docs/references/
4. **移动管理脚本** → scripts/management/
5. **移动安装脚本** → scripts/installation/
6. **移动监控脚本** → scripts/monitoring/
7. **移动配置文件** → config/
8. **移动日志文件** → logs/
9. **移动临时文件** → temp/

### 第三阶段: 清理和更新
1. 删除临时和重复文件
2. 更新README.md中的路径引用
3. 更新脚本中的相对路径
4. 创建新的根级README.md

## 🔧 文件移动清单

### 📚 文档文件移动 (20个文件)
```
FINAL_INSTALLATION_REPORT.md → docs/reports/
PROJECT_CONTENTS_STATISTICS.md → docs/reports/
UPDATED_PROJECT_CONTENTS_STATISTICS.md → docs/reports/
ANTHROPIC_SKILLS_SYNC_REPORT_*.md → docs/reports/
INSTALLATION_REPORT_*.md → docs/reports/
PROJECT_INITIALIZATION_REPORT.md → docs/reports/

README.md → docs/guides/ (新的主README)
COMPLETE_SKILLS_INSTALLATION_GUIDE.md → docs/guides/
AITMPL_INSTALLATION_SUMMARY.md → docs/guides/

CAPABILITIES_ATLAS.md → docs/references/
awesome-claude-skills-integration.md → docs/references/
AGENTS.md → docs/references/
SKILLS_GAP_ANALYSIS.md → docs/references/

EXTERNAL_UPDATES.md → docs/project/
```

### 🔧 脚本文件移动 (5个文件)
```
manage_local_backup.py → scripts/management/
sync_skills.py → scripts/management/
sync_anthropic_skills.py → scripts/management/

install_all_missing_skills.sh → scripts/installation/
install_aitmpl_batch.sh → scripts/installation/
download_aitmpl_agents.py → scripts/installation/

cron_status.sh → scripts/monitoring/
claude_code_env.sh → scripts/monitoring/
```

### ⚙️ 配置文件移动 (3个文件)
```
.mcp.json → config/
CLAUDE.md → config/
.gitignore → config/
```

### 📝 日志和临时文件移动
```
aitmpl_download.log → logs/
aitmpl-downloads/ → temp/
aitmpl-install-logs/ → temp/
anthropics-skills-backup/ → temp/
```

## 🎯 整理后的优势

### 1. 清晰的结构
- **文档分类明确**: 报告、指南、参考分别存放
- **脚本功能分组**: 管理、安装、监控各司其职
- **配置集中管理**: 所有配置文件统一位置

### 2. 易于维护
- **快速定位**: 根据文件类型快速找到目标
- **逻辑清晰**: 目录名称直接反映内容用途
- **扩展友好**: 新增文件有明确归属

### 3. 专业性提升
- **符合最佳实践**: 标准的项目目录结构
- **便于协作**: 团队成员容易理解和导航
- **工具友好**: IDE和工具能更好地识别项目结构

## ⚠️ 注意事项

1. **路径引用更新**: 移动文件后需要更新脚本中的路径引用
2. **Git跟踪**: 需要Git add/rm操作来跟踪文件移动
3. **权限保持**: 确保脚本文件的执行权限不变
4. **备份安全**: 移动前建议创建完整备份

## 🚀 执行确认

**准备执行项目根目录整理，预计移动35+个文件到新的逻辑结构中。**