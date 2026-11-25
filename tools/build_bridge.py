#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""쿠팡 브릿지 index.html 빌더 (에디토리얼 셀렉트숍 리디자인 v2)

상품 데이터는 index.html 안의 <script type="application/json" id="d"> 배열 하나가 원본이다.
상품을 추가·수정한 뒤 이 스크립트를 실행하면 카드·번호·태그·검색색인이 모두 그 데이터로
다시 만들어진다. 카드 마크업을 손으로 고치지 말고 이 파일을 고친다.

    python3 tools/build_bridge.py

v2 변경점
- 히어로를 짧게 압축(텍스트 + 사진 1장)해 첫 화면에서 검색·주제 칩·첫 상품이 보이게 함
- 상품 카드를 흰 배경·1px 보더·12px 라운딩·hover elevation + 하단 다크 그린 CTA 버튼으로 재구성
- 탐색 바를 불투명 아이보리 + blur로 정돈(뒤 카드 글자 비침 제거)
- ■ 문자 로고를 창틀 모티프 SVG 심볼로 교체, 차례는 컴팩트 인덱스 바(점프 칩)로 축약
- 상세 모달의 여백·버튼 대비 상향
"""
import hashlib
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

FTC = "이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다."

# 장(章) 메타데이터. 순서가 화면 순서다.
SECTIONS = [
    {
        "slug": "window",
        "no": "01",
        "label": "단열·방한",
        "eyebrow": "1화 · 월요일 아침",
        "title": "커튼이 혼자 흔들렸다",
        "diary": "아침에 애들 방 문을 열었는데 커튼이 혼자 흔들리고 있었어. 창문은 분명히 닫혀 있었는데. "
                 "손을 대 보니 창틀 틈으로 찬 바람이 솔솔 들어와. 보일러를 더 올리기 전에 틈부터 막기로 하고, "
                 "창틀이랑 현관에 붙일 것들을 찾아 뒀어.",
    },
    {
        "slug": "street",
        "no": "02",
        "label": "차량·외출",
        "eyebrow": "2화 · 화요일 등원길",
        "title": "장갑을 껴도 손끝이 시리다",
        "diary": "애들 등원시키고 돌아오면 손이 꽁꽁 얼어 있어. 차 앞유리에는 성에가 하얗게 앉았고, 시동을 걸면 "
                 "안쪽에는 김이 서려. 아침마다 조금씩 늦는 이유가 이거였어. 주머니랑 차에 하나씩 넣어 둘 "
                 "것들을 찾아 뒀어.",
    },
    {
        "slug": "bed",
        "no": "03",
        "label": "난방·이불",
        "eyebrow": "3화 · 수요일 밤",
        "title": "보일러 틀까 말까",
        "diary": "보일러 틀까 말까로 남편이랑 또 실랑이했어. 가스비 고지서가 무서운 건 둘 다 똑같거든. "
                 "그래서 방 전체 말고 이불 속이랑 앉은 자리부터 데우기로 했어. 난방을 켜면 공기가 마르니까 "
                 "가습기도 같이 봐 뒀어.",
    },
    {
        "slug": "soup",
        "no": "04",
        "label": "간식·어묵",
        "eyebrow": "4화 · 목요일 저녁",
        "title": "결국 오늘도 어묵탕",
        "diary": "추운 날 저녁 메뉴가 고민되면 결국 어묵탕이야. 애들도 국물을 좋아해서 냄비가 금방 비어. "
                 "밥 먹고 나면 꼭 간식을 찾으니까, 냉동실에 넣어 둘 호빵이랑 붕어빵도 같이 찾아 뒀어.",
    },
    {
        "slug": "xmas",
        "no": "05",
        "label": "크리스마스",
        "eyebrow": "5화 · 금요일 오후",
        "title": "엄마, 크리스마스 언제 와?",
        "diary": "애들이 크리스마스 언제 오냐고 매일 물어봐. 거실에 큰 트리를 놓으면 둘째가 장식을 다 뜯어 놓을 "
                 "게 뻔해. 그래서 올해는 책상 위에 올려 두는 작은 것들로 찾아 뒀어.",
    },
    {
        "slug": "chores",
        "no": "06",
        "label": "욕실·살림",
        "eyebrow": "6화 · 토요일 낮",
        "title": "미뤄 둔 살림이 한꺼번에",
        "diary": "추우니까 설거지도 욕실 청소도 자꾸 미루게 돼. 주말에 몰아서 하려고 보니 줄눈에 곰팡이가 "
                 "올라와 있었어. 손이 덜 가게 거들어 줄 살림 물건들을 찾아 뒀어.",
    },
    {
        "slug": "wow",
        "no": "07",
        "label": "남편 위시",
        "eyebrow": "7화 · 일요일 밤",
        "title": "남편의 장바구니",
        "diary": "애들을 재우고 나니 남편이 휴대폰을 내밀어. 캠핑 갈 때 쓴다는 팬히터, 가방에 들어간다는 드론, "
                 "거실 벽을 화면으로 쓴다는 프로젝터. 살 건 아니라는데 눈은 진심이야. 구경은 같이 했어.",
    },
    {
        "slug": "resilience",
        "no": "08",
        "label": "재난·비상",
        "eyebrow": "8화 · 비상 대비",
        "title": "뉴스가 무서운 밤에",
        "diary": "애들을 재우고 뉴스를 보다가 남편이 『우리도 뭐라도 사 둘까』 하더라. 큰일이야 있겠냐고 웃으면서도, "
                 "정전되면 집이 깜깜해지고 물이 끊기면 애들 씻길 것도 없으니까. 그날 밤에 조용히 찾아본 것들이야. "
                 "사 두면 몇 해씩 그대로 있는 것들이라, 한 번 갖춰 두면 마음이 놓이는 쪽이야.",
    },
]

HERO_IMAGES = ["fleece-blanket.jpg", "music-box.jpg", "hoppang.jpg"]
IMG_BASE = "https://myeongdang-jari.github.io/myeongdangjari/img/products/"

# 창틀 네 칸 모티프 — 헤더·푸터 로고 심볼
MARK = ('<svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true">'
        '<rect x="2.1" y="2.1" width="15.8" height="15.8" rx="3" stroke="currentColor" stroke-width="1.4"/>'
        '<path d="M10 2.1v15.8M2.1 10h15.8" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>'
        '</svg>')

HEAD = """<!DOCTYPE html>
<html lang="ko">
<!-- 이 파일은 tools/build_bridge.py 가 만든다. 상품을 추가·수정할 때는 파일 아래쪽
     상품 데이터 배열(script id="d" 의 JSON)에 항목을 넣고 `python3 tools/build_bridge.py` 를
     실행한다. 카드·번호·태그·검색색인이 모두 그 데이터로 다시 만들어진다. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ogimg}">
