# World news in one image — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/katherinecoco02-dotcom/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/katherinecoco02-dotcom/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for [make.fun](https://make.fun/bounty/news-image-20261121) bounty `news-image-20261121`:
sum up 21 November 2026's world news in one image.

## The image

A newspaper front page, 1024×1024, with the date at the top and six
stories from that day:

1. **Tankers hit, Strait of Hormuz** — Two tankers struck by unknown
   projectiles near Khasab, Oman; no casualties reported.
2. **Markets fall, New York** — S&P 500 enters correction as the AI
   sell-off spreads; Nasdaq falls 5.3%, Nikkei 5.1%, Nvidia 14%.
3. **UK–EU reset, Brussels** — Three post-Brexit deals signed: food
   trade, carbon markets, and youth mobility for 100,000 a year.
4. **Cyberattacks, Washington** — FBI probes a breach of the national
   crime database; hackers also hit the USDA farmer-payment system.
5. **COP31 stalls, Antalya** — Climate talks run past their deadline
   with no deal; the draft drops the fossil-fuel phase-out language.
6. **Cancer hope, Barcelona** — A daily pill plus chemotherapy makes
   pancreatic tumours vanish in 1 in 12 patients in an early trial.

## How it is built

- `draw.py` draws `entry.png` with Pillow (local build tool only).
- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, so both runs write identical bytes.

Test locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
