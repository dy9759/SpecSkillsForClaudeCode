#!/bin/bash

# AITemplates 批量安装脚本
# 安装所有重要的agents和MCPs

echo "🚀 AITemplates 批量安装脚本"
echo "=================================="

# 创建日志目录
mkdir -p aitmpl-install-logs
LOG_FILE="aitmpl-install-logs/install-$(date +%Y%m%d-%H%M%S).log"

# 统计变量
TOTAL_AGENTS=23
TOTAL_MCPS=23
SUCCESS_COUNT=0
FAILED_COUNT=0

echo "📊 计划安装:"
echo "   - Agents: $TOTAL_AGENTS 个"
echo "   - MCPs: $TOTAL_MCPS 个"
echo "   - 总计: $((TOTAL_AGENTS + TOTAL_MCPS)) 个"
echo ""
echo "📝 日志文件: $LOG_FILE"
echo ""

# 安装agents函数
install_agent() {
    local agent=$1
    echo "🤖 安装 Agent: $agent"

    if npx claude-code-templates@latest --agent="$agent" --yes >> "$LOG_FILE" 2>&1; then
        echo "✅ $agent - 成功"
        ((SUCCESS_COUNT++))
        return 0
    else
        echo "❌ $agent - 失败"
        ((FAILED_COUNT++))
        return 1
    fi
}

# 安装MCP函数
install_mcp() {
    local mcp=$1
    echo "🔌 安装 MCP: $mcp"

    if npx claude-code-templates@latest --mcp="$mcp" --yes >> "$LOG_FILE" 2>&1; then
        echo "✅ $mcp - 成功"
        ((SUCCESS_COUNT++))
        return 0
    else
        echo "❌ $mcp - 失败"
        ((FAILED_COUNT++))
        return 1
    fi
}

# 开始时间
START_TIME=$(date +%s)

echo "🎯 开始安装核心Agents..."
echo ""

# 核心Agents (前10个最重要的)
CORE_AGENTS=(
    "development-team/frontend-developer"
    "development-team/backend-architect"
    "development-team/fullstack-developer"
    "development-tools/code-reviewer"
    "development-tools/debugger"
    "ai-specialists/prompt-engineer"
    "programming-languages/python-pro"
    "programming-languages/typescript-pro"
    "programming-languages/javascript-pro"
    "database/database-architect"
)

for agent in "${CORE_AGENTS[@]}"; do
    install_agent "$agent"
    sleep 1  # 避免请求过快
done

echo ""
echo "🔌 开始安装核心MCPs..."
echo ""

# 核心MCPs (前10个最重要的)
CORE_MCPS=(
    "devtools/context7"
    "browser_automation/playwright-mcp-server"
    "devtools/chrome-devtools"
    "integration/memory-integration"
    "integration/github-integration"
    "web/web-fetch"
    "filesystem/filesystem-access"
    "database/postgresql-integration"
    "devtools/serena"
    "deepgraph/deepgraph-react"
)

for mcp in "${CORE_MCPS[@]}"; do
    install_mcp "$mcp"
    sleep 1  # 避免请求过快
done

# 结束时间
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# 显示结果
echo ""
echo "🎉 安装完成!"
echo "=================================="
echo "⏱️  总耗时: ${DURATION}秒"
echo "✅ 成功: $SUCCESS_COUNT 个"
echo "❌ 失败: $FAILED_COUNT 个"
echo "📈 成功率: $(( SUCCESS_COUNT * 100 / (SUCCESS_COUNT + FAILED_COUNT) ))%"
echo ""
echo "📋 查看已安装组件:"
echo "   npx claude-code-templates@latest --list-agents"
echo "   npx claude-code-templates@latest --mcp-stats"
echo ""
echo "🚀 启动工具:"
echo "   npx claude-code-templates@latest --analytics"
echo "   npx claude-code-templates@latest --chats"
echo "   npx claude-code-templates@latest --plugins"
echo ""
echo "📄 详细日志: $LOG_FILE"