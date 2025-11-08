# PRD Skill Usage Examples

## 📚 Real-World Examples

### Example 1: New Mobile Application

**User Input:**
```
"Help me create a PRD for a fitness tracking app with social features"
```

**Expected Workflow:**
1. **Phase 1 - Exploration**
   - `/sc:brainstorm "fitness tracking app with social features"`
   - `/sc:business-panel "fitness app market analysis and competitive landscape"`

2. **Phase 2 - Project Foundation**
   - Generate project brief with:
     - Target audience definition
     - Success metrics (user engagement, retention rates)
     - Competitive differentiation

3. **Phase 3 - Requirements Generation**
   - Use BMAD PRD Template for comprehensive requirements
   - Define epics like:
     - User authentication & profiles
     - Workout tracking & logging
     - Social challenges & leaderboards
     - Progress analytics & insights

4. **Phase 4 - Quality Validation**
   - Run PM checklist validation
   - Expert review of technical feasibility
   - UX evaluation of social features

5. **Phase 5 - Design Preparation**
   - `/sc:design "mobile fitness app architecture"`
   - Generate UX expert prompt for social interaction design

6. **Phase 6 - Implementation Planning**
   - `/sc:workflow "fitness app development roadmap"`
   - Create team-specific prompts for mobile development

---

### Example 2: Enterprise Feature Addition

**User Input:**
```
"I need to write requirements for adding role-based access control to our existing SaaS platform"
```

**Expected Workflow:**
1. **Phase 3 - Direct Requirements** (Skip exploration - clear need)
   - `/speckit.specify "add role-based access control system with user roles, permissions, and administrative interface"`

2. **Phase 4 - Quality Validation**
   - Generate security-focused checklist
   - Validate compliance requirements (GDPR, SOC2)
   - Technical feasibility assessment

3. **Phase 5 - Design Preparation**
   - `/sc:design "RBAC system architecture for existing SaaS platform"`
   - Integration requirements with existing authentication

4. **Phase 6 - Implementation Planning**
   - Migration strategy for existing users
   - Testing requirements for security validation

---

### Example 3: System Architecture Redesign

**User Input:**
```
"We need to restructure our monolithic e-commerce platform into microservices"
```

**Expected Workflow:**
1. **Phase 3 - Architecture Change Proposal**
   - Create OpenSpec change proposal under `openspec/changes/microservices-migration/`
   - Include detailed impact analysis and migration strategy

2. **Phase 4 - Technical Validation**
   - `openspec validate microservices-migration --strict`
   - `/sc:spec-panel "microservices architecture review"`
   - Performance and scalability analysis

3. **Phase 5 - Detailed Architecture**
   - Service boundary definitions
   - Data migration strategies
   - API contract specifications

---

### Example 4: Internal Tool Development

**User Input:**
```
"Help me create requirements for an internal project management dashboard"
```

**Expected Workflow:**
1. **Phase 2 - Project Foundation** (Skip exploration - internal need)
   - Project brief focusing on:
     - Internal stakeholder needs
     - Integration with existing tools
     - Productivity improvement metrics

2. **Phase 3 - Requirements**
   - BMAD PRD Template for internal tool
   - Features like:
     - Task tracking and assignment
     - Progress visualization
     - Team collaboration tools
     - Reporting and analytics

3. **Phase 4 - Stakeholder Validation**
   - Internal review checklists
   - Integration requirements with existing systems
   - Training and adoption planning

---

### Example 5: API Feature Development

**User Input:**
```
"Let's spec out a REST API for third-party integrations"
```

**Expected Workflow:**
1. **Phase 3 - Technical Requirements**
   - `/speckit.specify "REST API for third-party integrations with authentication, rate limiting, and comprehensive documentation"`
   - Focus on technical specifications rather than user features

2. **Phase 4 - API Quality**
   - API design best practices validation
   - Security and performance requirements
   - Documentation standards

3. **Phase 5 - Architecture**
   - `/sc:design "REST API architecture with gateway, authentication, and rate limiting"`
   - Integration patterns and data contracts

---

## 🎯 Advanced Usage Patterns

### Multi-Stakeholder Projects
For projects involving multiple departments:
```
"Help me create a PRD for a customer data platform that needs to serve marketing, sales, and customer support teams"
```

**Pattern:**
- Phase 1: Extensive stakeholder analysis
- Phase 2: Cross-functional requirement gathering
- Phase 3: Complex requirements with multiple user personas
- Phase 4: Multi-expert validation
- Phase 5: Integration architecture planning

### Regulatory Compliance
For regulated industries:
```
"I need requirements for a healthcare application that must comply with HIPAA regulations"
```

**Pattern:**
- Phase 2: Compliance and regulatory research
- Phase 3: Security and privacy-focused requirements
- Phase 4: Compliance validation checklists
- Phase 5: Security-first architecture design

### High-Risk Projects
For mission-critical systems:
```
"Help me create requirements for a payment processing system that handles financial transactions"
```

**Pattern:**
- Phase 1: Risk assessment and business analysis
- Phase 2: Comprehensive security and compliance requirements
- Phase 3: Detailed technical specifications with fail-safes
- Phase 4: Multiple validation rounds with security experts
- Phase 5: Redundancy and disaster recovery planning

## 💡 Pro Tips for Specific Scenarios

### For Startup MVPs
- Focus on Phase 1 (market validation) and Phase 3 (core features only)
- Use Lean Startup principles in requirements
- Emphasize speed to market and learning metrics

### For Enterprise Software
- Heavy emphasis on Phase 4 (comprehensive validation)
- Integration requirements in Phase 5
- Detailed rollout and migration planning

### For User-Facing Features
- Include extensive UX validation in Phase 4
- User testing requirements in acceptance criteria
- Accessibility and internationalization considerations

### For Backend Systems
- Technical feasibility focus in Phase 4
- Performance and scalability requirements
- Monitoring and observability specifications

## 📊 Expected Outputs

### Complete PRD Package Structure
```
project-folder/
├── docs/
│   ├── prd.md                    # Main requirements document
│   ├── project-brief.md          # Executive summary
│   └── checklists/
│       ├── pm-checklist.md       # Product manager validation
│       ├── architect-checklist.md # Technical review
│       ├── ux-checklist.md       # User experience validation
│       └── security-checklist.md # Security and compliance
├── prompts/
│   ├── ux-expert-prompt.md       # Design team handoff
│   ├── architect-prompt.md       # Architecture requirements
│   ├── dev-team-prompt.md        # Development specifications
│   └── qa-team-prompt.md         # Testing requirements
└── workflows/
    ├── implementation-workflow.md # Development roadmap
    ├── testing-workflow.md       # Quality assurance plan
    └── rollout-workflow.md       # Deployment strategy
```

### Quality Metrics
- **Completeness**: All mandatory sections populated
- **Clarity**: Requirements are unambiguous and testable
- **Alignment**: Business and technical requirements aligned
- **Feasibility**: Technical implementation validated
- **Traceability**: Clear link from business needs to requirements

## 🔄 Iterative Improvement

### Feedback Loops
1. **During Creation**: Real-time validation and clarification
2. **Post-Implementation**: Lessons learned for template improvement
3. **Cross-Project**: Pattern recognition and best practice sharing

### Continuous Enhancement
- Template refinement based on usage patterns
- Checklist evolution based on quality metrics
- Workflow optimization based on team feedback

---

These examples demonstrate how the PRD skill adapts to different project types, complexities, and organizational contexts while maintaining consistent quality and comprehensive coverage of requirements.