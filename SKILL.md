---
name: authenticated-site-task
description: "Log into a site the user names with credentials they give in this session, collect the documents that matter for the task, analyze them with web context, and finish the task. Use when the user asks to sign into a portal, pull files from behind a login, or complete work using materials only available after authentication. Not for password resets, credential storage, or access to accounts the user did not authorize."
type: workflow
lifecycle: active
user-invocable: true
metadata:
  author: Andrew Turnbough
  short-description: "Sign in, pull the documents, finish the task. Skip completed weeks."
---

# Authenticated Site Task — Login, collect, analyze, finish

Use this when the user names a site, supplies an account for that site, and wants a task done from documents behind the login. Credentials are session-only. Never write them into the skill, memory, artifacts, logs, or the reply.

## Hard rules

- Accept the site URL, username, and password only from the user in this conversation. Do not invent, reuse, or look up credentials.
- Touch only the account the user explicitly authorized. Stop if the session lands in a different account.
- Never persist passwords, OTPs, session cookies, or tokens. Do not put them in memory, files, commit messages, or the final answer.
- Do not bypass CAPTCHA, MFA, rate limits, or access controls. If a challenge appears, ask the user for the current code or to complete it, then continue.
- On a failed login, stop and report the visible error. Do not retry with guessed passwords.
- Before saving any page text, run `scripts/redact_secrets.py` on it.
- Prefer an official export or API the user already has access to over clicking through the UI.

## Workflow

1. Lock the task. Restate site, goal, and done-condition in one line. If the site URL or the goal is missing, ask once. If credentials are missing, ask once for username and password.
2. Open a fresh browser session. Do not use a fetch that does not share cookies. See `references/browser-session.md`.
3. Log in. Fill the visible form, submit, confirm a logged-in signal. Handle MFA by asking the user. Confirm the account matches the one they named.
4. Collect. Read `references/run-book.md` first. Skip every row marked done. Do not redo that week.
5. Supplement with the public web only for facts the portal does not contain. Account-specific facts come from the portal.
6. Do the task. Do not stop at a document list unless that was the ask.
7. Deliver and scrub. Delete any working file that still contains a credential. Tell the user the session was not saved.

Read `references/browser-session.md` before the first login. Read `references/run-book.md` before collecting course work. Read `references/task-delivery.md` before writing the final artifact.
