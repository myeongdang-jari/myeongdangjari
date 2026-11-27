#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""명당 밤도깨비 시장 숏클립 렌더러 (네이버 쇼핑라이브 숏클립 레퍼런스 스타일)

    python3 tools/render_shortclip.py --id bm-medien-toothbrush
    # SPECS 아래에 상품을 추가하고 돌리면 v/<id>-night.mp4 와 img/reels/<id>-night.jpg 가 나온다.
    # 발행용 파일명은 v/<id>-<해시>.mp4 관례를 따르므로 렌더 뒤 이름을 바꿔 커밋한다.

    1080x1920 / 30fps / H.264 yuv420p / 7초 / 무료 (PIL + FFmpeg, 크레딧 0원)

구조(레퍼런스 `view.shoppinglive.naver.com/shortclips/11597200` 분석):
  상단  짧은 아이브로 + 굵은 상품 핵심 한 줄
  중앙  아치형 프레임 안 실제 상품 사진 + Ken Burns 줌/팬
  사진 아래 3단 POINT 01/02/03 배지
  최하단 화이트 카드 바  `09 · 국내 생산` 태그 + 상품명 2줄 + `AI활용` 배지

    python3 render_clip.py --id bm-pure-sunday-dishcloth --img .../pure-sunday-dishcloth.jpg \
        --eyebrow "09 · 국내 생산 · PURE SUNDAY" --title "빨아 쓰는 행주|넉넉하게 세 통" \
        --p1 "국내 제조|MADE IN KOREA" ... --out v/xxx.mp4
