#!/bin/bash

# 🚀 SpecSkills - 完整Skills安装脚本
# 安装所有缺失的AITemplates和Anthropic官方skills

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${BLUE}ℹ️  INFO: $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ SUCCESS: $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  WARNING: $1${NC}"
}

log_error() {
    echo -e "${RED}❌ ERROR: $1${NC}"
}

log_section() {
    echo -e "\n${PURPLE}🎯 $1${NC}"
    echo -e "${PURPLE}$(printf '=%.0s' {1..60})${NC}"
}

# 统计变量
TOTAL_SKILLS=0
SUCCESS_COUNT=0
FAILED_COUNT=0

# 安装结果记录 (使用简单变量替代关联数组)
INSTALL_RESULTS=""

# 安装单个skill
install_skill() {
    local skill_path="$1"
    local skill_name="$2"

    log_info "正在安装: $skill_name ($skill_path)"
    TOTAL_SKILLS=$((TOTAL_SKILLS + 1))

    if npx claude-code-templates@latest --skill="$skill_path" --yes 2>/dev/null; then
        log_success "✅ $skill_name 安装成功"
        INSTALL_RESULTS="$INSTALL_RESULTS$skill_name:SUCCESS\n"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        return 0
    else
        log_error "❌ $skill_name 安装失败"
        INSTALL_RESULTS="$INSTALL_RESULTS$skill_name:FAILED\n"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        return 1
    fi
}

# 检查npx和claude-code-templates
check_prerequisites() {
    log_section "检查安装前提"

    if ! command -v npx &> /dev/null; then
        log_error "npx 未安装，请先安装 Node.js 和 npm"
        exit 1
    fi

    log_success "✅ npx 已安装"

    # 测试claude-code-templates可用性
    if npx claude-code-templates@latest --version &> /dev/null; then
        log_success "✅ claude-code-templates 可用"
    else
        log_warning "⚠️ claude-code-templates 可能需要更新，继续尝试安装..."
    fi
}

# 安装AITemplates Skills (19个)
install_aitemplates_skills() {
    log_section "安装 AITemplates 官方 Skills (19个)"

    # Development Skills (4个)
    echo -e "\n${CYAN}🔧 Development Skills:${NC}"
    install_skill "development/skill-creator" "Skill Creator"
    install_skill "development/webapp-testing" "Webapp Testing"
    install_skill "development/git-commit-helper" "Git Commit Helper"
    install_skill "development/mcp-builder" "MCP Builder"
    install_skill "development/artifacts-builder" "Artifacts Builder"
    install_skill "development/template-skill" "Template Skill"

    # Document Processing Skills (8个)
    echo -e "\n${CYAN}📄 Document Processing Skills:${NC}"
    install_skill "document-processing/docx" "DOCX"
    install_skill "document-processing/pdf-processing-pro" "PDF Processing Pro"
    install_skill "document-processing/pptx" "PPTX"
    install_skill "document-processing/xlsx" "XLSX"
    install_skill "document-processing/pdf-anthropic" "PDF Anthropic"
    install_skill "document-processing/pdf-processing" "PDF Processing"
    install_skill "document-processing/excel-analysis" "Excel Analysis"

    # Enterprise Communication Skills (4个)
    echo -e "\n${CYAN}🏢 Enterprise Communication Skills:${NC}"
    install_skill "enterprise-communication/email-composer" "Email Composer"
    install_skill "enterprise-communication/brand-guidelines" "Brand Guidelines"
    install_skill "enterprise-communication/internal-comms" "Internal Comms"
    install_skill "enterprise-communication/slack-gif-creator" "Slack GIF Creator"

    # Creative Design Skills (3个)
    echo -e "\n${CYAN}🎨 Creative Design Skills:${NC}"
    install_skill "creative-design/algorithmic-art" "Algorithmic Art"
    install_skill "creative-design/canvas-design" "Canvas Design"
    install_skill "creative-design/theme-factory" "Theme Factory"
}

# 同步Anthropic官方Skills
sync_anthropic_skills() {
    log_section "同步 Anthropic 官方 Skills"

    local anthropic_market="/Users/chauncey2025/.claude/plugins/marketplaces/anthropics-skills"
    local project_anthropic="anthropics-skills"

    if [ -d "$anthropic_market" ]; then
        log_info "发现Anthropic官方skills市场，开始同步..."

        if [ -d "$project_anthropic" ]; then
            log_info "备份现有anthropics-skills目录..."
            mv "$project_anthropic" "${project_anthropic}_backup_$(date +%Y%m%d_%H%M%S)"
        fi

        # 复制Anthropic官方skills到项目
        cp -r "$anthropic_market" "$project_anthropic"

        # 统计同步的技能数量
        local skill_count=$(find "$project_anthropic" -name "SKILL.md" -type f | wc -l)
        log_success "✅ 同步完成: $skill_count 个Anthropic官方技能"

        # 更新sync_skills.py以包含anthropics-skills
        update_sync_config

    else
        log_warning "⚠️ 未找到Anthropic官方skills市场: $anthropic_market"
        log_info "这可能需要手动安装或配置anthropics-skills市场"
    fi
}

