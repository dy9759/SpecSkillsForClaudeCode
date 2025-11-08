# 🎨 Claude Skills 目录 - 完整技能清单

## 📋 概述

基于当前根目录项目，我们可以创建多个专业的Claude技能，每个技能整合不同的工具组合来解决特定领域的问题。除了已创建的**PRD技能**，以下是可开发的技能清单。

---

## 🚀 已创建技能

### 1. **prd** - PRD大师 ✅
- **位置**: `/prd-skill/`
- **功能**: 完整PRD创建工作流，智能选择工具组合
- **核心价值**: 从创意到实施需求的端到端管理

---

## 🎯 待创建技能 (推荐优先级)

### 🔥 高优先级技能

#### 2. **architecture** - 系统架构师
```markdown
触发: "帮我设计系统架构" / "设计一个...架构"
核心能力:
- /sc:design + /sc:spec-panel + BMAD Architect
- OpenSpec架构变更管理
- 技术决策分析和风险评估
- 自动生成架构文档和决策记录
```

#### 3. **startup-mvp** - 创业MVP加速器
```markdown
触发: "我想创建一个MVP" / "快速验证商业模式"
核心能力:
- /sc:brainstorm + /sc:business-panel (Christensen, Godin)
- BMAD快速PRD模板
- 最小可行产品规划
- 用户验证和迭代策略
```

#### 4. **code-quality** - 代码质量大师
```markdown
触发: "提升代码质量" / "重构这个系统"
核心能力:
- /sc:analyze + /sc:improve + /sc:cleanup
- 自动化重构建议
- 技术债务管理
- 性能优化方案
```

#### 5. **api-design** - API设计专家
```markdown
触发: "设计REST API" / "API架构设计"
核心能力:
- /sc:design + /sc:explain + BMAD Architect
- API规范生成 (OpenAPI)
- 接口文档和测试用例
- 版本管理和兼容性策略
```

### 🌟 中优先级技能

#### 6. **data-analytics** - 数据分析平台
```markdown
触发: "分析这份数据" / "构建数据分析系统"
核心能力:
- /sc:research + /sc:index + BMAD Analyst
- 数据洞察生成
- 可视化建议
- 机器学习模型选择指导
```

#### 7. **security-review** - 安全审计专家
```markdown
触发: "安全审查" / "漏洞分析" / "安全加固"
核心能力:
- /sc:analyze + /sc:troubleshoot + 安全专家面板
- 漏洞扫描和风险评估
- 安全最佳实践建议
- 合规性检查清单
```

#### 8. **performance-optimization** - 性能优化大师
```markdown
触发: "系统性能优化" / "提升响应速度"
核心能力:
- /sc:analyze + /sc:improve + 性能分析
- 瓶颈识别和优化方案
- 监控策略设计
- 容量规划建议
```

#### 9. **user-research** - 用户研究专家
```markdown
触发: "用户研究" / "用户体验分析"
核心能力:
- /sc:brainstorm + BMAD UX Expert + /sc:explain
- 用户画像和旅程分析
- 可用性测试方案
- A/B测试设计
```

#### 10. **migration-strategy** - 系统迁移专家
```markdown
触发: "系统迁移" / "技术栈升级"
核心能力:
- /sc:spawn + OpenSpec + /sc:design
- 迁移风险评估
- 分阶段迁移计划
- 回滚策略设计
```

### 💡 特色技能

#### 11. **innovation-workshop** - 创新工作坊
```markdown
触发: "创新工作坊" / "产品创新 brainstorm"
核心能力:
- /sc:brainstorm + Business Panel (Christensen, Kim) + Godin
- 创新方法论应用 (蓝海、颠覆式创新)
- 创意筛选和评估
- 创新路线图设计
```

#### 12. **compliance-audit** - 合规审计专家
```markdown
触发: "合规审计" / "法规遵从性检查"
核心能力:
- /sc:analyze + 合规专家面板 + checklists
- GDPR/HIPAA/SOC2合规检查
- 风险评估和缓解方案
- 合规文档生成
```

#### 13. **devops-setup** - DevOps自动化专家
```markdown
触发: "搭建CI/CD" / "DevOps流程设计"
核心能力:
- /sc:build + /sc:workflow + BMAD DevOps
- CI/CD流水线设计
- 基础设施即代码
- 监控和告警策略
```

#### 14. **documentation-system** - 文档系统专家
```markdown
触发: "建立文档体系" / "技术文档生成"
核心能力:
- /sc:index + /sc:document + /sc:explain
- 自动文档生成
- 知识库架构设计
- 文档维护策略
```

#### 15. **ai-integration** - AI集成专家
```markdown
触发: "集成AI功能" / "LLM应用开发"
核心能力:
- /sc:research + /sc:design + Context7 MCP
- AI模型选择和集成
- 提示工程最佳实践
- 成本优化策略
```

### 🔧 工具型技能

#### 16. **git-workflow** - Git工作流专家
```markdown
触发: "优化Git工作流" / "分支策略设计"
核心能力:
- /sc:git + 团队协作最佳实践
- 分支策略设计
- 代码审查流程
- 发布管理策略
```

