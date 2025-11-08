# OpenSpec Integration Guide

## 🚀 Quick Start

OpenSpec is a specification-driven development methodology that solves the unpredictability of AI-generated code by locking intent before implementation.

### Installation & Setup

```bash
# Clone OpenSpec repository
git clone https://github.com/Fission-AI/OpenSpec.git openspec

# Install dependencies
cd openspec
npm install

# Initialize OpenSpec in your project
npx openspec init
```

### Core Workflow

```bash
# 1. Create a change proposal
openspec propose "Add user authentication system"

# 2. Design the specification
openspec design auth-system-spec

# 3. Validate the specification
openspec validate auth-system-spec --strict

# 4. Implement based on specification
openspec apply auth-system-spec

# 5. Archive completed changes
openspec archive auth-system-spec
```

## 📋 Specification Management

### Change Proposal Structure

```yaml
# openspec/changes/auth-system.md
title: "User Authentication System"
id: "auth-system-001"
status: "proposed"
date: "2025-11-08"

proposed_by: "product-team"
reviewers: ["tech-lead", "security-expert"]

# Problem Statement
problem: |
  Current system lacks user authentication, making it impossible to:
  - Secure user data
  - Implement personalized features
  - Track user sessions
  - Control access to sensitive operations

# Proposed Solution
solution: |
  Implement JWT-based authentication with:
  - User registration and login
  - Password reset functionality
  - Session management
  - Role-based access control

# Success Criteria
success_criteria:
  - Users can register and login successfully
  - Password reset workflow works end-to-end
  - Sessions are properly managed and expired
  - Access control prevents unauthorized operations

# Implementation Requirements
requirements:
  functional:
    - User registration with email verification
    - Secure password storage (bcrypt)
    - JWT token generation and validation
    - Password reset via email
  non_functional:
    - Password security standards
    - Session timeout configuration
    - Rate limiting on auth endpoints
    - Audit logging for security events
```

### Specification Template

```yaml
# openspec/specs/auth-system.md
spec_id: "auth-system-001"
title: "User Authentication System Specification"
version: "1.0.0"
status: "approved"

# API Specification
apis:
  auth:
    register:
      endpoint: "POST /api/auth/register"
      request:
        email: "string (required)"
        password: "string (min 8 chars)"
        name: "string (required)"
      response:
        user_id: "string"
        email: "string"
        name: "string"
        verification_required: "boolean"

    login:
      endpoint: "POST /api/auth/login"
      request:
        email: "string (required)"
        password: "string (required)"
      response:
        token: "string (JWT)"
        user: "User object"
        expires_in: "number"

# Database Schema
database:
  users:
    id: "UUID PRIMARY KEY"
    email: "VARCHAR UNIQUE NOT NULL"
    password_hash: "VARCHAR NOT NULL"
    name: "VARCHAR NOT NULL"
    email_verified: "BOOLEAN DEFAULT FALSE"
    created_at: "TIMESTAMP DEFAULT NOW()"

# Security Requirements
security:
  password_policy:
    min_length: 8
    require_uppercase: true
    require_lowercase: true
    require_numbers: true
    require_special_chars: true

  token_security:
    algorithm: "RS256"
    expires_in: "24 hours"
    refresh_token_rotation: true

# Testing Requirements
testing:
  unit_tests:
    coverage: "> 90%"
    include: "All authentication logic"

  integration_tests:
    scenarios:
      - "User registration flow"
      - "Login with valid credentials"
      - "Login with invalid credentials"
      - "Password reset flow"
      - "Token expiration handling"
```

## 🔧 Integration with AI Tools

### Claude Code Integration

```bash
# Using OpenSpec with Claude Code
claude-code --openspec-auth-system-001

# Claude will automatically:
# 1. Read the specification from openspec/specs/
# 2. Understand the requirements and constraints
# 3. Generate code that complies with the specification
# 4. Validate implementation against spec requirements
```

### Multi-AI Compatibility

```yaml
# OpenSpec works with multiple AI tools:
ai_tools:
  claude_code:
    integration: "native"
    workflow: "openspec apply"

  github_copilot:
    integration: "via-comments"
    workflow: "# OpenSpec: auth-system-001"

  cursor:
    integration: "via-project-config"
    workflow: ".cursor/rules/openspec.json"
```

## 📊 Quality Assurance

### Validation Commands

```bash
# Strict validation (all requirements must be met)
openspec validate auth-system-001 --strict

# Relaxed validation (warnings for missing requirements)
openspec validate auth-system-001 --relaxed

# Custom validation rules
openspec validate auth-system-001 --rules security,performance

# Validation report
openspec validate auth-system-001 --report --output validation-report.md
```

