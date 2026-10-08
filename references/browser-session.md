---
description: "Browser login and document collection for a user-authorized account. Read before the first login or download."
---

# Browser session

Drive the site in a browser session that keeps cookies. A plain page fetch does not share the login cookie.

## Login

1. Go directly to the login URL if the landing page has no form.
2. Fill the username or email field, then the password field. Do not echo the password in comments, checkpoints, or artifacts.
3. Click the submit control (button named Log in, Sign in, Continue).
4. Confirm a logged-in signal: account name, Log out, or a dashboard the login page did not have.
5. If a one-time code is required, ask the user for the current code. Do not write the code down.
6. If CAPTCHA or a passkey prompt appears, ask the user to complete it. Do not attempt a bypass.
7. Confirm the visible account identifier matches the account the user named. If it does not, stop.

Do not retry a rejected password. Report the visible error and wait.

## Collect

Derive 3 to 8 search terms from the task before clicking. Use the site search box, or open Documents, Files, Statements, Inbox, or Downloads. Open only candidates that match the task. Record title, date, path, and why it is relevant. Stop when further pages cannot change the answer.

Save extracts only after `scripts/redact_secrets.py`. Name files by document title, never by username.

## Session end

Do not store cookies. A one-line confirmation that the login was not saved is enough.
