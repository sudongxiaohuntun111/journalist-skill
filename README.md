# 记者技能 (Journalist Skill)

> 像一个真正的记者一样，通过专业采访帮你理清思路、挖掘深度、输出优质文章。

**开源项目 · Agent Skills 标准 · 跨平台兼容 · 自进化**

---

## 这是什么？

`journalist-skill` 是一个 AI Agent Skill，它模拟专业记者的工作方式：

1. **采访你**——不是让你直接说"写什么"，而是记者主动提问，层层递进
2. **挖掘深度**——有经验的记者知道什么时候追问、什么时候收网
3. **判断体裁**——根据你的内容，自动判断最适合写成什么（评论、随笔、口播稿…）
4. **输出成文**——最终输出一篇有专业水准的文章
5. **自进化**——每次使用后自动复盘，让技能越用越好用

## 适用场景

- 有感悟/想法/观察，想落成文字但不知道从何下笔
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
# 或项目级别
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

加载 skill 后，直接说：

> "我想写点东西"
> "帮我理一下这个想法"
> "今天有件事想写下来"

记者就会开始采访你。

## 项目结构

```
journalist-skill/
├── SKILL.md                 # 核心指令（Agent Skills 标准格式）
├── references/
│   ├── interview-flow.md    # 采访状态机
│   ├── writing-templates.md # 各体裁写作模板
│   └── 新闻学研究笔记        # 专业根基
├── examples/
│   ├── full-interview.md    # 完整采访示例
│   └── output-article.md    # 示例输出
├── scripts/
│   └── setup.sh             # 一键安装脚本
├── record/                  # 自进化复盘记录（本地存储降级方案）
│   └── mechanism-c/         # 使用后复盘文件
├── LICENSE
└── README.md
```

## 自进化机制（v1.1.2+）

本 skill 内置自进化闭环，每次使用都在变强：

1. **使用前** — 加载历史复盘，避免重复踩坑
2. **使用中** — 捕捉用户的修正信号（表达、事实、偏好）
3. **使用后** — 复盘入库，沉淀经验
4. **周期性升级** — 累计复盘后系统性优化 skill

复盘支持两种存储方式：知识库（推荐）或本地文件，无知识库的用户也可正常使用。

## 版本历史

| 版本 | 说明 |
|------|------|
| v1.1.2 | 通用复盘存储方案，支持无知识库用户的本地降级 |
| v1.1.1 | 立意校准、节奏控制、伦理标注、偏好分层 |
| v1.1.0 | 自进化机制：使用前加载经验 → 使用中捕捉修正 → 使用后复盘入库 |
| v1.0.0 | 初始版本：采访状态机、写作工作流、搜索规则 |

## 许可证

MIT
