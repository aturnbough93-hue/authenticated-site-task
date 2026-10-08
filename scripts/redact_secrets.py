#!/usr/bin/env python3
"""Redact passwords, OTPs, and session tokens from a text file in place."""
import re, sys
from pathlib import Path
PATTERNS = [
    (re.compile(r"(?i)\b(password|passwd|pwd)\s*[:=]\s*\S+"), r"\1: [REDACTED]"),
    (re.compile(r"(?i)\b(otp|mfa|verification code|one-time code)\s*[:=]\s*\S+"), r"\1: [REDACTED]"),
    (re.compile(r"(?i)\b(session[_-]?id|access[_-]?token|refresh[_-]?token|auth[_-]?token)\s*[:=]\s*\S+"), r"\1: [REDACTED]"),
    (re.compile(r"(?i)(authorization:\s*bearer\s+)\S+"), r"\1[REDACTED]"),
    (re.compile(r"([?&](?:token|access_token|id_token|code)=)[^&\s]+"), r"\1[REDACTED]"),
]
def redact(text):
    for pattern, repl in PATTERNS:
        text = pattern.sub(repl, text)
    return text
def main(argv):
    if len(argv) < 2:
        print("usage: redact_secrets.py <file> [<file> ...]", file=sys.stderr)
        return 2
    for raw in argv[1:]:
        path = Path(raw)
        original = path.read_text(encoding="utf-8", errors="replace")
        cleaned = redact(original)
        path.write_text(cleaned, encoding="utf-8")
        print(f"{path}: {'changed' if cleaned != original else 'unchanged'}")
    return 0
if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