<meta name="theme-color" content="#f6f5f0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500;700&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
:root{
  --paper:#f6f5f0; --paper-2:#fafaf6; --card:#fff; --img-bg:#fafaf8;
  --ink:#1c221e; --body:#3b423c; --sub:#71786f;
  --forest:#1b2e24; --forest-2:#2f4a39;
  --line:#e6e3da; --line-2:#d3cfc2;
  --serif:"Noto Serif KR","Nanum Myeongjo",AppleMyungjo,Batang,"Times New Roman",serif;
  --sans:Pretendard,-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  --w:1180px; --pad:clamp(16px,4.6vw,32px); --hh:56px;
  --ease:cubic-bezier(.2,.65,.25,1);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--paper);color:var(--body);font-family:var(--sans);line-height:1.65;
  -webkit-font-smoothing:antialiased;word-break:keep-all;overflow-wrap:anywhere}
a{color:inherit;text-decoration:none}
img{display:block;max-width:100%;height:auto}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
:focus-visible{outline:2px solid var(--forest);outline-offset:3px}
::selection{background:#dfe6dc;color:var(--ink)}
.sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:-9999px;top:0;z-index:99;background:var(--forest);color:#fff;padding:10px 16px;font-size:13px}
.skip:focus{left:8px;top:8px}

/* 상단 공정위 고지 */
.ftc{background:var(--forest);color:#e8e6da;font-size:10.5px;line-height:1.5;letter-spacing:.01em;
  text-align:center;padding:7px var(--pad);word-break:keep-all}

/* 헤더 */
.site{position:sticky;top:0;z-index:40;background:rgba(246,245,240,.94);
  backdrop-filter:saturate(150%) blur(14px);-webkit-backdrop-filter:saturate(150%) blur(14px);
  border-bottom:1px solid var(--line)}
.site .in{max-width:var(--w);margin:0 auto;padding:0 var(--pad);height:var(--hh);
  display:flex;align-items:center;gap:14px}
.brand{display:inline-flex;align-items:center;gap:9px;color:var(--ink);white-space:nowrap}
.brand .mk{display:inline-flex;align-items:center;justify-content:center;color:var(--forest);flex:none}
.brand .bt{font-family:var(--serif);font-size:18px;font-weight:700;letter-spacing:-.025em}
.site .right{margin-left:auto;display:flex;align-items:center;gap:14px;font-size:11px;
  color:var(--sub);letter-spacing:.05em;white-space:nowrap}
.site .right b{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.site .right .sep{width:1px;height:11px;background:var(--line-2);display:inline-block}
@media(max-width:600px){.site .right .vol{display:none}.brand .bt{font-size:16.5px}}

/* 히어로 (압축) */
.hero{max-width:var(--w);margin:0 auto;padding:clamp(16px,2.1vw,26px) var(--pad) 0}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.16fr) minmax(0,.84fr);
  gap:clamp(20px,3vw,40px);align-items:center}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:600;
  letter-spacing:.18em;color:var(--forest-2);text-transform:uppercase}
.eyebrow::before{content:"";width:16px;height:1px;background:var(--line-2);flex:none}
.hero h1{font-family:var(--serif);font-weight:700;font-size:clamp(25px,3.1vw,40px);line-height:1.18;
  letter-spacing:-.035em;color:var(--ink);margin-top:8px}
.stand{font-size:13.5px;line-height:1.72;color:var(--body);margin-top:9px;max-width:35em}
.hero-meta{display:flex;flex-wrap:wrap;align-items:center;gap:6px 12px;margin-top:11px;
  font-size:11.5px;color:var(--sub);letter-spacing:.03em}
