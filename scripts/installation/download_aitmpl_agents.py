#!/usr/bin/env python3
"""
AITemplates Agents & MCPs 批量下载器
从 https://www.aitmpl.com/ 批量安装所有agents和MCPs
"""

import subprocess
import json
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple

class AITemplatesDownloader:
    """AITemplates 批量下载器"""

    def __init__(self):
        self.project_dir = Path(__file__).parent
        self.install_dir = self.project_dir / "aitmpl-downloads"
        self.log_file = self.project_dir / "aitmpl_download.log"

        # 创建目录
        self.install_dir.mkdir(exist_ok=True)

        # 设置日志
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

        # 从网站提取的agents列表
        self.agents = [
            # Development Team (7.2K - 1.4K downloads)
            "development-team/frontend-developer",
            "development-team/backend-architect",
            "development-team/ui-ux-designer",
            "development-team/fullstack-developer",
            "development-team/mobile-developer",
            "development-team/devops-engineer",

            # Development Tools (5.6K - 1.4K downloads)
            "development-tools/code-reviewer",
            "development-tools/debugger",
            "development-tools/context-manager",
            "development-tools/test-engineer",
            "development-tools/error-detective",
            "development-tools/mcp-expert",

            # AI Specialists (3.8K - 1.5K downloads)
            "ai-specialists/prompt-engineer",
            "ai-specialists/task-decomposition-expert",
            "ai-specialists/search-specialist",

            # Programming Languages (2.3K - 1.4K downloads)
            "programming-languages/python-pro",
            "programming-languages/typescript-pro",
            "programming-languages/javascript-pro",

            # Database (2.1K - 2.0K downloads)
            "database/database-architect",

            # Expert Advisors (2.0K downloads)
            "expert-advisors/architect-review",

            # Data AI (1.5K downloads)
            "data-ai/ai-engineer",

            # DevOps Infrastructure (1.5K downloads)
            "devops-infrastructure/deployment-engineer",

            # Documentation (1.4K downloads)
            "documentation/api-documenter",
        ]

        # MCPs列表 (58 total)
        self.mcps = [
            # DevTools (3.8K - 174 downloads)
            "devtools/context7",
            "devtools/chrome-devtools",
            "devtools/ios-simulator-mcp",
            "devtools/markitdown",
            "devtools/figma-dev-mode",
            "devtools/serena",

            # Integration (2.1K - 1.2K downloads)
            "integration/memory-integration",
            "integration/github-integration",

            # Browser Automation (2.1K - 259 downloads)
            "browser_automation/playwright-mcp-server",
            "browser_automation/browser-use-mcp-server",
            "browser_automation/playwright-mcp",
            "browser_automation/mcp-server-playwright",
            "browser_automation/browsermcp",
            "browser_automation/mcp-server-browserbase",

            # Database (1.2K - 459 downloads)
            "database/postgresql-integration",
            "database/supabase",
            "database/mysql-integration",

            # Web (1.0K downloads)
            "web/web-fetch",

            # Filesystem (889 downloads)
            "filesystem/filesystem-access",

            # Deepgraph (488 - 160 downloads)
            "deepgraph/deepgraph-nextjs",
            "deepgraph/deepgraph-react",
            "deepgraph/deepgraph-typescript",
            "deepgraph/deepgraph-vue",
        ]

        # 统计信息
        self.stats = {
            "total_agents": len(self.agents),
            "total_mcps": len(self.mcps),
            "successful_installs": 0,
            "failed_installs": 0,
            "start_time": None,
            "end_time": None
        }

    def run_command(self, command: List[str], description: str) -> Tuple[bool, str]:
        """执行命令并返回结果"""
        self.logger.info(f"🔄 {description}")
        self.logger.info(f"命令: {' '.join(command)}")

        try:
            result = subprocess.run(
                command,
                cwd=self.project_dir,
                capture_output=True,
                text=True,
                timeout=300  # 5分钟超时
            )

            if result.returncode == 0:
                self.logger.info(f"✅ {description} - 成功")
                self.stats["successful_installs"] += 1
                return True, result.stdout
            else:
                self.logger.error(f"❌ {description} - 失败")
                self.logger.error(f"错误输出: {result.stderr}")
                self.stats["failed_installs"] += 1
                return False, result.stderr

        except subprocess.TimeoutExpired:
            self.logger.error(f"⏰ {description} - 超时")
            self.stats["failed_installs"] += 1
            return False, "Command timed out"
        except Exception as e:
            self.logger.error(f"💥 {description} - 异常: {str(e)}")
            self.stats["failed_installs"] += 1
            return False, str(e)

    def install_agents(self) -> Dict[str, List[str]]:
        """批量安装agents"""
        self.logger.info("🚀 开始安装Agents...")

        successful = []
        failed = []

        for i, agent in enumerate(self.agents, 1):
            self.logger.info(f"📦 进度: {i}/{len(self.agents)} - 安装 {agent}")

            command = [
                "npx",
                "claude-code-templates@latest",
                f"--agent={agent}",
                "--yes"
            ]

            success, output = self.run_command(
                command,
                f"安装Agent: {agent}"
            )

            if success:
                successful.append(agent)
            else:
                failed.append(agent)

            # 等待一秒避免请求过快
            time.sleep(1)

        return {"successful": successful, "failed": failed}

    def install_mcps(self) -> Dict[str, List[str]]:
        """批量安装MCPs"""
        self.logger.info("🔌 开始安装MCPs...")

        successful = []
        failed = []

        for i, mcp in enumerate(self.mcps, 1):
            self.logger.info(f"📦 进度: {i}/{len(self.mcps)} - 安装 {mcp}")

            command = [
                "npx",
                "claude-code-templates@latest",
                f"--mcp={mcp}",
                "--yes"
            ]

            success, output = self.run_command(
                command,
                f"安装MCP: {mcp}"
            )

            if success:
                successful.append(mcp)
            else:
                failed.append(mcp)

            # 等待一秒避免请求过快
            time.sleep(1)

        return {"successful": successful, "failed": failed}

    def save_results(self, agents_result: Dict, mcps_result: Dict):
        """保存安装结果"""
        results = {
            "installation_summary": {
                "timestamp": datetime.now().isoformat(),
                "stats": self.stats
            },
            "agents": agents_result,
            "mcps": mcps_result
        }

        results_file = self.install_dir / "installation_results.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        self.logger.info(f"📄 安装结果已保存到: {results_file}")

    def generate_report(self, agents_result: Dict, mcps_result: Dict):
        """生成安装报告"""
        report_content = f"""# AITemplates Agents & MCPs 安装报告

**安装时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**项目路径**: {self.project_dir}

## 📊 安装统计

### 总体统计
- **总Agents**: {self.stats['total_agents']} 个
- **总MCPs**: {self.stats['total_mcps']} 个
- **成功安装**: {self.stats['successful_installs']} 个
- **安装失败**: {self.stats['failed_installs']} 个
- **成功率**: {(self.stats['successful_installs'] / (self.stats['successful_installs'] + self.stats['failed_installs']) * 100):.1f}%

### Agents安装结果
- **成功**: {len(agents_result['successful'])} 个
- **失败**: {len(agents_result['failed'])} 个

#### ✅ 成功安装的Agents
"""

        for agent in agents_result['successful']:
            report_content += f"- {agent}\n"

        report_content += "\n#### ❌ 安装失败的Agents\n"
        for agent in agents_result['failed']:
            report_content += f"- {agent}\n"

        report_content += f"""
### MCPs安装结果
- **成功**: {len(mcps_result['successful'])} 个
- **失败**: {len(mcps_result['failed'])} 个

#### ✅ 成功安装的MCPs
"""

        for mcp in mcps_result['successful']:
            report_content += f"- {mcp}\n"

        report_content += "\n#### ❌ 安装失败的MCPs\n"
        for mcp in mcps_result['failed']:
            report_content += f"- {mcp}\n"

        report_content += f"""
## 📁 文件位置
- **安装目录**: {self.install_dir}
- **日志文件**: {self.log_file}
- **结果JSON**: {self.install_dir}/installation_results.json

## 🔍 使用说明

### 查看已安装的组件
```bash
# 查看agents
npx claude-code-templates@latest --list-agents

# 查看MCPs
npx claude-code-templates@latest --mcp-stats
```

### 启动工具
```bash
# 启动分析面板
npx claude-code-templates@latest --analytics

# 启动聊天监控
npx claude-code-templates@latest --chats

# 启动插件管理
npx claude-code-templates@latest --plugins

# 健康检查
npx claude-code-templates@latest --health-check
```

## 📝 备注
- 所有安装通过npx完成，无需手动下载文件
- 安装的agents和MCPs会自动集成到您的Claude Code环境
- 如有问题，请查看日志文件: {self.log_file}
"""

        report_file = self.install_dir / "INSTALLATION_REPORT.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        self.logger.info(f"📋 安装报告已生成: {report_file}")

    def install_all(self):
        """执行完整安装流程"""
        self.logger.info("🎯 开始AITemplates Agents & MCPs批量安装")
        self.stats["start_time"] = datetime.now()

        try:
            # 安装agents
            agents_result = self.install_agents()

            # 安装MCPs
            mcps_result = self.install_mcps()

            # 保存结果
            self.save_results(agents_result, mcps_result)

            # 生成报告
            self.generate_report(agents_result, mcps_result)

            self.stats["end_time"] = datetime.now()
            duration = self.stats["end_time"] - self.stats["start_time"]

            self.logger.info("🎉 安装完成!")
            self.logger.info(f"⏱️  总耗时: {duration}")
            self.logger.info(f"✅ 成功: {self.stats['successful_installs']}")
            self.logger.info(f"❌ 失败: {self.stats['failed_installs']}")

        except Exception as e:
            self.logger.error(f"💥 安装过程中发生异常: {str(e)}")
            self.stats["end_time"] = datetime.now()

def main():
    """主函数"""
    downloader = AITemplatesDownloader()

    print("🚀 AITemplates Agents & MCPs 批量下载器")
    print("=" * 50)
    print(f"📊 计划安装:")
    print(f"   - Agents: {downloader.stats['total_agents']} 个")
    print(f"   - MCPs: {downloader.stats['total_mcps']} 个")
    print(f"   - 总计: {downloader.stats['total_agents'] + downloader.stats['total_mcps']} 个")
    print()
    print("⚠️  开始安装大量组件...")

    downloader.install_all()

if __name__ == "__main__":
    main()