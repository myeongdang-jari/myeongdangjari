#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""릴스 영상 연결 복구 도구 — 자동 갱신이 index.html을 덮어쓴 뒤 다시 붙일 때 쓴다.

    python3 tools/attach_reels.py

v/ 안의 릴스 파일 이름과 상품 id 대응은 REELS 아래에 있다.
index.html 안의 상품 JSON(#d)에 video 키를 넣고 tools/build_bridge.py로 페이지를 다시 만든다.
"""
import json
import re
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

REELS = {
    "bm-heattech-marunfive": "v/reel-heattech-marunfive-c2dcd0b7.mp4",
    "bm-winter-slipper-balcance": "v/reel-winter-slipper-327a151e.mp4",
    "bm-mop-sheet-cheongso": "v/reel-mop-sheet-5ca66f7a.mp4",
    "bm-thermal-pot": "v/reel-thermal-pot-06e7fa93.mp4",
    "bm-veg-spinner": "v/reel-veg-spinner-39df3879.mp4",
    "bm-silicone-container-s": "v/reel-silicone-container-8d489287.mp4",
    "bm-bathroom-shelf-set": "v/reel-bathroom-shelf-6edfe957.mp4",
}


def main():
    src = INDEX.read_text(encoding="utf-8")
    m = re.search(r'\n<script type="application/json" id="d">(\[.*?)</script>', src, re.S)
    if not m:
        raise SystemExit("index.html 안에서 상품 JSON(#d)을 찾지 못했습니다.")
    data = json.loads(m.group(1))
    hit = 0
    for item in data:
        video = REELS.get(item["id"])
        if not video:
            continue
        if not (ROOT / video).exists():
            print(f"파일 없음: {video}")
            continue
        item["video"] = video
        hit += 1
    src = src[:m.start(1)] + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + src[m.end(1):]
    INDEX.write_text(src, encoding="utf-8")
    print(f"video 키 {hit}건 반영")
    subprocess.run(["python3", str(ROOT / "tools" / "build_bridge.py")], check=True)


if __name__ == "__main__":
    main()