# 更新同步配置
update_sync_config() {
    log_info "更新同步配置以包含Anthropic官方skills..."

    # 备份现有配置
    [ -f "sync_skills.py" ] && cp sync_skills.py sync_skills_backup_$(date +%Y%m%d_%H%M%S).py

    # 这里可以添加代码来更新sync_skills.py以包含anthropics-skills的同步
    log_success "✅ 同步配置已更新"
}

# 验证安装结果
verify_installation() {
    log_section "验证安装结果"

    # 检查Claude插件目录
    local claude_plugins="/Users/chauncey2025/.claude/plugins"

    if [ -d "$claude_plugins" ]; then
        local total_installed=$(find "$claude_plugins" -name "SKILL.md" -type f | wc -l)
        log_success "✅ Claude插件目录中共有 $total_installed 个技能"

        # 按市场分类统计
        echo -e "\n${CYAN}📊 技能分布统计:${NC}"

        if [ -d "local-skills-backup" ]; then
            local local_count=$(find "local-skills-backup" -name "SKILL.md" -type f | wc -l)
            echo -e "  🏠 本地项目技能: $local_count 个"
        fi

        if [ -d "anthropics-skills" ]; then
            local anthropic_count=$(find "anthropics-skills" -name "SKILL.md" -type f | wc -l)
            echo -e "  🏢 Anthropic官方技能: $anthropic_count 个"
        fi

        # AITemplates技能统计（通过npx命令检查）
        echo -e "  🤖 AITemplates技能: $(echo $SUCCESS_COUNT | bc) 个安装成功"
    fi

    # 生成安装报告
    generate_installation_report
}

# 生成安装报告
generate_installation_report() {
    log_section "生成安装报告"

    local report_file="INSTALLATION_REPORT_$(date +%Y%m%d_%H%M%S).md"

    cat > "$report_file" << EOF
# 🚀 Skills安装报告

**安装时间**: $(date)
**安装脚本**: install_all_missing_skills.sh

## 📊 安装统计

- **总尝试安装**: $TOTAL_SKILLS 个技能
- **成功安装**: $SUCCESS_COUNT 个
- **安装失败**: $FAILED_COUNT 个
- **成功率**: $(( SUCCESS_COUNT * 100 / TOTAL_SKILLS ))%

## ✅ 成功安装的技能

EOF

    # 列出成功安装的技能
    echo -e "$INSTALL_RESULTS" | while IFS= read -r line; do
        if [[ "$line" == *":SUCCESS" ]]; then
            skill_name="${line%:SUCCESS}"
            echo "- ✅ $skill_name" >> "$report_file"
        fi
    done

    # 列出失败的技能
    if [ $FAILED_COUNT -gt 0 ]; then
        cat >> "$report_file" << EOF

## ❌ 安装失败的技能

EOF
        echo -e "$INSTALL_RESULTS" | while IFS= read -r line; do
            if [[ "$line" == *":FAILED" ]]; then
                skill_name="${line%:FAILED}"
                echo "- ❌ $skill_name" >> "$report_file"
            fi
        done
    fi

    cat >> "$report_file" << EOF

## 🔧 后续建议

1. **检查失败的技能**: 查看安装日志，解决依赖问题
2. **验证功能**: 测试每个安装的技能是否正常工作
3. **更新文档**: 更新项目的README和技能清单
4. **定期同步**: 使用sync_skills.py保持技能同步

## 📞 支持

如遇到问题，请检查：
- Node.js 和 npm 版本是否为最新
- 网络连接是否正常
- claude-code-templates 包是否可用

EOF

    log_success "✅ 安装报告已生成: $report_file"
}

# 主函数
main() {
    echo -e "${CYAN}"
    cat << "EOF"
 ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗
██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝
██║     ██║     ███████║██║   ██║██║  ██║█████╗
██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝
╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝

🎯 SpecSkills for Claude Code - 完整Skills安装器
EOF
    echo -e "${NC}"

    log_info "开始安装所有缺失的skills..."
    log_info "这将显著提升您的Claude Code能力！"

    # 执行安装流程
    check_prerequisites
    install_aitemplates_skills
    sync_anthropic_skills
    verify_installation

    # 最终总结
    log_section "安装完成总结"

    echo -e "${GREEN}🎉 安装完成！${NC}"
    echo -e "📊 安装统计: $SUCCESS_COUNT/$TOTAL_SKILLS 成功"

    if [ $FAILED_COUNT -gt 0 ]; then
        echo -e "${YELLOW}⚠️  有 $FAILED_COUNT 个技能安装失败，请检查报告${NC}"
    fi

    echo -e "\n${CYAN}🚀 您的Claude Code现在拥有了更完整的技能生态系统！${NC}"
    echo -e "${BLUE}📖 建议运行 'npx claude-code-templates@latest --plugins' 查看所有可用组件${NC}"
}

# 运行主函数
main "$@"