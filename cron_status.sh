#!/bin/bash

# SpecSkills定时任务状态检查脚本

echo "🔍 SpecSkills定时任务状态检查"
echo "=================================="

# 检查当前crontab
echo "📋 当前的定时任务:"
crontab -l | grep -v claude || echo "无相关定时任务"

echo ""
echo "📊 备份任务详情:"
crontab -l | grep "manage_local_backup.py" | while read -r line; do
    echo "  📅 执行时间: $(echo "$line" | awk '{print $1, $2}' | sed 's/0 2/凌晨2点/')"
    echo "  🔄 执行命令: $(echo "$line" | awk '{print $3" "$4" "$5}')"
    echo "  📝 日志文件: backup.log"
done

echo ""
echo "📝 备份日志状态:"
if [ -f "backup.log" ]; then
    echo "  ✅ 日志文件存在"
    echo "  📊 日志大小: $(ls -lh backup.log | awk '{print $5}')"
    echo "  🕐 最后修改: $(ls -l backup.log | awk '{print $6" "$7" "$8}')"
    echo "  📄 最近5条记录:"
    tail -5 backup.log | sed 's/^/    /'
else
    echo "  ❌ 日志文件不存在"
fi

echo ""
echo "🔧 项目脚本状态:"
if [ -f "manage_local_backup.py" ]; then
    echo "  ✅ 备份脚本存在"
    echo "  🚀 执行权限: $(ls -l manage_local_backup.py | awk '{print $1}')"
else
    echo "  ❌ 备份脚本不存在"
fi

if [ -d "local-skills-backup" ]; then
    echo "  ✅ 备份目录存在"
    skill_count=$(ls -1 local-skills-backup/ 2>/dev/null | wc -l)
    echo "  📊 备份技能数量: $skill_count"
else
    echo "  ❌ 备份目录不存在"
fi

echo ""
echo "🎯 系统信息:"
echo "  🖥️  当前时间: $(date)"
echo "  📍 当前目录: $(pwd)"
echo "  👤 当前用户: $(whoami)"

echo ""
echo "📋 快速操作:"
echo "  手动执行备份: python3 manage_local_backup.py backup"
echo "  查看备份状态: python3 manage_local_backup.py status"
echo "  查看完整日志: cat backup.log"
echo "  清理日志: echo '# $(date)' > backup.log"
echo ""
echo "⚙️  定时任务管理:"
echo "  编辑定时任务: crontab -e"
echo "  删除所有任务: crontab -r"
echo "  重新加载任务: crontab -l | crontab -"