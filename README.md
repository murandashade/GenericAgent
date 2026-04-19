# GenericAgent

<div align="center">
<img src="assets/images/bar.jpg" width="880"/>

<a href="https://trendshift.io/repositories/25944" target="_blank"><img src="https://trendshift.io/api/badge/repositories/25944" alt="lsdefine%2FGenericAgent | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

<p align="center">
  <a href="#english">English</a> | <a href="#chinese">中文</a> | 📄 <a href="assets/GenericAgent_Technical_Report.pdf">Technical Report</a>
</p>

---
<a name="english"></a>
## 🌟 Overview

**GenericAgent** is a minimal, self-evolving autonomous agent framework. Its core is just **~3K lines of code**. Through **9 atomic tools + a ~100-line Agent Loop**, it grants any LLM system-level control over a local computer — covering browser, terminal, filesystem, keyboard/mouse input, screen vision, and mobile devices (ADB).

Its design philosophy: **don't preload skills — evolve them.**

Every time GenericAgent solves a new task, it automatically crystallizes the execution path into an skill for direct reuse later. The longer you use it, the more skills accumulate — forming a skill tree that belongs entirely to you, grown from 3K lines of seed code.

> **🤖 Self-Bootstrap Proof** — Everything in this repository, from installing Git and running `git init` to every commit message, was completed autonomously by GenericAgent. The author never opened a terminal once.

> **📝 Personal Note** — I'm using this fork primarily to experiment with Gemini models and to build up a personal skill tree for automating my development workflow. If you're trying this out, I recommend starting with small, well-defined tasks to let the skill tree grow organically.
>
> **My setup**: Gemini 1.5 Pro as the primary model, with tasks focused on file management and Git automation. Skill tree is stored in `~/agent_skills/` for easy backup.

## 📋 Core Features
- **Self-Evolving**: Automatically crystallizes each task into an skill. Capabilities grow with every use, forming your personal skill tree.
- **Minimal Architecture**: ~3K lines of core code. Agent Loop is ~100 lines. No complex dependencies, zero deployment overhead.
- **Strong Execution**: Injects into a real browser (preserving login sessions). 9 atomic tools take direct control of the system.
- **High Compatibility**: Supports Claude / Gemini / Kimi / MiniMax and other major models. Cross-platform.
- **Token Efficient**: <30K context window — a fraction of the 200K–1M other agents consume. Layered memory ensures the right knowledge is always in scope. Less noise, fewer hallucinations, higher success rate — at a fraction of the cost.


## 🧬 Self-Evolution Mechanism

This is what fundamentally distinguishes GenericAgent from every other agent framework.

```
[New Task] --> [Autonomous Exploration] (install deps, write scripts, debug & verify) -->
[Crystallize Execution Path into skill] --> [Write to Memory Layer] --> [Direct Recall on Next Similar Task]
```

| What you say | What the agent does the first time | Every time after |
|---|---|---|
| *"Read my WeChat messages"* | Install deps → reverse DB → write read script → save skill | **one-line invoke** |
