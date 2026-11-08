# 参与和验证

欢迎提出问题、修正文档或提交改进。提交前请移除账号、Cookie、访问令牌、位置轨迹和真实健康数据；示例与自动测试只使用虚构数据。

## 本地检查

在仓库根目录运行：

```bash
python3 plugins/running-coach/skills/running-coach/examples/test_render.py
python3 plugins/running-coach/skills/running-coach/scripts/render_report.py plugins/running-coach/skills/running-coach/examples/sample.json /tmp/running-coach-sample.svg
```

Skill 结构可以用 OpenAI skill-creator 中的 `quick_validate.py` 校验；该工具需要 PyYAML。检查示例图的视觉布局及中文显示，并分别验证空记录、缺失数据、零跑量和同步延迟。

## 发布前人工验证

- 在干净环境中验证 Skill 安装、首次引导、已安装 MCP 的识别和登录过期恢复。
- 在目标 ChatGPT 环境中连接两个 MCP，验证真实记录、同一次活动去重与来源标注；检查只连接一个数据源时的报告。
- 对照真实数据核对报告数字、时区、缺失项和手机端图表可读性。
- 在用户明确指定时间后验证定时任务创建、运行、通知和失败提示；记录实际支持的账号、平台及限制。
- 检查独立依赖的许可证及第三方素材；删除测试中产生的个人数据。外部贡献涉及商业再授权时，应先明确贡献者授权。
- 只有上述首测完成后，才在介绍素材和发布说明中声称相应功能已验证。

开发预览不保证所有宿主具有相同的 MCP、定时或图表能力。请在问题中说明实际运行环境及复现步骤。
