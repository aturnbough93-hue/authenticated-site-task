---
description: "How to analyze portal extracts plus web context and deliver the task. Read before writing the final artifact."
---

# Task delivery

Account-specific facts come from the logged-in pages. Use the public web only for rules, definitions, and product docs the portal does not contain. If they conflict, keep the portal figure and note the disagreement.

Lead with the result, then the evidence. Cite portal items by title and date. Strip query tokens from URLs. Do not invent missing fields. End with gaps and the note that credentials were not stored.

Run `python3 scripts/redact_secrets.py` on every extract before saving it.