"""
import argparse
import math
import os
import pathlib
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
FPS = 30
SECS = 7.0
N = int(FPS * SECS)

# 폰트·ffmpeg 경로 — 이 저장소 밖에서 돌릴 때는 환경변수로 지정한다.
#   PRETENDARD_DIR=<Pretendard-*.otf 가 있는 폴더>  FFMPEG=<ffmpeg 실행 파일>
def _font_dir():
    for cand in (os.environ.get("PRETENDARD_DIR"),
                 "/workspace/work/coupas-reels/src/fonts",
                 str(pathlib.Path.home() / ".fonts/pretendard")):
        if cand and all((pathlib.Path(cand) / f"Pretendard-{w}.otf").exists()
                        for w in ("Regular", "Medium", "SemiBold", "Bold", "ExtraBold")):
            return pathlib.Path(cand)
    raise SystemExit("Pretendard 폰트를 찾지 못했습니다. PRETENDARD_DIR 환경변수로 폴더를 지정하세요 "
                     "(Pretendard-Regular/Medium/SemiBold/Bold/ExtraBold.otf).")


FONT_DIR = _font_dir()
FFMPEG = os.environ.get("FFMPEG") or "ffmpeg"

# 팔레트 — 밤도깨비 시장 톤(크림 종이 + 등불 금빛 + 먹색)
BG_TOP = (245, 240, 230)
BG_BOT = (233, 225, 210)
INK = (28, 25, 20)
INK_SOFT = (74, 67, 57)
GOLD = (150, 104, 46)
GOLD_LT = (231, 199, 154)
MUTED = (150, 140, 124)
WHITE = (255, 255, 255)

# 기하
ARCH_X0, ARCH_X1 = 118, 962          # 아치 프레임
ARCH_TOP = 408
ARCH_BOT = 1214
ARCH_R = (ARCH_X1 - ARCH_X0) // 2    # 반원
BORDER = 12
TITLE_TOP = 176
BAND_TOP = 968                        # POINT 띠 시작
CARD_X0, CARD_X1, CARD_TOP, CARD_BOT = 108, 972, 1300, 1592

_fc = {}


def F(weight, size):
    key = (weight, size)
    if key in _fc:
        return _fc[key]
    f = ImageFont.truetype(str(FONT_DIR / f"Pretendard-{weight}.otf"), size)
    _fc[key] = f
    return f


def spaced(draw, text, center_x, y, font, spacing, fill):
    w = sum(font.getlength(c) for c in text) + spacing * max(0, len(text) - 1)
    x = center_x - w / 2
    for c in text:
        draw.text((x, y), c, font=font, fill=fill, anchor="lm")
        x += font.getlength(c) + spacing
    return w


def ease_out(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def ease_in_out(x):
    x = max(0.0, min(1.0, x))
    return 3 * x * x - 2 * x * x * x


def cover(img, size, zoom=1.0, fx=0.5, fy=0.5):
    tw, th = size
    sw, sh = img.size
    s = max(tw / sw, th / sh) * zoom
    dw, dh = int(round(sw * s)), int(round(sh * s))
    big = img.resize((dw, dh), Image.LANCZOS)
    left = max(0, min(dw - tw, int(round((dw - tw) * fx))))
    top = max(0, min(dh - th, int(round((dh - th) * fy))))
    return big.crop((left, top, left + tw, top + th))


def paste_rgba(dst, layer, ox=0, oy=0):
    lw, lh = layer.size
    sx0, sy0 = max(0, -ox), max(0, -oy)
    dx0, dy0 = max(0, ox), max(0, oy)
    w = min(lw - sx0, dst.width - dx0)
    h = min(lh - sy0, dst.height - dy0)
    if w <= 0 or h <= 0:
        return
    dst.alpha_composite(layer.crop((sx0, sy0, sx0 + w, sy0 + h)), (dx0, dy0))


def arch_mask(w, h, r, ss=3):
    """윗변 반원 + 아래 직사각형 마스크."""
    m = Image.new("L", (w * ss, h * ss), 0)
    d = ImageDraw.Draw(m)
    d.pieslice((0, 0, 2 * r * ss, 2 * r * ss), 180, 360, fill=255)
    d.rectangle((0, r * ss, w * ss, h * ss), fill=255)
    return m.resize((w, h), Image.LANCZOS)


def arch_path_points(w, h, r, n=160):
    """아치 테두리 폴리곤(안쪽 선) — 마스크 외곽선 대신 벡터로 그린다."""
    pts = []
    cx = w / 2
    for i in range(n + 1):
        a = math.pi + math.pi * i / n
        pts.append((cx + r * math.cos(a), r + r * math.sin(a)))
    pts.append((w, h))
    pts.append((0, h))
    return pts


def stage(size, z=1.0, fx=0.5, fy=0.5, top=(238, 228, 208), bot=(214, 197, 167)):
    """아치 안 사진대 — 따뜻한 크림 그라데이션 + 옅은 비네트."""
    w, h = size
    col = np.zeros((h, 1, 3), dtype=np.float32)
    for y in range(h):
        t = y / max(1, h - 1)
        col[y, 0] = [top[i] + (bot[i] - top[i]) * t for i in range(3)]
    arr = np.repeat(col, w, axis=1)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx - w * fx) / (w * 0.85)) ** 2 + ((yy - h * 0.45) / (h * 0.9)) ** 2)
    arr *= np.clip(1.03 - 0.16 * d, 0.82, 1.04)[..., None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def tone(img):
    """사진을 아치 안에 앉힌다 — 따뜻한 톤 + 아치 모양 비네트(가장자리를 살짝 눌러 프레임이 읽히게).
    흰 배경 팩샷의 상품 면은 그대로 살린다(키아웃 없음).
    """
    a = np.asarray(img.convert("RGB")).astype(np.float32)
    h, w = a.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx - w * 0.5) / (w * 0.52)) ** 2 + ((yy - h * 0.56) / (h * 0.60)) ** 2)
    vig = np.clip(1.02 - 0.20 * np.clip(d - 0.35, 0, None) ** 1.6, 0.80, 1.02)
    warm = np.array([1.0, 0.972, 0.930], dtype=np.float32)
    out = a * warm * vig[..., None]
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def grain(size):
    import random
    random.seed(7)
    g = Image.new("L", (size[0] // 3, size[1] // 3))
    px = g.load()
    for y in range(g.height):
        for x in range(g.width):
            px[x, y] = 128 + random.randint(-6, 6)
    return g.resize(size, Image.BILINEAR)


def base_layers(spec, photo):
    """배경·아치·카드 등 정적 레이어."""
    """배경·아치·카드 등 정적 레이어."""
    bg = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / H
        col = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        d.line((0, y, W, y), fill=col)
    # 등불 번짐 (아주 옅게)
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-260, -300, 1340, 620), fill=(34, 24, 8))
    glow = glow.filter(ImageFilter.GaussianBlur(180))
    bg = Image.blend(bg, Image.new("RGB", (W, H), (250, 244, 232)), 0.0)
    bg = Image.composite(Image.new("RGB", (W, H), (252, 247, 238)), bg,
                         glow.convert("L").point(lambda v: min(255, v * 3)))
    # 종이 결
    gr = grain((W, H)).convert("L").point(lambda v: 128 + (v - 128) * 0.5)
    bg = Image.blend(bg, Image.merge("RGB", (gr, gr, gr)), 0.035)

    canvas = bg.convert("RGBA")

    # 아치 그림자 + 흰 테 + 사진
    aw, ah = ARCH_X1 - ARCH_X0, ARCH_BOT - ARCH_TOP
    shadow = Image.new("RGBA", (aw + 120, ah + 140), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse((60, 40 + ARCH_R, aw + 60, 40 + ARCH_R + 120), fill=(60, 45, 25, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(26))
    paste_rgba(canvas, shadow, ARCH_X0 - 60, ARCH_TOP - 40 + 8)

    white = Image.new("RGBA", (aw, ah), (0, 0, 0, 0))
    ImageDraw.Draw(white).polygon(arch_path_points(aw, ah, ARCH_R), fill=(255, 255, 255, 255))
    paste_rgba(canvas, white, ARCH_X0, ARCH_TOP)

    # 아치 테두리 한 줄 — 크림 종이 위에서 프레임이 또렷하게
    edge = Image.new("RGBA", (aw, ah), (0, 0, 0, 0))
    ImageDraw.Draw(edge).line(arch_path_points(aw - 1, ah - 1, ARCH_R - 1, 200) + [(aw - 1, ah - 1)],
                              fill=(206, 193, 170, 235), width=2, joint="curve")
    paste_rgba(canvas, edge, ARCH_X0, ARCH_TOP)

    inner_w, inner_h = aw - 2 * BORDER, ah - BORDER
    mask = arch_mask(inner_w, inner_h, ARCH_R - BORDER)
    return canvas, mask, (ARCH_X0 + BORDER, ARCH_TOP + BORDER), (inner_w, inner_h)


def draw_texts(canvas, spec, t):
    """아이브로·제목·카드 텍스트를 시간 t에 맞춰 합성."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx = W / 2

    # 아이브로
    a1 = ease_out((t - 0.05) / 0.55)
    if a1 > 0:
        eb = spec["eyebrow"]
        f = F("SemiBold", 27)
        tmp = Image.new("RGBA", (W, 60), (0, 0, 0, 0))
        spaced(ImageDraw.Draw(tmp), eb, cx, 30, f, 7.5, GOLD + (int(255 * a1),))
        paste_rgba(layer, tmp, 0, 118 + int(16 * (1 - a1)))

    # 제목 2줄
    a2 = ease_out((t - 0.18) / 0.7)
    if a2 > 0:
        fl = F("ExtraBold", 82)
        y = TITLE_TOP + int(26 * (1 - a2))
        for line in spec["title"]:
            tmp = Image.new("RGBA", (W, 120), (0, 0, 0, 0))
            dd = ImageDraw.Draw(tmp)
            dd.text((cx, 60), line, font=fl, fill=INK + (int(255 * a2),), anchor="mm")
            paste_rgba(layer, tmp, 0, y)
            y += 96

    # 하단 브랜드 라인
    a3 = ease_out((t - 2.2) / 0.8)
    if a3 > 0:
        tmp = Image.new("RGBA", (W, 60), (0, 0, 0, 0))
        spaced(ImageDraw.Draw(tmp), "명당 밤도깨비 시장 · 9화 국내 생산", cx, 30,
               F("SemiBold", 22), 5.0, MUTED + (int(220 * a3),))
        paste_rgba(layer, tmp, 0, 1720)
    canvas.alpha_composite(layer)


