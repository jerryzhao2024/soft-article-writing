# Soft Article Writing Skill

A Codex skill for writing and rewriting reader-first B2B and industrial soft articles.

## What it covers

- 公众号长文、公司资讯、技术解读、选型指南、项目复盘、标准解读
- Reader-first article planning
- Hook → Problem → Cause → Method → Proof → CTA structure
- PAS, AIDA, BAB, FAB, and 4U copywriting frameworks
- Evidence and compliance rules
- Anti-homogenization matrix for multi-article campaigns
- AI-flavor and quality review checklist

## Install

Copy the `soft-article-writing` folder into your Codex skills directory:

```text
~/.codex/skills/soft-article-writing/
```

On Windows:

```text
C:\Users\<user>\.codex\skills\soft-article-writing\
```

## Use

Ask Codex to use `soft-article-writing` when writing or rewriting a soft article, company news item, technical explainer, selection guide, project story, or advertorial.

Example:

```text
Use soft-article-writing to rewrite this article for an industrial equipment website. Keep the facts accurate and remove competitor comparisons.
```

## Validate

```bash
python scripts/soft_article_check.py <article-file>
```
