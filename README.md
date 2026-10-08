# authenticated-site-task

Sign into a site the user names, collect the documents behind that login, and finish the task. Passwords stay in the session. They are never written to the skill, memory, or the reply.

Week 6 of IDS 104 is marked done in `references/run-book.md`. Later runs skip 6-1 and 6-2.

## Install

Grok, Claude Code, and Codex all read `SKILL.md`.

```bash
git clone https://github.com/aturnbough93-hue/authenticated-site-task.git
mkdir -p ~/.grok/skills
cp -a authenticated-site-task ~/.grok/skills/authenticated-site-task
```

Raw skill file:

https://raw.githubusercontent.com/aturnbough93-hue/authenticated-site-task/main/SKILL.md

## Layout

```
SKILL.md
references/browser-session.md
references/run-book.md
references/task-delivery.md
scripts/redact_secrets.py
evals/
```

No credentials are in this repo.
