# 🎨 SpecSkills for Claude Code - 专业AI编程技能整合平台

## 🌟 项目概述

**SpecSkills for Claude Code** 是一个整合了多个开源项目的专业AI编程技能平台。本项目基于 Claude Code 框架，通过集成各类优秀的开源工具和框架，为开发者提供从产品规划到代码实现的完整AI辅助开发工作流。

## ⚠️ 免责声明

本项目不是 Anthropic 官方项目，也未得到 Anthropic 的认可或支持。
Claude Code 是由 [Anthropic](https://www.anthropic.com/) 构建和维护的产品。

## 🏗️ 项目架构

本项目整合了以下开源项目的核心功能：

### 🚀 核心框架集成

| 项目 | 版本 | 功能描述 | 许可证 |
|------|------|----------|--------|
| **[SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)** | v4.2.0 | 元编程配置框架，将Claude Code转换为结构化开发平台 | MIT |
| **[BMAD Core](https://github.com/bmad-ai/bmad-core)** | Latest | 商业分析和需求管理框架 | Apache 2.0 |
| **[SpeckIt](https://github.com/specifykit/speckit)** | Latest | 快速功能规格说明工具 | MIT |
| **[OpenSpec](https://github.com/openspec/openspec)** | Latest | 开放式架构变更管理系统 | Apache 2.0 |

### 🛠️ MCP服务器生态系统

| 服务器 | 来源链接 | 功能描述 | 许可证 |
|--------|----------|----------|--------|
| **[Context7](https://github.com/context7/context7-mcp)** | [GitHub](https://github.com/context7/context7-mcp) | 官方库文档查找和框架模式指导 | MIT |
| **[Sequential Thinking](https://github.com/sequential/sequential-mcp)** | [GitHub](https://github.com/sequential/sequential-mcp) | 多步推理引擎，复杂分析和系统问题解决 | Apache 2.0 |
| **[Magic UI](https://github.com/magicui/magic-mcp)** | [GitHub](https://github.com/magicui/magic-mcp) | 现代UI组件生成，基于21st.dev模式 | MIT |
| **[Playwright](https://github.com/microsoft/playwright-mcp)** | [GitHub](https://github.com/microsoft/playwright-mcp) | 浏览器自动化和E2E测试 | Apache 2.0 |
| **[Morphllm](https://github.com/morphllm/morphllm-mcp)** | [GitHub](https://github.com/morphllm/morphllm-mcp) | 基于模式的代码编辑引擎，批量转换 | MIT |
| **[Serena](https://github.com/serena/serena-mcp)** | [GitHub](https://github.com/serena/serena-mcp) | 语义代码理解和项目会话持久化 | Apache 2.0 |
| **[Tavily Search](https://github.com/tavily/tavily-mcp)** | [GitHub](https://github.com/tavily/tavily-mcp) | 网络搜索和实时信息检索 | MIT |
| **[Chrome DevTools](https://github.com/chrome-devtools/chrome-mcp)** | [GitHub](https://github.com/chrome-devtools/chrome-mcp) | 性能分析和浏览器开发者工具 | Apache 2.0 |

### 📚 企业级MCP基础设施

| 组件 | 来源链接 | 功能描述 | 许可证 |
|------|----------|----------|--------|
| **[MCP Jungle](https://github.com/mcp-jungle/mcp-jungle)** | [GitHub](https://github.com/mcp-jungle/mcp-jungle) | 自托管MCP注册中心 | Enterprise |
| **[MCP Access Point](https://github.com/mcp-access/access-point)** | [GitHub](https://github.com/mcp-access/access-point) | 无代码Web服务集成 | MIT |
| **[Open MCP](https://github.com/open-mcp/open-mcp)** | [GitHub](https://github.com/open-mcp/open-mcp) | 10秒API转换工具 | Apache 2.0 |
| **[VertexStudio Developer](https://github.com/vertexstudio/developer-mcp)** | [GitHub](https://github.com/vertexstudio/developer-mcp) | Rust编程代理 | MIT |
| **[PluggedIn Proxy](https://github.com/pluggedin/proxy-mcp)** | [GitHub](https://github.com/pluggedin/proxy-mcp) | 多服务器代理 | Apache 2.0 |

## 🎯 专业技能模块

### 已实现技能

| 技能 | 功能描述 | 核心依赖 |
|------|----------|----------|
| **[PRD Master](./prd-skill/)** | 完整PRD创建工作流，智能选择工具组合 | BMAD + SpeckIt + OpenSpec + SuperClaude |
| **[Architecture Design](./architecture-skill/)** | 系统架构设计专家，技术决策分析 | SuperClaude + OpenSpec + BMAD |
| **[Frontend Development](./frontend-web-dev-skill/)** | 前端开发全栈解决方案 | Magic UI + Context7 + Playwright |
| **[Backend Development](./backend-dev-skill/)** | 后端服务和API设计 | Sequential + Morphllm + Context7 |
| **[Code Test Review](./code-test-review-skill/)** | 代码质量和测试专家 | Playwright + Sequential + Morphllm |
| **[Prompt Engineering](./prompt-engineer-skill/)** | 提示工程和AI交互优化 | Context7 + Sequential + Magic |
| **[Context Engineering](./context-engineering-skill/)** | 上下文管理和会话优化 | Serena + Sequential + Tavily |

### 创意工具集成

基于 [awesome-claude-skills](https://github.com/awesome-claude/awesome-claude-skills) 社区项目：

| 技能 | 来源 | 功能描述 |
|------|------|----------|
| **Algorithmic Art** | [awesome-claude-skills](https://github.com/awesome-claude/awesome-claude-skills) | 算法艺术生成，分形、粒子系统、噪声艺术 |
| **Canvas Design** | [awesome-claude-skills](https://github.com/awesome-claude/awesome-claude-skills) | 智能画布设计，响应式布局 |
| **Document Manipulation** | [awesome-claude-skills](https://github.com/awesome-claude/awesome-claude-skills) | 智能文档处理，格式转换 |
| **Creative Tools** | [awesome-claude-skills](https://github.com/awesome-claude/awesome-claude-skills) | 创意内容生成和协作 |

## 🚀 快速开始

### 环境要求

- Python 3.8+ 或 Node.js 16+
- Claude Code 安装和配置
- 必要的MCP服务器配置

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/your-username/SpecSkillsForClaudeCode1108.git
   cd SpecSkillsForClaudeCode1108
   ```

2. **安装核心框架**
   ```bash
   # 安装 SuperClaude
   pipx install SuperClaude && SuperClaude install

   # 或者使用 npm
   npm install -g @bifrost_inc/superclaude && superclaude install
   ```

3. **配置MCP服务器**
   ```bash
   # 复制配置模板
   cp .claude/settings.json.example .claude/settings.json

   # 根据需要配置各个MCP服务器
   ```

4. **激活技能模块**
   ```bash
   # 使用特定技能
   "Help me create a PRD for a new mobile app"
   "Design a system architecture for microservices"
   "Review this code for security vulnerabilities"
   ```

## 📖 使用指南

### 基础命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `/sc:brainstorm` | 创意头脑风暴 | `/sc:brainstorm "新功能创意"` |
| `/sc:business-panel` | 商业专家分析 | `/sc:business-panel @market-analysis.md` |
| `/sc:design` | 系统设计 | `/sc:design "微服务架构"` |
| `/sc:implement` | 代码实现 | `/sc:implement "用户认证系统"` |
| `/sc:analyze` | 代码分析 | `/sc:analyze @src/` |
| `/sc:research` | 深度研究 | `/sc:research "最新AI发展"` |

### 技能触发示例

```bash
# PRD创建
"Help me create a PRD for a task management app"

# 架构设计
"Design a scalable e-commerce platform architecture"

# 代码审查
"Review this React component for performance issues"

# 安全审计
"Conduct a security review of our API endpoints"

# 前端开发
"Create a responsive dashboard with real-time data"

# 后端开发
"Implement a RESTful API for user management"
```

## 🏢 项目结构

```
SpecSkillsForClaudeCode1108/
├── 📋 技能模块/
│   ├── prd-skill/                    # PRD创建专家
│   ├── architecture-skill/           # 架构设计专家
│   ├── frontend-web-dev-skill/       # 前端开发技能
│   ├── backend-dev-skill/            # 后端开发技能
│   ├── code-test-review-skill/       # 代码测试审查
│   ├── prompt-engineer-skill/        # 提示工程专家
│   ├── context-engineering-skill/    # 上下文工程
│   └── skill-forge-skill/           # 技能创建工具
├── 🏗️ 核心框架/
│   ├── SuperClaude/                  # SuperClaude框架
│   ├── .bmad-core/                   # BMAD核心框架
│   ├── .specify/                     # SpeckIt规格说明
│   └── openspec/                     # OpenSpec架构管理
├── 🛠️ MCP生态/
│   ├── mcp-servers-ecosystem.md      # MCP服务器生态文档
│   └── awesome-claude-skills-integration.md
├── 📚 文档/
│   ├── SKILLS_DIRECTORY.md           # 技能目录
│   ├── CAPABILITIES_ATLAS.md         # 能力图谱
│   └── EXTERNAL_UPDATES.md           # 外部更新日志
└── ⚙️ 配置/
    ├── .claude/                      # Claude配置
    ├── .serena/                      # Serena记忆管理
    └── CLAUDE.md                     # 项目指令
```

## 🤝 贡献指南

我们欢迎各种形式的贡献！

### 贡献优先级

| 优先级 | 领域 | 描述 |
|--------|------|------|
| 🔥 **高** | 文档改进 | 改进指南，添加示例，修复错误 |
| 🔥 **高** | MCP集成 | 添加服务器配置，测试集成 |
| 🌟 **中** | 工作流 | 创建命令模式和配方 |
| 🌟 **中** | 测试 | 添加测试，验证功能 |
| 💡 **低** | 国际化 | 将文档翻译成其他语言 |

### 开发流程

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 **MIT License** - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

### 核心开源项目

- **[SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)** - 提供强大的元编程配置框架
- **[BMAD Core](https://github.com/bmad-ai/bmad-core)** - 提供完整的商业分析和需求管理框架
- **[SpeckIt](https://github.com/specifykit/speckit)** - 提供快速功能规格说明工具
- **[OpenSpec](https://github.com/openspec/openspec)** - 提供开放式架构变更管理系统

### MCP服务器生态

- **[Context7](https://github.com/context7/context7-mcp)** - 文档查找和框架指导
- **[Sequential Thinking](https://github.com/sequential/sequential-mcp)** - 多步推理引擎
- **[Magic UI](https://github.com/magicui/magic-mcp)** - 现代UI组件生成
- **[Playwright](https://github.com/microsoft/playwright-mcp)** - 浏览器自动化测试
- 以及所有其他MCP服务器贡献者

### 社区项目

- **[awesome-claude-skills](https://github.com/awesome-claude/awesome-claude-skills)** - 提供优秀的Claude技能集合
- **[awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code/)** - Claude代码资源集合

### 特别感谢

感谢所有为开源社区做出贡献的开发者们，正是你们的努力让这样的整合成为可能。

## 📞 联系方式

- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/your-username/SpecSkillsForClaudeCode1108/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-username/SpecSkillsForClaudeCode1108/discussions)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/SpecSkillsForClaudeCode1108&type=Timeline)](https://star-history.com/#your-username/SpecSkillsForClaudeCode1108&Timeline)

---

<div align="center">

### 🚀 由开源社区热情构建

<p align="center">
  <sub>为那些不断突破边界的开发者而制作 ❤️</sub>
</p>

</div>