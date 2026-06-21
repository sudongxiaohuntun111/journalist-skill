# 记者技能（Journalist Skill）

> 像一个真正的记者一样，通过专业采访帮你理清思路、挖掘深度、输出优质文章。

**开源项目 · 遵循 Agent Skills 标准 · 跨平台兼容**

---

## 这是什么？

`journalist-skill` 是一个 AI Agent 技能（Skill），它模拟专业记者的工作方式：

1. **采访你**——不会让你直接说"写什么"，而是记者主动提问，层层递进
2. **挖掘深度**——有经验的记者知道什么时候追问、什么时候收网
3. **判断体裁**——根据你的内容，自动判断最适合写成什么（评论、随笔、口播稿……）
4. **输出成文**——最终输出一篇有专业水准的文章

## 适用场景

- 有感悟、想法、观察，想落成文字但不知道从何下笔
- 脑子里一团乱麻，需要有人帮你理清
- 想写点东西，但不确定写成什么形式合适
- 写完后想有专业级的编辑反馈

## 快速开始

### Hermes Agent

```bash
cp -r journalist-skill ~/.hermes/skills/journalist
```

### Claude Code

```bash
cp -r journalist-skill ~/.claude/skills/journalist
# 或放在项目级别
mkdir -p .claude/skills/
cp -r journalist-skill .claude/skills/journalist
```

### Codex CLI

```bash
cp -r journalist-skill ~/.codex/skills/journalist
```

### OpenClaw

```bash
openclaw skills install ./journalist-skill
```

## 使用方式

加载技能后，直接对 AI 说：

> "我想写点东西"
> "帮我理一下这个想法"
> "今天有件事想写下来"

记者就会开始采访你。

## 项目结构

```
journalist-skill/
├── SKILL.md                 # 核心指令（Agent Skills 标准格式）
├── references/
│   ├── interview-flow.md    # 采访状态机详解
│   └── writing-templates.md # 各体裁写作模板
├── examples/
│   ├── full-interview.md    # 完整采访示例
│   └── output-article.md    # 示例输出文章
├── scripts/
│   └── search_helper.py     # 采访辅助搜索脚本
├── evals/
│   └── test-prompts.json    # 测试场景
├── CONTRIBUTING.md          # 贡献指南
├── LICENSE                  # MIT 许可证
└── README.md
```

## 许可证

本项目采用 MIT 许可证。