### Quality Gates

```yaml
# .openspec/config.yml
quality_gates:
  pre_commit:
    - validate_specification
    - check_completeness
    - security_review

  pre_merge:
    - validate_implementation
    - test_coverage_check: "> 80%"
    - performance_benchmarks

  pre_release:
    - full_security_audit
    - accessibility_review
    - documentation_completeness
```

## 🔄 Continuous Integration

### GitHub Actions Integration

```yaml
# .github/workflows/openspec.yml
name: OpenSpec Validation

on:
  push:
    paths: ['openspec/**']
  pull_request:
    paths: ['openspec/**']

jobs:
  validate-specs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup OpenSpec
        run: |
          npm install -g @openspec/cli

      - name: Validate Specifications
        run: |
          openspec validate-all --strict

      - name: Generate Compliance Report
        run: |
          openspec compliance-report --output compliance.md

      - name: Upload Report
        uses: actions/upload-artifact@v3
        with:
          name: openspec-report
          path: compliance.md
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: openspec-validate
        name: Validate OpenSpec specifications
        entry: openspec validate
        language: system
        files: '^openspec/.*\.md$'

      - id: openspec-format
        name: Format OpenSpec specifications
        entry: openspec format
        language: system
        files: '^openspec/.*\.md$'
```

## 📈 Team Collaboration

### Review Process

```bash
# Submit specification for review
openspec submit auth-system-001 --reviewers tech-lead,security-expert

# Add review comments
openspec comment auth-system-001 "Security requirements look comprehensive"

# Approve specification
openspec approve auth-system-001 --by tech-lead

# Request changes
openspec request-changes auth-system-001 --by security-expert --reason "Need MFA support"
```

### Change Management

```bash
# Create change proposal
openspec propose "Add MFA to authentication"

# Link to existing specification
openspec link mfa-enhancement auth-system-001 --type "enhancement"

# Track implementation progress
openspec status auth-system-001
openspec progress mfa-enhancement

# Close completed specifications
openspec close auth-system-001 --reason "Successfully implemented"
```

## 🎯 Best Practices

### Specification Design

1. **Clear Problem Statement**: Define the specific problem you're solving
2. **Measurable Success Criteria**: Define what "done" looks like
3. **Comprehensive Requirements**: Cover functional and non-functional aspects
4. **Security First**: Include security requirements from the beginning
5. **Testability**: Ensure all requirements can be tested

### AI Integration

1. **Lock Intent**: Write specifications before AI implementation
2. **Provide Context**: Give AI access to relevant specifications
3. **Validate Output**: Ensure AI output complies with specifications
4. **Iterative Refinement**: Update specifications based on implementation insights

### Team Workflow

1. **Collaborative Authoring**: Involve cross-functional team in specification creation
2. **Early Reviews**: Get technical and business reviews early
3. **Continuous Validation**: Validate specifications throughout development
4. **Knowledge Sharing**: Use specifications as team knowledge base

## 🔍 Advanced Features

### Custom Templates

```yaml
# .openspec/templates/api-feature.yml
title: "{{ feature_name }} API"
version: "1.0.0"

problem: |
  {{ problem_description }}

solution: |
  {{ solution_description }}

api_endpoints:
  - endpoint: "{{ endpoint_method }} {{ endpoint_path }}"
    description: "{{ endpoint_description }}"

    request:
      {{ request_parameters }}

    response:
      {{ response_schema }}

success_criteria:
  - {{ success_criteria_1 }}
  - {{ success_criteria_2 }}
```

### Automated Testing

```bash
# Generate test cases from specification
openspec generate-tests auth-system-001 --framework jest

# Create API documentation
openspec generate-docs auth-system-001 --format openapi

# Generate client SDKs
openspec generate-sdk auth-system-001 --languages javascript,python
```

### Metrics and Analytics

```bash
# Track specification quality metrics
openspec metrics auth-system-001 --detailed

# Team collaboration analytics
openspec analytics --team --period "last-30-days"

# Implementation progress tracking
openspec dashboard --project authentication-system
```

---

## 📚 Additional Resources

- [OpenSpec Documentation](https://github.com/Fission-AI/OpenSpec)
- [Specification Examples](https://github.com/Fission-AI/OpenSpec/tree/main/examples)
- [Community Discord](https://discord.gg/openspec)
- [Best Practices Guide](https://openspec.dev/best-practices)

OpenSpec transforms AI development from unpredictable generation to reliable, specification-driven implementation, ensuring that AI-generated code meets business requirements and quality standards.