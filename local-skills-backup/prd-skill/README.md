# PRD Skill - Complete Product Requirements Document Workflow

## 🚀 Quick Start

**Basic Usage:**
```
"Help me create a PRD for [your product/feature idea]"
```

**Examples:**
- "Help me create a PRD for a new task management app"
- "I need to write requirements for adding user authentication"
- "Let's spec out a customer analytics dashboard"

## 📋 What This Skill Does

The PRD skill automatically guides you through creating complete Product Requirements Documents using the powerful toolset in this repository. It intelligently selects the right tools and processes based on your project's complexity and scope.

### 🎯 Key Features

- **Intelligent Phase Selection** - Automatically picks the right starting point
- **Multi-Tool Orchestration** - Combines BMAD, SpeckKit, OpenSpec, and SuperClaude tools
- **Quality Assurance** - Built-in validation and expert review processes
- **Team Coordination** - Generates role-specific prompts and checklists
- **Business Intelligence** - Multi-expert analysis when needed

## 🔄 Workflow Phases

### Phase 1: Exploration 🚀
*For new ideas and market validation*
- Interactive brainstorming (`/sc:brainstorm`)
- Multi-expert business analysis (`/sc:business-panel`)

### Phase 2: Project Foundation 🏗️
*For scoping and success metrics*
- Project brief creation using BMAD templates

### Phase 3: Requirements Generation 📋
*For detailed specification*
- **Simple features**: `/speckit.specify`
- **Complex products**: BMAD PRD Template
- **Architecture changes**: OpenSpec proposals

### Phase 4: Quality Validation 🔍
*For review and refinement*
- Automated quality checklists
- Expert review processes

### Phase 5: Design Preparation 🎨
*For technical handoff*
- System architecture prompts
- Design team briefs

### Phase 6: Implementation Planning 🛠️
*For development execution*
- Implementation workflows
- Team-specific guidance

## 🛠️ Tool Integration

This skill orchestrates four powerful frameworks in your repository:

| Tool | Primary Use | When Triggered |
|------|-------------|----------------|
| **BMAD Core** | Comprehensive PRDs | Complex products, multiple stakeholders |
| **SpeckKit** | Rapid feature specs | Single function, focused requirements |
| **OpenSpec** | Architecture changes | System modifications, breaking changes |
| **SuperClaude** | Expert analysis | Market validation, design reviews |

## 📊 Example Workflows

### New Mobile App
```
User: "Help me create a PRD for a fitness tracking app"

Path: Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6
Tools: /sc:brainstorm → /sc:business-panel → BMAD PRD → Quality Checks → /sc:design → /sc:workflow
```

### Single Feature Addition
```
User: "I need to add PDF export functionality"

Path: Phase 3 → Phase 4 → Phase 6
Tools: /speckit.specify → Quality Validation → Implementation Planning
```

### System Architecture Change
```
User: "We need to migrate from monolith to microservices"

Path: Phase 3 → Phase 4 → Phase 5
Tools: OpenSpec Proposal → Validation → /sc:spec-panel
```

## 🎯 Output Deliverables

Each PRD creation generates a complete package:

### Core Documents
- **prd.md** - Main requirements document
- **project-brief.md** - Executive summary (when needed)
- **checklists/** - Quality validation checklists

### Team Handoffs
- **ux-expert-prompt.md** - Design team guidance
- **architect-prompt.md** - Architecture team requirements
- **dev-team-prompt.md** - Development team specifications

### Implementation Guides
- **implementation-workflow.md** - Development roadmap
- **validation-workflow.md** - Testing and validation plan

## 💡 Pro Tips

### For Best Results
1. **Be Specific**: Provide clear details about your idea
2. **Identify Users**: Who will use this product/feature?
3. **Define Success**: What does success look like?
4. **Know Constraints**: Any technical or business limitations?

### When to Use Which Phase
- **Vague idea?** → Start with Phase 1 (Exploration)
- **Clear concept?** → Start with Phase 3 (Requirements)
- **System change?** → Use OpenSpec directly
- **Team project?** → Use BMAD PRD Template

### Quality Assurance
- Always review generated checklists
- Use the expert panel for important decisions
- Validate requirements are testable and measurable

## 🔧 Advanced Features

### Intelligent Adaptation
The skill automatically adapts to:
- **Project complexity** - Simple vs. multifaceted requirements
- **Team structure** - Individual vs. enterprise workflows
- **Risk level** - Low-risk vs. high-impact changes
- **Timeline pressure** - Rapid prototyping vs. comprehensive analysis

### Continuous Learning
- Learns from successful PRD patterns
- Improves based on your feedback
- Adapts to organizational preferences
- Tracks quality metrics over time

## 🎨 Customization

### Adding Your Own Templates
Modify `.bmad-core/templates/prd-tmpl.yaml` to match your organization's standards.

### Custom Checklists
Create organization-specific checklists in `.bmad-core/checklists/` directory.

### Integration Points
The skill integrates with:
- Git workflows for version control
- Project management tools for task tracking
- Documentation systems for knowledge management
- Communication platforms for team coordination

## 📞 Getting Help

### Troubleshooting
- **Confused about starting point?** The skill will recommend the optimal phase
- **Scope creep issues?** Use quality validation phases to maintain boundaries
- **Stakeholder disagreements?** Leverage business panel analysis
- **Technical concerns?** Use architecture review phases early

### Best Practice Resources
- Review generated checklists for quality standards
- Use multi-expert analysis for critical decisions
- Maintain traceability from requirements to implementation
- Collect feedback for continuous improvement

---

## 🚀 Ready to Start?

Simply describe your product or feature idea, and the PRD skill will guide you through the complete process of creating professional, implementation-ready requirements documentation.

**Example**: *"Help me create a PRD for a collaborative document editing platform with real-time features and version control"*