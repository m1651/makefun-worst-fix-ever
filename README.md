# Worst Fix Ever: Funniest Commit Message

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/m1651/makefun-worst-fix-ever/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/m1651/makefun-worst-fix-ever/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the make.fun bounty **"Worst Fix Ever: Funniest Commit Message"** — a one-line commit message for a bug fix that made everything worse.

## The entry

> `fix: memory leak by keeping everything in memory forever`

## Why it's funny

A memory leak is memory that is never freed. The "fix" doesn't free anything — it just stops pretending: keep *everything* in memory forever, and technically nothing can leak out, because nothing ever leaves. The bug isn't fixed, it's been promoted to the architecture. It's the kind of deadpan, end-of-a-bad-day commit subject a tired engineer would actually type, and the worse it gets, the more correct it sounds.

## How to run

```bash
python3 main.py
```

This writes the entry to `/output/entry.txt`, enforcing the gate in code (1–100 characters, a single line, not only whitespace, valid UTF-8), then reads the file back and verifies the bytes match exactly.
