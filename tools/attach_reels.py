#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""릴스 영상 연결 복구 도구 — 자동 갱신이 index.html을 덮어쓴 뒤 다시 붙일 때 쓴다.

    python3 tools/attach_reels.py

v/ 안의 릴스 파일 이름과 상품 id 대응은 REELS 아래에 있다.
index.html 안의 상품 JSON(#d)에 video 키를 넣고 tools/build_bridge.py로 페이지를 다시 만든다.
빌더가 video 상품을 히어로 아래 「릴스 띠」(#s-reels)로 모아 주므로, 이 스크립트를 돌리면
띠도 같이 다시 만들어진다. 띠 카드의 커버는 img/reels/{릴스 파일명}.jpg 이고,
커버가 없으면 빌더가 상품 사진으로 대신한다.
"""
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
COVER_DIR = ROOT / "img" / "reels"

REELS = {
    "bm-heattech-marunfive": "v/reel-heattech-marunfive-c2dcd0b7.mp4",
    "bm-winter-slipper-balcance": "v/reel-winter-slipper-327a151e.mp4",
    "bm-mop-sheet-cheongso": "v/reel-mop-sheet-5ca66f7a.mp4",
    "bm-thermal-pot": "v/reel-thermal-pot-06e7fa93.mp4",
    "bm-veg-spinner": "v/reel-veg-spinner-39df3879.mp4",
    "bm-silicone-container-s": "v/reel-silicone-container-8d489287.mp4",
    "bm-bathroom-shelf-set": "v/reel-bathroom-shelf-6edfe957.mp4",
    "bm-homstar-pink": "v/bm-homstar-pink_th-2e47dcff.mp4",
    "bm-home-sauna": "v/bm-home-sauna-bd3da7c2.mp4",
    "bm-weatherstrip": "v/bm-weatherstrip-f75e63a1.mp4",
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
        cover_stem = pathlib.Path(video).stem
        cover_stem = cover_stem[len("reel-"):] if cover_stem.startswith("reel-") else cover_stem
        cover = COVER_DIR / (cover_stem + ".jpg")
        if not cover.exists():
            print(f"커버 없음: {cover.relative_to(ROOT)} — 릴스 띠에서 상품 사진을 씁니다")
    src = src[:m.start(1)] + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + src[m.end(1):]
    INDEX.write_text(src, encoding="utf-8")
    print(f"video 키 {hit}건 반영")
    subprocess.run(["python3", str(ROOT / "tools" / "build_bridge.py")], check=True)

    # 빌드 결과에 릴스 띠가 그대로 들어갔는지 확인
    built = INDEX.read_text(encoding="utf-8")
    if 'id="s-reels"' not in built:
        raise SystemExit("빌드는 끝났지만 index.html에 릴스 띠(#s-reels)가 없습니다.")
    in_band = len(re.findall(r'<a class="rl" href="#p=', built))
    for pid in REELS:
        if f'href="#p={pid}"' not in built:
            raise SystemExit(f"릴스 띠에 {pid} 가 없습니다.")
    print(f"릴스 띠 확인 — 카드 {in_band}개, 영상 상품 {hit}건 모두 연결")


if __name__ == "__main__":
    main()
