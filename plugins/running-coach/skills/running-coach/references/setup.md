# 首次接入与安装

先查看当前宿主已有工具。用户已安装时只验证连接和登录，不重装或覆盖配置。确认宿主、操作系统、可使用的工具后选择路径；两个仓库均为第三方项目，用户账号需由本人在各自官方登录页面操作。

## Codex 本机

已有本地仓库优先使用现有目录。安装脚本创建虚拟环境、安装依赖、可能打开浏览器登录并修改客户端配置，先说明将做什么，保留其他 MCP 配置；按宿主权限执行。没有仓库时从以下项目取得，选择用户可写目录：

- https://github.com/hongshunanhai/rqrun-mcp
- https://github.com/hongshunanhai/garmin-mcp

各自仓库执行 `./install.sh --client=codex`；也可参考仓库 `docs/codex.md` 手动配置。首次登录在项目登录窗口进行。分别用 `codex mcp get rqrun`、`codex mcp get garmin` 检查注册，再在新会话调用两个服务的 `list_activities` 验证读数；注册、握手、登录和实际数据读取是不同检查。若不需要立即登录，可使用 `--no-login`。不要输出或复制凭据。

## ChatGPT Work / 网页

先检查用户是否已经安装并可调用对应插件。Codex 的本地配置不会自动证明 ChatGPT 已连接。若缺失，先引导按两个仓库 README 安装并由用户完成本地登录，再分别连接 ChatGPT 支持的自定义 MCP 插件。网页接入使用可访问的 streamable HTTP / SSE 地址或受支持的安全隧道，并完成认证；OpenAI 文档说明安全隧道可转发 stdio 或 HTTP 服务，需检查用户账户和工作区是否支持。Garmin 项目提供 `--http`、`--readonly`；RQrun 当前项目提供 stdio。不要宣称本项目已验证隧道或桥接方案。分别在 ChatGPT 插件界面检查工具列表，选择插件后各调用 `list_activities` 验证。桌面本地插件是否可用取决于宿主及权限；以实际工具列表和调用为准。

参考 https://developers.openai.com/api/docs/guides/custom-mcp-server 、https://developers.openai.com/api/docs/guides/secure-mcp-tunnels 和 https://developers.openai.com/plugins/deploy/desktop-only 。不要引导将无鉴权健康数据服务暴露公网；不要将 session 文件、密码或 token 粘贴进聊天。

## 排障

连接失败时区分未注册、进程启动失败、登录过期、网络失败、无活动以及数据延迟。先返回能诊断的简短错误和下一步；后台运行不能交互登录时提示用户手动重新登录，不反复弹窗。修复后重新执行只读验证。
