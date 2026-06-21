# 贡献指南

感谢你关注记者.skill！欢迎任何形式的贡献。

## 开发流程

1. Fork 本仓库
2. 修改 `SKILL.md` 或 `references/` 下的文件
3. 运行测试：参考 `evals/test-prompts.json` 进行推演验证
4. 提交 PR

## 修改什么

| 文件 | 说明 |
|------|------|
| `SKILL.md` | 核心指令，修改后确保测试场景仍能通过 |
| `references/` | 采访状态机、写作模板等辅助文档 |
| `examples/` | 示例采访和输出文章，覆盖不同场景 |
| `evals/` | 测试场景定义 |

## 规范

- 使用简体中文
- 遵循 Agent Skills 标准（agentskills.io）
- 保持 MIT 许可证
