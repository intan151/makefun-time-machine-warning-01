# Funniest Time Machine Warning Label

[![Funniest Time Machine Warning Label](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/intan151/makefun-time-machine-warning-01/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/intan151/makefun-time-machine-warning-01/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

Entry for [Funniest Time Machine Warning Label](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
competition on [make.fun](https://make.fun).

## The entry

`main.py` (Python standard library only) writes one warning label for a
time machine, 88 characters, to `/output/entry.txt`:

> WARNING: Do not meet yourself. If you do, do not lend him money — he never pays it back.

A genuine-looking safety notice about the real hazard of meeting your
duplicate self — the straight face carries the joke, and the surprise
lands in the last few words.

## Run

```sh
python3 main.py
```

Deterministic: repeated runs produce byte-identical output.
The label is validated before writing (1–120 characters, one line, UTF-8),
and a self-check gate asserts the written file matches the entry exactly.