.hero-meta b{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.hero-meta .d{width:3px;height:3px;background:var(--line-2);border-radius:50%}
.disc{font-size:10.5px;color:var(--sub);line-height:1.6;margin-top:8px;letter-spacing:.01em}
.hero-media{display:grid;grid-template-columns:1fr;gap:8px}
.hero-media figure{margin:0;min-width:0}
.hero-media img{width:100%;object-fit:cover;background:var(--img-bg);border:1px solid var(--line)}
.hero-media .hm-main img{aspect-ratio:16/9;max-height:208px;border-radius:12px}
.hero-media .hm-thumb{display:none}
.hero-media figcaption{grid-column:1/-1;font-size:10px;color:var(--sub);letter-spacing:.02em;margin-top:2px}
@media(max-width:860px){
  .hero-grid{grid-template-columns:1fr;gap:16px}
  .hero h1{margin-top:7px}
  .stand{font-size:13px;line-height:1.7;margin-top:8px}
  .hero-meta{margin-top:10px;font-size:11px}
  .disc{margin-top:6px}
  .hero-media{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
  .hero-media .hm-main{grid-column:auto;grid-row:auto;display:block}
  .hero-media .hm-thumb{display:block}
  .hero-media .hm-main img,.hero-media .hm-thumb img{aspect-ratio:1;border-radius:9px}
  .hero-media figcaption{display:none}
}
/* 폰에서는 히어로 사진을 접어 검색·카드가 첫 화면에 들어오게 한다 */
@media(max-width:640px){
  .hero{padding-top:14px}
  .hero-media{display:none}
  .hero-meta{display:none}
  .stand{font-size:12.8px;line-height:1.68}
  .chapter{padding-top:18px}
  .chead{gap:10px;margin-bottom:13px}
  .diary{display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
  .chapter + .chapter{padding-top:22px;margin-top:26px}
}

/* 차례 — 컴팩트 인덱스 바 */
.toc{max-width:var(--w);margin:clamp(14px,1.8vw,20px) auto 0;padding:0 var(--pad)}
.toc h2{position:absolute;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.toc ol{list-style:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0 clamp(12px,2vw,26px);
  border-top:1px solid var(--line)}
.toc a{display:flex;align-items:center;gap:9px;padding:6px 2px;border-bottom:1px solid var(--line);
  min-width:0;font-size:12.5px;transition:color .15s}
.toc a:hover .t{color:var(--forest);text-decoration:underline;text-underline-offset:3px}
.toc .n{font-family:var(--serif);font-size:11px;font-weight:500;letter-spacing:.08em;color:var(--forest-2);
  flex:none;font-variant-numeric:tabular-nums}
.toc .t{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  color:var(--ink);font-weight:500;letter-spacing:-.01em}
.toc .t em{display:none}
.toc .c{font-size:10.5px;color:var(--sub);flex:none;font-variant-numeric:tabular-nums}
@media(max-width:860px){
  .toc{margin-top:14px}
  .toc ol{display:flex;gap:6px;border-top:0;overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none;
    margin:0 calc(var(--pad) * -1);padding:0 var(--pad)}
  .toc ol::-webkit-scrollbar{display:none}
  .toc a{border:1px solid var(--line-2);border-radius:99px;padding:0 11px;height:30px;flex:none;gap:6px}
  .toc a:hover{border-color:var(--forest)}
  .toc .t{display:none}
  .toc .c{padding-left:5px;border-left:1px solid var(--line-2);line-height:1}
}

/* 탐색 바 — 스크롤 시 뒤 글자가 비치지 않게 종이색으로 불투명하게 깐다(blur는 보조) */
.tools{position:sticky;top:var(--hh);z-index:30;background:var(--paper);
  backdrop-filter:saturate(150%) blur(8px);-webkit-backdrop-filter:saturate(150%) blur(8px);
  border-bottom:1px solid var(--line);margin-top:clamp(12px,1.7vw,18px);
  box-shadow:0 14px 18px -20px rgba(28,34,30,.55)}
.tools .in{max-width:var(--w);margin:0 auto;padding:10px var(--pad) 9px;display:flex;flex-direction:column;gap:8px}
.searchrow{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.search{position:relative;flex:1;min-width:0;max-width:520px}
.search .ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--sub);pointer-events:none}
.search input{width:100%;height:40px;padding:0 44px 0 40px;background:#fff;color:var(--ink);
  border:1px solid var(--line-2);border-radius:10px;font:inherit;font-size:13.5px;letter-spacing:-.01em;
  appearance:none;-webkit-appearance:none;transition:border-color .15s,box-shadow .15s}
.search input::-webkit-search-cancel-button{display:none}
.search input::placeholder{color:#9aa096}
.search input:focus{outline:none;border-color:var(--forest);box-shadow:0 0 0 3px rgba(27,46,36,.09)}
.search .clr{position:absolute;right:8px;top:50%;transform:translateY(-50%);width:26px;height:26px;
  display:none;align-items:center;justify-content:center;border-radius:50%;color:var(--sub)}
.search .clr:hover{background:var(--paper);color:var(--ink)}
.search.has .clr{display:flex}
.rs{margin-left:auto;font-size:11.5px;color:var(--sub);letter-spacing:.03em;white-space:nowrap}
.rs b{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.chips{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none;
  margin:0 calc(var(--pad) * -1);padding:1px var(--pad) 2px}
.chips::-webkit-scrollbar{display:none}
.chip{flex:none;display:inline-flex;align-items:center;gap:5px;height:31px;padding:0 12px;
  border:1px solid var(--line-2);border-radius:99px;font-size:12px;color:var(--body);
  background:rgba(255,255,255,.5);white-space:nowrap;
  transition:background .15s,color .15s,border-color .15s}
.chip:hover{border-color:var(--forest);color:var(--ink);background:#fff}
.chip[aria-pressed=true]{background:var(--forest);border-color:var(--forest);color:#f1f0e6}
.chip .cn{font-size:10px;opacity:.6;font-variant-numeric:tabular-nums}
@media(max-width:640px){.searchrow{gap:8px}.search{max-width:none}.rs{font-size:11px;letter-spacing:0}}

/* 장 */
.chapters{max-width:var(--w);margin:0 auto;padding:0 var(--pad)}
.chapter{padding:clamp(20px,2.6vw,30px) 0 0;scroll-margin-top:calc(var(--hh) + 106px)}
.chapter[hidden]{display:none}
.chapter + .chapter{border-top:1px solid var(--line);margin-top:clamp(30px,4vw,48px);padding-top:clamp(26px,3.4vw,40px)}
.chead{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.84fr);
  gap:clamp(16px,3vw,44px);align-items:start;margin-bottom:clamp(14px,2vw,22px)}
.chline{display:flex;align-items:center;gap:10px}
.chn{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;flex:none;
  border:1px solid var(--line-2);border-radius:8px;font-family:var(--serif);font-size:13px;font-weight:500;
  letter-spacing:.02em;color:var(--forest-2);font-variant-numeric:tabular-nums}
.chlabel{font-size:10.5px;letter-spacing:.14em;color:var(--sub);font-weight:600}
.chead h2{font-family:var(--serif);font-weight:700;font-size:clamp(21px,2.5vw,31px);line-height:1.3;
  letter-spacing:-.028em;color:var(--ink);margin-top:10px}
.diary{font-family:var(--serif);font-size:14px;line-height:1.9;color:#414840;
  border-left:1px solid var(--line-2);padding-left:clamp(12px,1.8vw,18px)}
.chcount{display:inline-block;margin-top:9px;font-size:10.5px;letter-spacing:.1em;color:var(--sub);
  font-variant-numeric:tabular-nums}

/* 카드 그리드 */
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px 20px}
.card{display:flex;flex-direction:column;min-width:0;background:var(--card);
  border:1px solid var(--line);border-radius:12px;padding:8px;
  transition:box-shadow .22s var(--ease),transform .22s var(--ease),border-color .22s var(--ease)}
.card[hidden]{display:none!important}
.card:hover{transform:translateY(-2px);border-color:#d9d5c8;
  box-shadow:0 14px 28px -18px rgba(28,34,30,.34),0 2px 6px -3px rgba(28,34,30,.06)}
.card .ph{display:block;background:var(--img-bg);border-radius:9px;overflow:hidden;aspect-ratio:1}
.card .ph img{width:100%;height:100%;object-fit:cover;transition:transform .45s var(--ease)}
.card:hover .ph img{transform:scale(1.03)}
.cbody{display:flex;flex-direction:column;flex:1;padding:11px 4px 3px}
.card .meta{display:flex;align-items:center;gap:8px;font-size:10px;letter-spacing:.07em;color:var(--sub)}
.card .no{color:var(--forest-2);font-weight:700;letter-spacing:.1em;font-variant-numeric:tabular-nums;white-space:nowrap}
.card .tag{padding-left:8px;border-left:1px solid var(--line-2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.card .tag.reel{display:inline-flex;align-items:center;gap:4px;margin-left:2px;padding:2px 7px;border:0;
  border-radius:99px;background:var(--forest);color:#f1f0e6;font-weight:600;letter-spacing:.02em}
.card .tag.reel::before{content:"";width:0;height:0;border-left:4px solid currentColor;
  border-top:3px solid transparent;border-bottom:3px solid transparent}
.card .name{font-size:13.5px;font-weight:600;line-height:1.45;letter-spacing:-.015em;color:var(--ink);
  margin-top:7px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
  min-height:calc(2 * 1.45em)}
.card .name a:hover{text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--line-2)}
.card .why{font-size:12px;line-height:1.55;color:var(--sub);margin-top:4px;margin-bottom:11px;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card .buy{margin-top:auto;display:flex;align-items:center;justify-content:center;gap:7px;
  height:38px;border-radius:8px;background:var(--forest);color:#f2f0e6;
  font-size:12.5px;font-weight:600;letter-spacing:.01em;
  transition:background .18s,box-shadow .18s}
.card .buy:hover{background:var(--forest-2);box-shadow:0 8px 16px -10px rgba(27,46,36,.75)}
.card .buy .ar{font-size:10px;opacity:.7}
.card.flash .ph{box-shadow:0 0 0 2px var(--forest)}
@media(max-width:1024px){.grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:22px 18px}}
@media(max-width:860px){
  .grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 14px}
  .chead{grid-template-columns:1fr;gap:12px;align-items:start}
  .diary{font-size:13px;line-height:1.8}
  .chead h2{font-size:clamp(19px,4.6vw,24px);margin-top:9px}
  .chn{width:28px;height:28px;font-size:12px;border-radius:7px}
  .chcount{margin-top:7px}
}
@media(max-width:640px){
  .grid{gap:18px 12px}
  .card{padding:6px;border-radius:11px}
  .card .ph{border-radius:8px}
  .cbody{padding:9px 2px 1px}
  .card .name{font-size:12.8px;-webkit-line-clamp:3;min-height:calc(3 * 1.45em)}
  .card .why{font-size:11.5px;margin-bottom:9px}
  .card .buy{height:35px;font-size:11.5px;gap:5px;border-radius:7px}
}

/* 빈 결과 */
.empty{display:none;padding:64px 0 40px;text-align:center}
.empty.on{display:block}
.empty p{font-family:var(--serif);font-size:17px;color:var(--ink)}
.empty small{display:block;margin-top:8px;font-size:12.5px;color:var(--sub)}
.empty button{margin-top:18px;border:1px solid var(--forest);color:var(--forest);padding:10px 20px;
  border-radius:99px;font-size:12.5px}
.empty button:hover{background:var(--forest);color:#f2f0e6}

/* 푸터 */
.foot{background:var(--forest);color:#c3c9bd;margin-top:clamp(48px,6vw,76px);padding:clamp(34px,4.4vw,52px) var(--pad)}
.foot .in{max-width:var(--w);margin:0 auto;display:grid;grid-template-columns:minmax(0,1fr) auto;
  gap:20px 40px;align-items:end}
.foot .fb{display:inline-flex;align-items:center;gap:9px;font-family:var(--serif);font-size:20px;
  font-weight:700;letter-spacing:-.02em;color:#f2f1e6}
.foot .fb .mk{display:inline-flex;color:#8fa392}
.foot p{font-size:10.5px;line-height:1.85;color:#a9b2a4;margin-top:11px;max-width:56em}
.foot .sig{font-size:10px;letter-spacing:.14em;color:#86947f;text-align:right;line-height:1.9}
@media(max-width:700px){.foot .in{grid-template-columns:1fr}.foot .sig{text-align:left}}

/* 상세 */
.dv{position:fixed;inset:0;z-index:60;background:var(--paper);overflow-y:auto;
  -webkit-overflow-scrolling:touch;overscroll-behavior:contain}
.dv[hidden]{display:none!important}
.dvi{max-width:820px;margin:0 auto;min-height:100%;display:flex;flex-direction:column;padding:0 var(--pad)}
.dtop{position:sticky;top:0;z-index:3;display:flex;align-items:center;gap:12px;height:56px;
  margin:0 calc(var(--pad) * -1);padding:0 calc(var(--pad) - 6px);
  background:rgba(246,245,240,.96);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-bottom:1px solid var(--line)}
.dtop button{width:40px;height:40px;display:flex;align-items:center;justify-content:center;
  border-radius:50%;color:var(--ink);transition:background .15s}
.dtop button:hover{background:#ecebe2}
.dtop .lb{font-size:11px;letter-spacing:.08em;color:var(--sub);min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dtop .lb b{color:var(--ink);font-weight:600}
.dbody{padding:clamp(14px,2.4vw,22px) 0 86px;flex:1}
/* 릴스 플레이어 */
.reelbox{margin:0 0 14px;background:#0d0f0e;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.reelbox[hidden]{display:none}
.reelbox video{display:block;width:100%;max-height:min(62vh,560px);background:#0d0f0e}
.reelmeta{display:flex;align-items:center;justify-content:space-between;gap:10px;
  padding:8px 12px;font-size:11px;color:#c2c8bd;background:#141815}
.reelmeta b{font-weight:600;color:#f1f0e6;letter-spacing:.04em}
.reelmeta a{color:#eceade;border-bottom:1px solid rgba(241,240,230,.35);padding-bottom:1px}
.gal{display:flex;overflow-x:auto;gap:8px;scroll-snap-type:x mandatory;scrollbar-width:none;
  background:var(--img-bg);border:1px solid var(--line);border-radius:14px;
  justify-content:center;align-items:center;max-height:min(46vh,400px)}
.gal::-webkit-scrollbar{display:none}
.gal img{flex:none;width:auto;height:auto;max-width:100%;max-height:min(46vh,400px);
  object-fit:contain;scroll-snap-align:center;margin:0 auto}
.ds{display:inline-flex;align-items:center;gap:6px;margin-top:20px;padding:4px 10px;border-radius:99px;
  background:#eceae0;border:1px solid #dfdcd0;font-size:10.5px;letter-spacing:.1em;
  color:var(--forest);font-weight:600;transition:background .15s}
.ds:hover{background:#e4e2d6}
.dbody h1{font-family:var(--serif);font-weight:700;font-size:clamp(20px,2.8vw,28px);line-height:1.38;
  letter-spacing:-.025em;color:var(--ink);margin-top:12px}
.lead{font-size:14.5px;line-height:1.8;color:var(--body);margin-top:10px}
.reason{margin-top:24px;background:var(--paper-2);border:1px solid var(--line);border-radius:12px;
  padding:2px 16px 6px}
.reason h2,.dbody h2{font-size:10.5px;letter-spacing:.16em;color:var(--sub);font-weight:600;margin:16px 0 2px}
.dbody ul{list-style:none}
.dbody li{position:relative;padding:11px 0 11px 15px;font-size:13.5px;line-height:1.8;color:var(--body);
  border-bottom:1px solid var(--line)}
.dbody li:last-child{border-bottom:0}
.dbody li::before{content:"";position:absolute;left:1px;top:20px;width:4px;height:4px;border-radius:50%;
  background:var(--forest-2)}
.note{font-size:11px;line-height:1.8;color:var(--sub);margin-top:22px;padding:14px 16px;
  background:#f1efe7;border-radius:10px}
.rel{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px 12px;margin-top:10px}
.rc{min-width:0;display:block;background:#fff;border:1px solid var(--line);border-radius:10px;
  padding:6px;transition:box-shadow .2s var(--ease),transform .2s var(--ease)}
.rc:hover{transform:translateY(-2px);box-shadow:0 10px 20px -16px rgba(28,34,30,.4)}
.rc img{aspect-ratio:1;object-fit:cover;background:var(--img-bg);border-radius:7px}
.rc span{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
  font-size:11px;line-height:1.45;color:var(--body);margin-top:6px;padding:0 2px}
.rc:hover span{color:var(--forest)}
.morelink{display:inline-block;margin-top:16px;font-size:11.5px;letter-spacing:.02em;color:var(--forest-2);
  border-bottom:1px solid rgba(47,74,57,.3);padding-bottom:2px}
.morelink:hover{border-color:var(--forest);color:var(--forest)}
.cta{position:sticky;bottom:0;display:flex;gap:9px;margin:0 calc(var(--pad) * -1);
  padding:11px var(--pad) calc(11px + env(safe-area-inset-bottom));
  background:rgba(246,245,240,.95);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  border-top:1px solid var(--line)}
.btn{flex:1;display:flex;align-items:center;justify-content:center;gap:7px;height:52px;border-radius:10px;
  font-size:14.5px;font-weight:600;letter-spacing:.01em;color:#f3f1e7;background:var(--forest);
  box-shadow:0 10px 20px -14px rgba(27,46,36,.85);transition:background .16s,box-shadow .16s}
.btn:hover{background:var(--forest-2)}
.btn .ar{font-size:12px;opacity:.75}
.btn.nv{background:#03c75a;color:#06301c;box-shadow:0 10px 20px -14px rgba(3,199,90,.8)}
.btn.nv:hover{background:#02b351}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important;transform:none!important}}
</style>
</head>
<body>
<a class="skip" href="#main">본문으로 건너뛰기</a>
<div class="ftc">{ftc}</div>
<header class="site">
  <div class="in">
    <a class="brand" href="./"><span class="mk">{mark}</span><span class="bt">겨울 살림 마트</span></a>
    <div class="right">
      <span class="vol">2026년 11월 · 8개 장</span>
      <span class="sep vol"></span>
      <span>이번 호 <b data-count>{count}</b>가지</span>
    </div>
  </div>
</header>
"""


def esc(s):
    return html.escape(s, quote=True)


def card_html(p, no, label):
    pid = esc(p["id"])
    img = esc(p["imgs"][0])
    title = esc(p["title"])
    hook = esc(p.get("hook", ""))
    return (
        '      <article class="card" data-id="{pid}" data-cat="{cat}">\n'
        '        <a class="ph" href="#p={purl}" tabindex="-1" aria-hidden="true">'
        '<img src="{img}" alt="" loading="lazy" width="492" height="492"></a>\n'
        '        <div class="cbody">\n'
        '          <p class="meta"><span class="no">No. {no}</span>'
        '<span class="tag">{label}</span>{reel}</p>\n'
        '          <h3 class="name"><a href="#p={purl}">{title}</a></h3>\n'
        '          <p class="why">{hook}</p>\n'
        '          <a class="buy" href="{link}" target="_blank" rel="noopener noreferrer sponsored">'
        '<span class="bl">쿠팡에서 보기</span><span class="ar" aria-hidden="true">&#8599;</span></a>\n'
        '        </div>\n'
        '      </article>\n'
    ).format(pid=pid, cat=esc(p["s"]), purl=esc(p["id"]), img=img, no=f"{no:02d}",
             label=esc(label), title=title, hook=hook, link=esc(p["link"]),
             reel='<span class="tag reel">릴스</span>' if p.get("video") else '')


def build():
    src = INDEX.read_text(encoding="utf-8")
    m = re.search(r'\n<script type="application/json" id="d">(\[.*?)</script>', src, re.S)
    if not m:
        raise SystemExit("index.html 안에서 상품 JSON(#d)을 찾지 못했습니다.")
    data = json.loads(m.group(1))

    title = re.search(r"<title>(.*?)</title>", src, re.S).group(1).strip()
    desc = re.search(r'<meta name="description" content="(.*?)"', src).group(1).strip()
    ogimg = re.search(r'<meta property="og:image" content="(.*?)"', src).group(1).strip()

    labels = {s["slug"]: s["label"] for s in SECTIONS}
    counts = {s["slug"]: 0 for s in SECTIONS}
    for p in data:
        counts[p["s"]] = counts.get(p["s"], 0) + 1

    head = (HEAD.replace("{title}", esc(title)).replace("{desc}", esc(desc))
            .replace("{ogimg}", esc(ogimg)).replace("{ftc}", FTC)
            .replace("{mark}", MARK).replace("{count}", str(len(data))))
    out = [head]

    # 히어로 — 텍스트 + 대표 사진 1장(모바일은 3장 한 줄)
    a, b, c = HERO_IMAGES
    out.append(f"""<main id="main">
<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">살림하는 아줌마의 겨울 일기</p>
      <h1>첫 추위가 온 한 주</h1>
      <p class="stand">창틈에서 시작해 현관, 이불 속, 식탁 위까지. 한 주 동안 하나씩 찾아 둔
        겨울 살림 물건 {len(data)}가지를 장마다 모았습니다. 필요한 것만 골라 보세요.</p>
      <div class="hero-meta">
        <span>8개 장</span><span class="d"></span>
        <span>물건 <b data-count>{len(data)}</b>가지</span><span class="d"></span>
        <span>2026년 11월</span>
      </div>
      <p class="disc">일기는 꾸며 쓴 이야기예요. 사진은 판매 중인 상품 사진이에요.</p>
    </div>
    <div class="hero-media">
      <figure class="hm-main"><img src="{IMG_BASE}{a}" alt="" width="492" height="492" loading="eager" fetchpriority="high"></figure>
      <figure class="hm-thumb"><img src="{IMG_BASE}{b}" alt="" width="492" height="492" loading="lazy"></figure>
      <figure class="hm-thumb"><img src="{IMG_BASE}{c}" alt="" width="492" height="492" loading="lazy"></figure>
      <figcaption>이번 호에 실린 물건들 &mdash; 사진은 판매 중인 상품 사진입니다.</figcaption>
    </div>
  </div>
</section>

<section class="toc" aria-labelledby="toc-h">
  <h2 id="toc-h">차례</h2>
  <ol>
""")
    for s in SECTIONS:
        out.append(
            f'    <li><a href="#s-{s["slug"]}"><span class="n">{s["no"]}</span>'
            f'<span class="t"><em>{esc(s["eyebrow"].split(" · ")[1])}</em>{esc(s["title"])}</span>'
            f'<span class="c">{counts.get(s["slug"], 0)}</span></a></li>\n'
        )
    out.append("  </ol>\n</section>\n\n")

    # 탐색 바
    out.append(f"""<div class="tools">
  <div class="in">
    <div class="searchrow">
      <div class="search" id="sb">
        <svg class="ic" width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.7"/>
          <path d="M16.5 16.5 21 21" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <label class="sr" for="q">상품명이나 설명으로 찾기</label>
        <input id="q" type="search" placeholder="상품명이나 설명으로 찾기" autocomplete="off" spellcheck="false">
        <button class="clr" id="qc" type="button" aria-label="검색어 지우기">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
      </div>
      <p class="rs" id="rs" aria-live="polite"></p>
    </div>
    <div class="chips" role="group" aria-label="주제로 고르기">
      <button class="chip" type="button" data-cat="all" aria-pressed="true">전체 <span class="cn">{len(data)}</span></button>
""")
    for s in SECTIONS:
        out.append(
            f'      <button class="chip" type="button" data-cat="{s["slug"]}" aria-pressed="false">'
            f'{esc(s["label"])} <span class="cn">{counts.get(s["slug"], 0)}</span></button>\n'
        )
    out.append("    </div>\n  </div>\n</div>\n\n<div class=\"chapters\">\n")

    # 장 + 카드
    n = 0
    for s in SECTIONS:
        items = [p for p in data if p["s"] == s["slug"]]
        out.append(f"""  <section class="chapter" id="s-{s["slug"]}" data-cat="{s["slug"]}" aria-labelledby="h-{s["slug"]}">
    <div class="chead">
      <div class="chleft">
        <p class="chline"><span class="chn">{s["no"]}</span><span class="chlabel">{esc(s["eyebrow"].split(" · ")[1])}</span></p>
        <h2 id="h-{s["slug"]}">{esc(s["title"])}</h2>
      </div>
      <div class="chright">
        <p class="diary">{esc(s["diary"])}</p>
        <span class="chcount">물건 {len(items)}가지</span>
      </div>
    </div>
    <div class="grid">
""")
        for p in items:
            n += 1
            out.append(card_html(p, n, labels[s["slug"]]))
        out.append("    </div>\n  </section>\n\n")

    out.append("""  <div class="empty" id="empty">
    <p>찾는 물건이 없어요</p>
    <small>다른 낱말로 찾아보시거나, 전체를 눌러 처음으로 돌아가세요.</small>
    <button type="button" id="reset">전체 보기</button>
  </div>
</div>
</main>
""")

    out.append(f"""<footer class="foot">
  <div class="in">
    <div>
      <span class="fb"><span class="mk">{MARK}</span>겨울 살림 마트</span>
      <p>{FTC}<br>가격과 배송 조건은 판매처에서 바뀔 수 있어요.</p>
    </div>
    <div class="sig">살림하는 아줌마의 겨울 일기<br>VOL. 11 &middot; 2026</div>
  </div>
</footer>

<div class="dv" id="dv" hidden role="dialog" aria-modal="true" aria-labelledby="dt">
  <div class="dvi">
    <div class="dtop">
      <button id="bk" aria-label="뒤로">
        <svg width="21" height="21" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <path d="M15 5l-7 7 7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <span class="lb">겨울 살림 마트 &middot; <b id="dno"></b></span>
    </div>
    <div class="dbody">
      <div class="reelbox" id="dw" hidden>
        <video id="dwv" controls playsinline preload="metadata"></video>
        <div class="reelmeta"><b>릴스로 보기</b><a id="dwl" href="#" target="_blank" rel="noopener">영상만 열기</a></div>
      </div>
      <div class="gal" id="gal"></div>
      <a class="ds" id="ds"></a>
      <h1 id="dt"></h1>
      <p class="lead" id="dh"></p>
      <div class="reason" id="pw"><h2>이런 물건이에요</h2><ul id="dp"></ul></div>
      <p class="note">가격과 배송 조건은 쿠팡 상품 페이지에서 확인해 주세요. 판매처에서 바뀔 수 있어요.<br>{FTC}</p>
      <div id="rw"><h2>같은 장에서 찾아 둔 물건</h2><div class="rel" id="rel"></div><p id="rmore"></p></div>
    </div>
    <div class="cta" id="cta" data-cp="쿠팡에서 보기" data-nv="네이버에서 보기"></div>
  </div>
</div>
""")

    out.append('<script type="application/json" id="d">'
               + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
               + "</script>\n")

    out.append("""<script>
(function(){
  "use strict";
  var D = JSON.parse(document.getElementById('d').textContent);
  var LABEL = {};
""")
    for s in SECTIONS:
        out.append(f'  LABEL["{s["slug"]}"] = {json.dumps(s["label"], ensure_ascii=False)};\n')
    out.append("""  var M = {}, I = {};
  D.forEach(function(p, i){ M[p.id] = p; I[p.id] = i + 1; });

  function $(id){ return document.getElementById(id); }
  function el(tag, cls, txt){ var n = document.createElement(tag); if(cls) n.className = cls; if(txt != null) n.textContent = txt; return n; }
  function esc(s){ return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
  function pad(n){ return (n < 10 ? '0' : '') + n; }

  /* ---------- 카드 만들기 (JSON에만 있고 화면에 없는 상품 보충) ---------- */
  function makeCard(p){
    var id = encodeURIComponent(p.id), no = pad(I[p.id] || 0), lab = LABEL[p.s] || '';
    var a = document.createElement('article');
    a.className = 'card'; a.dataset.id = p.id; a.dataset.cat = p.s;
    a.innerHTML =
      '<a class="ph" href="#p=' + id + '" tabindex="-1" aria-hidden="true">' +
        '<img src="' + esc((p.imgs || [])[0] || '') + '" alt="" loading="lazy" width="492" height="492"></a>' +
      '<div class="cbody">' +
        '<p class="meta"><span class="no">No. ' + no + '</span><span class="tag">' + esc(lab) + '</span>' +
          (p.video ? '<span class="tag reel">릴스</span>' : '') + '</p>' +
        '<h3 class="name"><a href="#p=' + id + '">' + esc(p.title) + '</a></h3>' +
        '<p class="why">' + esc(p.hook || '') + '</p>' +
        '<a class="buy" href="' + esc(p.link || '') + '" target="_blank" rel="noopener noreferrer sponsored">' +
          '<span class="bl">쿠팡에서 보기</span><span class="ar" aria-hidden="true">&#8599;</span></a>' +
      '</div>';
    return a;
  }
  function renumber(){
    Array.prototype.forEach.call(document.querySelectorAll('.chapter'), function(sec){
      Array.prototype.forEach.call(sec.querySelectorAll('.card'), function(c){
        var n = c.querySelector('.no'); if(n) n.textContent = 'No. ' + pad(++SEQ);
      });
    });
  }
  var SEQ = 0;
  var grids = {};
  Array.prototype.forEach.call(document.querySelectorAll('.chapter'), function(sec){
    grids[sec.dataset.cat] = sec.querySelector('.grid');
  });
  var have = {};
  Array.prototype.forEach.call(document.querySelectorAll('.card[data-id]'), function(c){ have[c.dataset.id] = 1; });
  D.forEach(function(p){
    if(have[p.id] || !grids[p.s]) return;
    grids[p.s].appendChild(makeCard(p));
  });
  renumber();

  /* ---------- 검색·필터 ---------- */
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card'));
  var text = {};
  cards.forEach(function(c){
    var p = M[c.dataset.id] || {};
    text[c.dataset.id] = ((p.title || '') + ' ' + (p.hook || '') + ' ' + ((p.pts || []).join(' ')) +
      (p.video ? ' 릴스 영상' : '')).toLowerCase().replace(/\s+/g, ' ');
  });
  var chapters = Array.prototype.slice.call(document.querySelectorAll('.chapter'));
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var input = $('q'), box = $('sb'), rs = $('rs'), empty = $('empty');
  var cat = 'all', q = '';

  function apply(anchor){
    var terms = q.toLowerCase().replace(/\s+/g, ' ').trim().split(' ').filter(Boolean);
    var total = 0;
    chapters.forEach(function(sec){
      var n = 0;
      Array.prototype.forEach.call(sec.querySelectorAll('.card'), function(c){
        var ok = (cat === 'all' || sec.dataset.cat === cat) && terms.every(function(t){
          return (text[c.dataset.id] || '').indexOf(t) !== -1; });
        c.hidden = !ok;
        if(ok) n++;
      });
      sec.hidden = (n === 0);
      var cc = sec.querySelector('.chcount');
      if(cc) cc.textContent = '물건 ' + n + '가지';
      total += n;
    });
    var label = cat === 'all' ? '전체' : (LABEL[cat] || '');
    rs.innerHTML = q
      ? '&ldquo;' + esc(q) + '&rdquo; &middot; <b>' + total + '</b>가지'
      : label + ' &middot; <b>' + total + '</b>가지';
    box.classList.toggle('has', !!q);
    empty.classList.toggle('on', total === 0);
    if(anchor){
      var target = null;
      if(!total) target = empty;
      else chapters.forEach(function(sec){ if(!target && !sec.hidden) target = sec; });
      if(target){
        var bar = (document.querySelector('.site').offsetHeight || 0) +
                  (document.querySelector('.tools').offsetHeight || 0);
        var y = target.getBoundingClientRect().top + window.scrollY - bar - 14;
        if(Math.abs(window.scrollY - y) > 120) window.scrollTo({top: Math.max(0, y), behavior: 'smooth'});
      }
    }
  }
  function setCat(next){
    cat = next;
    chips.forEach(function(c){ c.setAttribute('aria-pressed', String(c.dataset.cat === cat)); });
    apply(true);
  }
  function reset(){ q = ''; input.value = ''; setCat('all'); }

  chips.forEach(function(c){ c.addEventListener('click', function(){ setCat(c.dataset.cat); }); });
  input.addEventListener('input', function(e){ if(e.isComposing) return; q = input.value; apply(true); });
  input.addEventListener('compositionend', function(){ q = input.value; apply(true); });
  input.addEventListener('keydown', function(e){ if(e.key === 'Escape'){ input.value = ''; q = ''; apply(); } });
  $('qc').addEventListener('click', function(){ input.value = ''; q = ''; input.focus(); apply(true); });
  $('reset').addEventListener('click', function(){ reset(); });
  Array.prototype.forEach.call(document.querySelectorAll('.toc a'), function(a){
    a.addEventListener('click', function(){ if(cat !== 'all' || q) reset(); });
  });

  /* ---------- 상세 ---------- */
  var dv = $('dv'), nav = 0, last = null, opened = null;
  function show(p){
    var rb = $('dw'), rv = $('dwv'), rl = $('dwl');
    if(p.video){
      rv.poster = (p.imgs || [])[0] || '';
      if(rv.getAttribute('src') !== p.video) rv.src = p.video;
      rl.href = p.video; rb.hidden = false;
    } else {
      try { rv.pause(); } catch(e){}
      rv.removeAttribute('src'); rv.load(); rb.hidden = true;
    }
    var g = $('gal'); g.textContent = '';
    (p.imgs || []).forEach(function(u){ var i = el('img'); i.src = u; i.alt = p.title; g.appendChild(i); });
    g.classList.toggle('one', (p.imgs || []).length < 2);
    var nc = document.querySelector('.card[data-id="' + p.id + '"] .no');
    $('dno').textContent = nc ? nc.textContent : ('No. ' + pad(I[p.id] || 0));
    $('ds').textContent = LABEL[p.s] || p.st || '';
    $('ds').href = '#s-' + p.s;
    $('dt').textContent = p.title;
    $('dh').textContent = p.hook || '';
    $('dh').hidden = !p.hook;
    var u = $('dp'); u.textContent = '';
    (p.pts || []).forEach(function(s){ u.appendChild(el('li', '', s)); });
    $('pw').hidden = !(p.pts || []).length;
    var a = $('cta'); a.textContent = '';
    [['cp', p.link, a.dataset.cp], ['nv', p.naver, a.dataset.nv]].forEach(function(b){
      if(b[1]){ var x = el('a', 'btn ' + b[0]);
        x.href = b[1]; x.appendChild(el('span', 'tx', b[2]));
        x.appendChild(el('span', 'ar', '\u2197'));
        x.target = '_blank'; x.rel = 'noopener noreferrer sponsored'; a.appendChild(x); }
    });
    var r = $('rel'); r.textContent = ''; var shown = 0, total = 0;
    D.forEach(function(o){
      if(o.s === p.s && o.id !== p.id) total++;
      if(o.s === p.s && o.id !== p.id && shown < 6){
        shown++;
        var x = el('a', 'rc'); x.href = '#p=' + encodeURIComponent(o.id);
        var i = el('img'); i.src = (o.imgs || [])[0]; i.alt = ''; i.loading = 'lazy';
        x.appendChild(i); x.appendChild(el('span', '', o.title)); r.appendChild(x);
      }
    });
    var more = $('rmore'); more.textContent = '';
    if(total > shown){
      var ma = el('a', 'morelink', '이 장에서 더 보기 (' + (total + 1) + '가지)');
      ma.href = '#s-' + p.s; more.appendChild(ma);
    }
    $('rw').hidden = !r.children.length;
    opened = document.querySelector('.card[data-id="' + p.id + '"]');
    if(dv.hidden) last = document.activeElement;
    dv.hidden = false; document.body.style.overflow = 'hidden';
    dv.scrollTop = 0; g.scrollLeft = 0; $('bk').focus();
  }
  function closeDv(){
    var rv = $('dwv'); if(rv && !rv.paused){ try { rv.pause(); } catch(e){} }
    dv.hidden = true; document.body.style.overflow = '';
    if(opened){
      opened.scrollIntoView({block: 'center', behavior: 'smooth'});
      opened.classList.add('flash');
      setTimeout(function(){ opened.classList.remove('flash'); }, 1800);
      opened = null;
    }
    if(last && last.focus) last.focus();
  }
  function route(){
    var m = /^#p=(.+)$/.exec(location.hash);
    var p = m && M[decodeURIComponent(m[1])];
    if(p) show(p);
    else if(!dv.hidden) closeDv();
  }
  function back(){
    if(nav) history.back();
    else { history.replaceState(null, '', location.pathname + location.search); route(); }
  }
  window.addEventListener('hashchange', function(){ nav++; route(); });
  $('bk').onclick = back;
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && !dv.hidden) back(); });

  /* 머리말 개수는 데이터에서 */
  Array.prototype.forEach.call(document.querySelectorAll('[data-count]'), function(n){
    n.textContent = D.length;
  });
  apply();
  route();
})();
</script>
""")

    digest = hashlib.sha1(json.dumps(data, ensure_ascii=False).encode()).hexdigest()[:12]
    out.append(f"<!-- build:{digest} · tools/build_bridge.py 로 생성 -->\n</body>\n</html>\n")

    INDEX.write_text("".join(out), encoding="utf-8")
    print(f"built index.html — {len(data)} items, build:{digest}")


if __name__ == "__main__":
    build()
