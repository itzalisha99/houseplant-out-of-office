# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/itzalisha99/houseplant-out-of-office/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/itzalisha99/houseplant-out-of-office/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

A make.fun entry for **The Houseplant Out-of-Office**: the funniest
out-of-office auto-reply a houseplant would send, 120 characters or fewer.

## The reply

> Out of office: I am a dead fern. My owner waters the plastic plant next to me.

The joke is the plant's own life driving it: a real fern, dead from neglect,
while its owner faithfully waters the plastic plant sitting right beside it.

## How it works

`main.py` (Python stdlib only, deterministic) writes the reply to
`/output/entry.txt`. It validates the text against the bounty gate first:
1–120 characters, UTF-8, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