def draw_band(canvas, spec, t):
    """사진 아래 3단 POINT 띠."""
    aw = ARCH_X1 - ARCH_X0
    band_h = ARCH_BOT - BAND_TOP
    # 그라데이션 띠 (위쪽에서 빨리 어두워져 글자가 항상 읽히게)
    grad = Image.new("RGBA", (aw, band_h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(band_h):
        a = int(233 * min(1.0, (y / (band_h * 0.20)) ** 0.85))
        gd.line((0, y, aw, y), fill=(24, 20, 15, a))
    # 아치 모양으로 잘라 붙이기
    mask = arch_mask(aw, ARCH_BOT - ARCH_TOP, ARCH_R)
    band_full = Image.new("RGBA", (aw, ARCH_BOT - ARCH_TOP), (0, 0, 0, 0))
    paste_rgba(band_full, grad, 0, BAND_TOP - ARCH_TOP)
    band_full.putalpha(Image.composite(band_full.split()[3], Image.new("L", band_full.size, 0), mask))
    canvas.alpha_composite(band_full, (ARCH_X0, ARCH_TOP))

    # 구분선
    d = ImageDraw.Draw(canvas)
    for i in (1, 2):
        x = ARCH_X0 + aw * i / 3
        d.line((x, BAND_TOP + 34, x, ARCH_BOT - 34), fill=(255, 255, 255, 46), width=1)

    cols = [ARCH_X0 + aw * (i + 0.5) / 3 for i in range(3)]
    for i, (label, sub) in enumerate(spec["points"]):
        a = ease_out((t - (1.30 + 0.16 * i)) / 0.55)
        if a <= 0:
            continue
        tmp = Image.new("RGBA", (360, 200), (0, 0, 0, 0))
        td = ImageDraw.Draw(tmp)
        td.text((180, 24), f"POINT {i + 1:02d}", font=F("SemiBold", 23),
                fill=GOLD_LT + (int(240 * a),), anchor="mm")
        td.text((180, 74), label, font=F("Bold", 40), fill=(255, 255, 255, int(250 * a)), anchor="mm")
        spaced(td, sub, 180, 128, F("Medium", 18), 3.6, (230, 219, 201, int(215 * a)))
        paste_rgba(canvas, tmp, int(cols[i] - 180), BAND_TOP + 34 + int(14 * (1 - a)))


def draw_card(canvas, spec, t):
    a = ease_out((t - 1.95) / 0.75)
    if a <= 0:
        return
    off = int(46 * (1 - a))
    cw, ch = CARD_X1 - CARD_X0, CARD_BOT - CARD_TOP
    card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    sh = Image.new("RGBA", (cw + 80, ch + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((40, 46, cw + 40, ch + 60), radius=34,
                                         fill=(58, 44, 26, 80))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    paste_rgba(canvas, sh, CARD_X0 - 40, CARD_TOP - 40 + off)

    d = ImageDraw.Draw(card)
    d.rounded_rectangle((0, 0, cw - 1, ch - 1), radius=30, fill=(255, 255, 255, int(255 * a)))
    card.putalpha(card.split()[3])
    # 태그
    d.text((44, 46), spec["tag"], font=F("Bold", 26), fill=GOLD + (int(255 * a),), anchor="lm")
    # 상품명 2줄
    y = 92
    for line in spec["name"]:
        d.text((42, y), line, font=F("Bold", 47), fill=INK + (int(255 * a),), anchor="lm")
        y += 60
    # AI활용 배지
    bt = "AI활용"
    f = F("Medium", 21)
    bw = f.getlength(bt) + 30
    d.rounded_rectangle((cw - 46 - bw, ch - 76, cw - 46, ch - 28), radius=14,
                        fill=(238, 233, 224, int(235 * a)))
    d.text((cw - 46 - bw / 2, ch - 52), bt, font=f, fill=(120, 110, 95, int(250 * a)), anchor="mm")
    paste_rgba(canvas, card, CARD_X0, CARD_TOP + off)

    # 진행선 (카드 아래)
    pw = int((cw - 20) * min(1.0, t / SECS))
    if pw > 2:
        ImageDraw.Draw(canvas).rounded_rectangle(
            (CARD_X0 + 10, CARD_BOT + 18, CARD_X0 + 10 + pw, CARD_BOT + 21), radius=2,
            fill=GOLD + (170,))


def render(spec, photo_path, out_mp4, frames_dir):
    photo = Image.open(photo_path).convert("RGB")
    canvas0, mask, (px, py), (iw, ih) = base_layers(spec, photo)
    frames_dir.mkdir(parents=True, exist_ok=True)
    for n in range(N):
        t = n / FPS
        canvas = canvas0.copy()

        # 사진 Ken Burns — 천천히 줌인 + 좌우 미세 팬
        p = t / SECS
        z = 1.045 + 0.075 * ease_in_out(p)
        fx = 0.5 + 0.035 * math.sin(p * math.pi)
        fy = 0.5 - 0.02 * ease_in_out(p)
        ph = cover(photo, (iw, ih), zoom=z, fx=fx, fy=fy)
        ph = tone(ph).convert("RGBA")
        ph.putalpha(mask)
        # 아치 등장 (살짝 확대에서 정착)
        s = 0.972 + 0.028 * ease_out(t / 1.0)
        if s < 0.999:
            nw, nh = int(iw * s), int(ih * s)
            small = ph.resize((nw, nh), Image.LANCZOS)
            ox = px + (iw - nw) // 2
            oy = py + (ih - nh)
            canvas.alpha_composite(small, (ox, oy))
        else:
            canvas.alpha_composite(ph, (px, py))

        draw_band(canvas, spec, t)
        draw_texts(canvas, spec, t)
        draw_card(canvas, spec, t)

        canvas.convert("RGB").save(frames_dir / f"f{n:04d}.png")

    cmd = [FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-framerate", str(FPS),
           "-i", str(frames_dir / "f%04d.png"), "-c:v", "libx264", "-profile:v", "high",
           "-pix_fmt", "yuv420p", "-crf", "21", "-r", str(FPS),
           "-movflags", "+faststart", str(out_mp4)]
    subprocess.run(cmd, check=True)
    print(f"렌더 완료: {out_mp4}")


def render_cover(spec, photo_path, out_jpg, cw=480, ch=560):
    """릴스 띠 카드용 6:7 커버 — 같은 디자인을 작게."""
    photo = Image.open(photo_path).convert("RGB")
    bg = Image.new("RGB", (cw, ch), (245, 240, 230))
    d = ImageDraw.Draw(bg)
    for y in range(ch):
        t = y / ch
        col = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        d.line((0, y, cw, y), fill=col)
    canvas = bg.convert("RGBA")

    aw = cw - 60
    aw_x = 30
    r = aw // 2
    top = 132
    body = 240
    ah = r + body
    white = Image.new("RGBA", (aw, ah), (0, 0, 0, 0))
    ImageDraw.Draw(white).polygon(arch_path_points(aw, ah, r), fill=(255, 255, 255, 255))
    paste_rgba(canvas, white, aw_x, top)
    b = 7
    iw, ih = aw - 2 * b, ah - b
    ph = cover(photo, (iw, ih), zoom=1.06).convert("RGBA")
    ph.putalpha(arch_mask(iw, ih, r - b))
    canvas.alpha_composite(ph, (aw_x + b, top + b))

    d = ImageDraw.Draw(canvas)
    aw2 = aw
    # 태그
    spaced(d, spec["eyebrow_short"], cw / 2, 52, F("SemiBold", 16), 3.2, GOLD + (255,))
    # 제목
    fl = F("ExtraBold", 33)
    y = 86
    for line in spec["title"]:
        d.text((cw / 2, y), line, font=fl, fill=INK + (255,), anchor="mm")
        y += 38
    # 하단 이름 바
    d.rectangle((0, ch - 84, cw, ch), fill=(255, 255, 255, 255))
    d.text((22, ch - 56), spec["cover_name"], font=F("Bold", 22), fill=INK + (255,), anchor="lm")
    d.text((22, ch - 26), "09 · 국내 생산", font=F("SemiBold", 15), fill=GOLD + (255,), anchor="lm")
    canvas.convert("RGB").save(out_jpg, quality=90, optimize=True)
    print(f"커버 완료: {out_jpg}")


SPECS = {
    "bm-pure-sunday-dishcloth": {
        "photo": "img/products/pure-sunday-dishcloth.jpg",
        "eyebrow": "09 · 국내 생산 · PURE SUNDAY",
        "eyebrow_short": "09 · 국내 생산 · PURE SUNDAY",
        "title": ["빨아 쓰는 행주,", "넉넉하게 세 통"],
        "points": [("국내 제조", "MADE IN KOREA"), ("50개입 × 3통", "BULK 50"), ("빨아서 다시", "WASHABLE")],
        "tag": "09 · 국내 생산",
        "name": ["퓨어썬데이 국내제조", "빨아쓰는 데일리 행주 50개입"],
        "cover_name": "퓨어썬데이 데일리 행주 50개입",
    },
    "bm-medien-toothbrush": {
        "photo": "img/products/medien-toothbrush.jpg",
        "eyebrow": "09 · 국내 생산 · MEDIAN 365",
        "eyebrow_short": "09 · 국내 생산 · MEDIAN",
        "title": ["한 달에 하나씩,", "열두 자루"],
        "points": [("국내 제조", "MADE IN KOREA"), ("12개입", "12 MONTHS"), ("온 가족 기본모", "FAMILY")],
        "tag": "09 · 국내 생산",
        "name": ["메디안 국내 제조", "365DAYS 칫솔 12개입"],
        "cover_name": "메디안 365DAYS 칫솔 12개입",
    },
    "bm-sock-maker-49": {
        "photo": "img/products/sock-maker-49.jpg",
        "eyebrow": "09 · 국내 생산 · 49 YEARS",
        "eyebrow_short": "09 · 국내 생산 · 49 YEARS",
        "title": ["국산 무지 양말,", "열 켤레"],
        "points": [("국산", "MADE IN KOREA"), ("단목 + 중목", "TWO LENGTHS"), ("10켤레 세트", "10 PAIRS")],
        "tag": "09 · 국내 생산",
        "name": ["49년양말장인 국산", "무지 양말 10켤레 세트"],
        "cover_name": "49년양말장인 국산 양말 10켤레",
    },
    # 2026-11-27: 09장 「국내 생산」 남은 3종 — 장 전체를 릴스로 채움
    "bm-riond-microwave-set": {
        "photo": "img/products/riond-microwave-container.jpg",
        "eyebrow": "09 · 국내 생산 · RIOND",
        "eyebrow_short": "09 · 국내 생산 · RIOND",
        "title": ["전자레인지에 그대로,", "국내 생산 뚜껑 세트"],
        "points": [("국내 생산", "MADE IN KOREA"), ("BPA프리", "BPA FREE"), ("뚜껑 덮어 데우기", "MICROWAVE")],
        "tag": "09 · 국내 생산",
        "name": ["리온드 국내생산", "전자레인지 접시뚜껑세트"],
        "cover_name": "리온드 전자레인지 접시뚜껑세트",
    },
    "bm-hannune-pantry-box": {
        "photo": "img/products/hannune-pantry-box.jpg",
        "eyebrow": "09 · 국내 생산 · HANNUNE",
        "eyebrow_short": "09 · 국내 생산 · HANNUNE",
        "title": ["선반 한 칸,", "네 통으로 정리"],
        "points": [("국내 생산", "MADE IN KOREA"), ("4개 한 세트", "4 BOXES"), ("팬트리 정리", "PANTRY")],
        "tag": "09 · 국내 생산",
        "name": ["한누네 국내생산", "다용도 팬트리 정리함 4개"],
        "cover_name": "한누네 팬트리 정리함 4개",
    },
    "bm-prieel-pillow-cover": {
        "photo": "img/products/prieel-pillow-cover.jpg",
        "eyebrow": "09 · 국내 생산 · PRIEEL",
        "eyebrow_short": "09 · 국내 생산 · PRIEEL",
        "title": ["베갯잠은 자주,", "국내 생산 커버"],
        "points": [("국내 생산", "MADE IN KOREA"), ("피그먼트 코튼", "COTTON"), ("색 맞춰 여분", "SPARE")],
        "tag": "09 · 국내 생산",
        "name": ["쁘리엘르 국내생산", "코튼캔디 베개 커버"],
        "cover_name": "쁘리엘르 베개 커버",
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True, choices=list(SPECS))
    ap.add_argument("--root", default="/workspace/repo-myeongdangjari")
    ap.add_argument("--work", default="/workspace/work/nightmarket-clips")
    args = ap.parse_args()
    spec = SPECS[args.id]
    root = pathlib.Path(args.root)
    work = pathlib.Path(args.work)
    out_mp4 = root / "v" / f"{args.id}-night.mp4"
    cover = root / "img" / "reels" / f"{args.id}-night.jpg"
    render(spec, root / spec["photo"], out_mp4, work / f"frames-{args.id}")
    render_cover(spec, root / spec["photo"], cover)


if __name__ == "__main__":
    main()
