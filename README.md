[![One-Line Laugh-Off](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/toirant/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/toirant/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)

# One-Line Laugh-Off

Entry for the [One-Line Laugh-Off](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae) bounty on make.fun — exactly one funny line, no setup notes, judged head-to-head by an AI comedy judge.

## The line

> I taught my dog to fetch my slippers, and now he brings me the neighbor's divorce papers every morning.

## How it works

`main.py` writes that single line to `/output/entry.txt` (103 characters, one line, well inside the 1–200 character gate), then reads it back and verifies the gate holds before exiting.

Run it locally:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
cat /tmp/entry.txt
```