#### 17. **test-strategy** - 测试策略专家
```markdown
触发: "设计测试策略" / "测试体系搭建"
核心能力:
- /sc:test + BMAD QA + 质量保证流程
- 测试金字塔设计
- 自动化测试框架
- 测试数据管理
```

#### 18. **feature-flag** - 功能开关管理
```markdown
触发: "功能开关系统" / "灰度发布策略"
核心能力:
- 功能开关架构设计
- 灰度发布策略
- 用户分流管理
- 监控和回滚机制
```

---

## 🛠️ 技能创建模板

### 标准技能结构
```
skill-name/
├── SKILL.md           # 技能定义文件
├── README.md          # 使用指南
├── examples.md        # 使用示例
├── LICENSE.txt        # Apache 2.0许可证
└── workflows/         # 工作流程定义 (可选)
    ├── basic.md
    ├── advanced.md
    └── enterprise.md
```

### 技能定义模板
```yaml
---
name: skill-name
description: 清晰描述技能功能和适用场景
license: Apache 2.0
tools: []  # 依赖的MCP工具
---

# 技能名称 - 简短描述

## 概述
技能功能和价值的简洁描述

## 何时使用
明确的触发条件和适用场景

## 核心能力
主要功能和工具组合

## 工作流程
详细的使用步骤和工具协调

## 示例
具体的使用案例和输出示例
```

---

## 🎨 技能组合策略

### **工具协同模式**

#### 分析型技能
```bash
/sc:analyze + /sc:research + Business Panel + BMAD Analyst
```

#### 创造型技能
```bash
/sc:brainstorm + /sc:design + BMAD PM + /sc:explain
```

#### 实施型技能
```bash
/sc:implement + /sc:spawn + /speckit.tasks + BMAD Dev Team
```

#### 质量型技能
```bash
/sc:test + /sc:improve + /sc:cleanup + Quality Checklists
```

### **专家组合模式**

#### 商业决策
```bash
Business Panel (Porter + Christensen + Drucker) + BMAD PM
```

#### 技术架构
```bash
Spec Panel + BMAD Architect + /sc:design
```

#### 用户体验
```bash
BMAD UX Expert + /sc:brainstorm + User Research Methods
```

---

## 📊 技能开发优先级矩阵

| 技能类型 | 开发复杂度 | 商业价值 | 推荐优先级 |
|----------|------------|----------|------------|
| **prd** | 中 | 高 | ✅ 已完成 |
| **architecture** | 高 | 高 | 🔥 立即开发 |
| **startup-mvp** | 中 | 高 | 🔥 立即开发 |
| **code-quality** | 中 | 中 | 🌟 近期开发 |
| **api-design** | 中 | 高 | 🌟 近期开发 |
| **security-review** | 高 | 中 | 💡 中期开发 |
| **performance-optimization** | 高 | 中 | 💡 中期开发 |

---

## 🚀 技能使用场景映射

### **创业公司场景**
```yaml
必备技能:
  - startup-mvp      # 快速产品验证
  - prd              # 产品规划
  - architecture     # 技术架构

可选技能:
  - user-research    # 用户验证
  - api-design       # 接口设计
  - git-workflow     # 团队协作
```

### **企业级产品场景**
```yaml
必备技能:
  - prd              # 完整需求管理
  - architecture     # 系统架构
  - security-review  # 安全合规
  - compliance-audit # 法规遵从

可选技能:
  - migration-strategy # 系统升级
  - performance-optimization # 性能优化
  - devops-setup     # 运维自动化
```

### **技术团队场景**
```yaml
必备技能:
  - code-quality     # 代码质量
  - test-strategy    # 测试策略
  - api-design       # 接口规范
  - git-workflow     # 版本控制

可选技能:
  - documentation-system # 技术文档
  - feature-flag     # 功能开关
  - ai-integration   # AI集成
```

---

## 💡 技能开发建议

### **1. 从高价值技能开始**
- 先开发架构、MVP等核心技能
- 确保每个技能解决真实痛点

### **2. 保持技能专业化**
- 每个技能专注解决一类问题
- 避免功能过于宽泛

### **3. 强调工具协同**
- 充分利用现有工具的协同效应
- 展示工具组合的独特价值

### **4. 提供具体示例**
- 每个技能都要有详细的使用案例
- 展示不同复杂度场景的应用

### **5. 建立质量标准**
- 所有技能都要有Apache 2.0许可证
- 统一的文档结构和示例

---

## 🔮 技能生态愿景

通过创建这些专业技能，我们可以构建一个**完整的AI驱动开发技能生态系统**：

### **技能协作**
- 技能之间可以相互调用和组合
- 复杂项目可以自动组合多个技能

### **智能推荐**
- 根据项目特征自动推荐技能组合
- 基于历史数据优化技能选择

### **持续学习**
- 技能可以从项目中学习并优化
- 建立技能使用效果反馈机制

### **开放生态**
- 支持第三方技能开发
- 建立技能市场和质量认证体系

这个技能生态将把当前的强大工具平台转化为**更容易使用、更专业化、更智能的AI助手群体**，为不同角色和场景提供精准的专业服务。