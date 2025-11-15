#!/bin/bash

# SpecSkills同步脚本 - Shell版本
# 提供简单的命令行接口

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/sync_skills.py"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印彩色消息
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# 显示帮助信息
show_help() {
    echo "SpecSkills同步管理器"
    echo ""
    echo "用法: $0 [命令] [选项]"
    echo ""
    echo "命令:"
    echo "  sync       同步所有技能（仅同步有变更的）"
    echo "  force      强制同步所有技能（忽略变更检测）"
    echo "  status     显示同步状态"
    echo "  clean      清理目标目录"
    echo "  install    安装到系统（创建符号链接）"
    echo "  uninstall  从系统卸载"
    echo "  help       显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 sync          # 同步技能"
    echo "  $0 status        # 查看状态"
    echo "  $0 force         # 强制同步"
    echo "  $0 install       # 安装到系统"
}

# 检查Python是否可用
check_python() {
    if ! command -v python3 &> /dev/null; then
        print_error "Python3 未安装或不在PATH中"
        exit 1
    fi
}

# 检查Python脚本
check_script() {
    if [[ ! -f "$PYTHON_SCRIPT" ]]; then
        print_error "同步脚本不存在: $PYTHON_SCRIPT"
        exit 1
    fi
}

# 运行Python脚本
run_python_script() {
    check_python
    check_script

    local cmd="$1"
    print_info "执行命令: $cmd"
    python3 "$PYTHON_SCRIPT" "$cmd"
}

# 安装到系统
install_to_system() {
    local install_dir="$HOME/.local/bin"
    local link_path="$install_dir/specskills-sync"

    if [[ ! -d "$install_dir" ]]; then
        print_info "创建安装目录: $install_dir"
        mkdir -p "$install_dir"
    fi

    # 创建符号链接
    if [[ -L "$link_path" ]]; then
        print_warning "符号链接已存在，更新之"
        rm "$link_path"
    fi

    ln -s "$0" "$link_path"
    print_success "已安装到: $link_path"

    # 检查PATH
    if [[ ":$PATH:" != *":$install_dir:"* ]]; then
        print_warning "请将 $install_dir 添加到您的PATH中"
        echo "在 ~/.bashrc 或 ~/.zshrc 中添加:"
        echo "export PATH=\"\$PATH:$install_dir\""
    fi
}

# 从系统卸载
uninstall_from_system() {
    local install_dir="$HOME/.local/bin"
    local link_path="$install_dir/specskills-sync"

    if [[ -L "$link_path" ]]; then
        rm "$link_path"
        print_success "已从系统卸载"
    else
        print_warning "未找到安装的符号链接"
    fi
}

# 设置自动同步
setup_auto_sync() {
    local script_path="$(realpath "$0")"
    local crontab_entry="*/5 * * * * cd '$(dirname "$script_path")' && python3 sync_skills.py sync >/dev/null 2>&1"

    print_info "设置每5分钟自动同步..."

    # 检查是否已有crontab条目
    if crontab -l 2>/dev/null | grep -q "sync_skills.py"; then
        print_warning "自动同步已设置"
        crontab -l 2>/dev/null | grep "sync_skills.py"
    else
        # 添加到crontab
        (crontab -l 2>/dev/null; echo "$crontab_entry") | crontab -
        print_success "自动同步已设置（每5分钟检查一次）"
        print_info "使用 'crontab -e' 编辑定时任务"
    fi
}

# 移除自动同步
remove_auto_sync() {
    print_info "移除自动同步..."

    # 移除crontab条目
    crontab -l 2>/dev/null | grep -v "sync_skills.py" | crontab -
    print_success "自动同步已移除"
}

# 主函数
main() {
    local command="${1:-help}"

    case "$command" in
        "sync")
            run_python_script "sync"
            ;;
        "force")
            run_python_script "force"
            ;;
        "status")
            run_python_script "status"
            ;;
        "clean")
            run_python_script "clean"
            ;;
        "install")
            install_to_system
            ;;
        "uninstall")
            uninstall_from_system
            ;;
        "auto")
            setup_auto_sync
            ;;
        "no-auto")
            remove_auto_sync
            ;;
        "help"|"-h"|"--help")
            show_help
            ;;
        *)
            print_error "未知命令: $command"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# 运行主函数
main "$@"