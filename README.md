# world-news-24-nov-2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/havizrizkyansyahh/world-news-24-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/havizrizkyansyahh/world-news-24-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One front page that sums up the world's news of Tuesday 24 November 2026: 38 stories from 7 regions, each checked against reports dated that day, with original vector drawings, a map of where it happened and a date check of the stories left out as other days' news.

`main.py` copies `entry.png` to `/output/entry.png`. The image is rendered by `src/build.py` (HTML + SVG in headless Chrome, downsampled to 1024×1024) from the story list in `src/stories.py` and the drawings in `src/art.py`. The map uses Natural Earth's public-domain 1:110m land outlines.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6baap856&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
