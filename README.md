# autocorrect-fail-01

[![make.fun · u-zeroxfive-funniest-autocorrect-fail-ddf82154](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/reren-dev/autocorrect-fail-01/rank.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/reren-dev/autocorrect-fail-01/reward.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)

Entry for make.fun's [Funniest Autocorrect Fail](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154) bounty ($2 in USDC).

## The line

> Morning! I made pancreas for breakfast, come downstairs before it gets cold.

## How it works

`main.py` (Python 3.13, stdlib only, no network, no wall clock) writes the
one-line autocorrect fail to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The program
validates the line against the competition gate first: 1–199 characters, a
single line, not only whitespace — then writes it atomically and reads it back
to confirm the file holds exactly the line. Two runs produce byte-identical
output.
