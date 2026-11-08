# 跑步教练 Running Coach

中文 ｜ [English](#english)

把 Garmin 与 RQrun 的跑步记录整理成图表报告，并结合训练和恢复数据给出简短建议。适合希望复盘跑量、比较两端同步记录的跑友。

> **项目状态：开发预览。** 两个 MCP 已分别完成本地协议冒烟测试，报告模板已用模拟数据测试；ChatGPT 中的真实账号、定时任务和通知尚未完成端到端验证。欢迎先试用并反馈，不要依赖它作为唯一训练依据。

![跑步周报示例，使用模拟数据](plugins/running-coach/skills/running-coach/examples/sample-report.svg)

## 可以做什么

- 读取 Garmin 和 RQrun 的训练记录，识别可能的重复活动，避免将同一次跑步算两遍。
- 按日、周、月、年设计图表为主的复盘；Skill 可按数据选择跑量柱状图、强度分布、恢复趋势、单次分段与平台对比等展示，并可使用 ECharts、Plotly 等宿主可用的工具。内置 SVG 只是基础后备模板，丰富图表的实际生成取决于运行环境。
- 结合已有计划、训练负荷和恢复信息，给出有依据的简短建议；缺少数据时说明限制。
- 根据用户要求引导设置周期报告和训练提醒；实际能否定时、交付及通知取决于所在平台的能力和权限。

## 使用前准备

本项目是 Skill，负责分析流程和报告；数据来自两个独立的 MCP：

| 数据源 | 项目 | 用途 |
| --- | --- | --- |
| Garmin | [garmin-mcp](https://github.com/hongshunanhai/garmin-mcp) | 训练、睡眠、恢复等数据 |
| RQrun | [rqrun-mcp](https://github.com/hongshunanhai/rqrun-mcp) | 跑步记录、跑力和训练分析 |

首次使用时 Skill 会检查可用工具，并引导安装或连接缺失的数据源。可以先只连接一个；两个数据源的登录、权限和数据可用性各自独立。请先阅读对应项目的安装说明和许可证：Garmin MCP 使用非商业许可证，其约束独立于本项目。

## 安装与首测

### Codex 本地

1. 下载本仓库，将完整的 `plugins/running-coach/skills/running-coach` 目录复制到用户级 Skill 目录 `~/.agents/skills/running-coach`，或项目级目录 `.agents/skills/running-coach`。保留其中的 `references`、`scripts` 和 `examples`。
2. 开启新会话，输入：`使用 running-coach，帮我连接 Garmin 和 RQrun，生成本周跑步报告。`
3. 按提示检查或安装两个 MCP、完成登录，再检查首次报告的数据来源和区间。已有的 MCP 不需要重装。

### ChatGPT

仓库包含用于本地测试的 ChatGPT 桌面插件与 marketplace。以下是**待端到端验证的安装路径**，不是已经验证的一键安装：

1. 下载或克隆本仓库，在仓库根目录执行 `codex plugin marketplace add .`，将本地 marketplace 加入 Codex 配置。
2. 重启 ChatGPT 桌面 App，在 Work 的插件目录中选择“跑步教练”来源，找到“跑步教练”并点击安装。开启本地 Work 会话，运行插件的设置或选择该 Skill。
3. 按引导分别连接 Garmin 和 RQrun，并在新对话里验证两边都能读取活动，再生成第一份周报。

这条路径需要本机安装 Codex CLI，可能受账号、版本和工作区权限影响。安装 Skill 不会自动安装或登录两个 MCP。Codex 的本地 MCP 配置不会自动等同于 ChatGPT 的插件连接；Garmin 支持 HTTP，RQrun 使用本地 stdio。具体接入参考 [首次接入](plugins/running-coach/skills/running-coach/references/setup.md) 和 [OpenAI 插件打包文档](https://developers.openai.com/plugins/build/plugins)。本仓库发布到 GitHub、安装和首测验证后，才能给出真实的 GitHub 地址和确认可用的快捷安装命令。

### 试试这样说

```text
用我的 Garmin 和 RQrun 数据做一份上周跑步报告，以图表为主。
比较昨天那次跑步在两个平台的距离和配速，有差异就解释可能原因。
结合最近的训练和恢复情况，给我明天的训练建议。
如果当前平台支持定时任务，每周一早上 8 点给我上一周的报告，时区为上海。
```

先检查一次手动报告，再设置定时任务。运行依赖本地文件时，定时任务的运行条件取决于宿主；登录过期或设备未同步时报告可能不完整。

## 本地查看示例图

需要 Python 3，无额外绘图库：

```bash
python3 plugins/running-coach/skills/running-coach/scripts/render_report.py plugins/running-coach/skills/running-coach/examples/sample.json report.svg
```

`sample.json` 和示例图仅为模拟数据。实际报告需要先读取并核实用户数据，再按样例结构填入；模板不会自动连接账号。敏感数据不要提交到 GitHub。

## 隐私与使用边界

账号密码只应输入各平台官方登录页面，不要粘贴密码、验证码、Cookie 或令牌。数据会交由用户选择的 AI 客户端及其模型处理；分享报告前请检查内容。训练建议不构成医疗诊断，身体不适或伤病时应优先考虑休息并寻求专业帮助。

## 反馈与验证

提交问题时请描述平台、操作步骤和报错，先移除账号、位置轨迹、健康数据和凭据。项目的验证步骤和发布前检查见 [CONTRIBUTING.md](CONTRIBUTING.md)。

本项目采用 [PolyForm Noncommercial License 1.0.0](LICENSE)：个人非商业使用请遵守许可证条款；其他使用方式请先联系版权人取得授权。许可证允许用途以完整条款为准。两个 MCP 的许可证各自独立。

## English

Turn Garmin and RQrun running records into chart-first reports with short, evidence-based training and recovery suggestions — for runners who want to review mileage and compare synced records across both platforms.

> **Status: development preview.** Both MCPs have passed local protocol smoke tests and the report template was tested with simulated data; real accounts, scheduled jobs, and notifications in ChatGPT are not yet verified end-to-end. Try it and share feedback, but do not rely on it as your only training reference.

![Sample weekly report, simulated data](plugins/running-coach/skills/running-coach/examples/sample-report.svg)

### What it can do

- Read workouts from Garmin and RQrun and flag possible duplicates, so the same run is not counted twice.
- Design chart-first reviews by day, week, month, and year. The skill picks mileage bars, intensity distribution, recovery trends, single-run splits, and platform comparisons based on available data, using ECharts, Plotly, or whatever tools the host provides. The built-in SVG is only a basic fallback; richer charts depend on the runtime environment.
- Give short, evidence-based suggestions from existing plans, training load, and recovery data, and state limitations when data is missing.
- Guide you through periodic reports and training reminders on request; actual scheduling, delivery, and notifications depend on your platform's capabilities and permissions.

### Before you start

This project is a skill for the analysis workflow and reporting; data comes from two independent MCPs:

| Source | Project | Purpose |
| --- | --- | --- |
| Garmin | [garmin-mcp](https://github.com/hongshunanhai/garmin-mcp) | Training, sleep, recovery data |
| RQrun | [rqrun-mcp](https://github.com/hongshunanhai/rqrun-mcp) | Workout records, running level, analysis |

On first use the skill checks available tools and guides you through installing or connecting missing data sources. Connecting just one is fine; logins, permissions, and data availability are independent per source. Read each project's install notes and license first: Garmin MCP uses a non-commercial license independent of this project.

### Install & first run

**Codex (local)**

1. Download this repo and copy the full `plugins/running-coach/skills/running-coach` directory to the user-level skill directory `~/.agents/skills/running-coach`, or a project-level `.agents/skills/running-coach`. Keep `references`, `scripts`, and `examples` inside.
2. Start a new session and type: "Use running-coach to connect Garmin and RQrun and generate this week's running report."
3. Follow the prompts to check or install the two MCPs, complete login, then review the data sources and reporting period in your first report. Existing MCPs do not need reinstalling.

**ChatGPT**

The repo includes a ChatGPT desktop plugin and marketplace for local testing. These are installation paths pending end-to-end verification, not verified one-click installs:

1. Download or clone this repo and run `codex plugin marketplace add .` in the repo root to add the local marketplace to Codex.
2. Restart the ChatGPT desktop app, pick the "跑步教练" source in Work's plugin directory, find Running Coach, and install it. Start a local Work session and run the plugin setup or select the skill.
3. Follow the guide to connect Garmin and RQrun, verify both can read activities in a new conversation, then generate your first weekly report.

This path requires the Codex CLI locally and may be affected by account, version, and workspace permissions. Installing the skill does not install or log in the two MCPs; Codex local MCP config is not the same as a ChatGPT plugin connection. Garmin supports HTTP and RQrun uses local stdio. See the [setup guide](plugins/running-coach/skills/running-coach/references/setup.md) and the [OpenAI plugin packaging docs](https://developers.openai.com/plugins/build/plugins).

### Try saying

```text
Use my Garmin and RQrun data to make last week's running report, chart-first.
Compare yesterday's run on both platforms (distance and pace) and explain any differences.
Given my recent training and recovery, what should I do tomorrow?
If this platform supports scheduled jobs, send me last week's report every Monday at 8 AM, Asia/Shanghai.
```

Run one manual report before setting up a schedule. When runs depend on local files, scheduling depends on the host; reports may be incomplete when logins expire or a device has not synced.

### Render the sample chart locally

Requires Python 3, no extra plotting libraries:

```bash
python3 plugins/running-coach/skills/running-coach/scripts/render_report.py plugins/running-coach/skills/running-coach/examples/sample.json report.svg
```

`sample.json` and the sample image are simulated data. Real reports require reading and verifying user data first, then filling in the sample structure; the template does not connect to accounts automatically. Do not commit sensitive data to GitHub.

### Privacy & boundaries

Enter passwords only on each platform's official login page; never paste passwords, verification codes, cookies, or tokens into chat. Data is processed by the AI client and model you choose; review report content before sharing. Training suggestions are not medical diagnosis; when unwell or injured, rest first and seek professional help.

### Feedback & verification

When filing issues, describe your platform, steps, and error messages, and remove accounts, GPS traces, health data, and credentials first. Verification steps and pre-release checks are in [CONTRIBUTING.md](CONTRIBUTING.md).

This project is licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE): personal non-commercial use must follow the license terms; for other uses contact the copyright holder first. The full terms govern permitted uses. The two MCPs are licensed separately.
