# 릴스·클립 발행 전 자동 검수 체크리스트

> 쓰는 사람: 클로드(영상 생성·수정), 피클(발행 전 최종 확인)
> 쓰는 때: `video_generator.py` 같은 스크립트로 만든 세로 영상을 인스타 릴스·네이버 클립·기타 숏폼에 올리기 **직전마다**. 한 번도 예외 없다.
> 이 문서는 실제 사고 기록에서 나왔다. 2장 "사고 이력"을 읽으면 왜 이 항목들이 있는지 알 수 있다.

---

## 0. 결론부터: 통과 기준 6개

| # | 항목 | 기준 | 미달 시 |
|---|---|---|---|
| 1 | 비디오 스트림 | 1080×1920(9:16), 15초(14.5~15.5), 25~30fps | 재렌더 |
| 2 | 오디오 스트림 존재 | 오디오 트랙이 **1개 이상** | 재합성 |
| 3 | 오디오 길이 | 비디오 길이와 차이 **0.3초 이내** | 재합성 |
| 4 | 오디오 레벨 | `mean_volume` ≥ -40 dB **그리고** `max_volume` ≥ -10 dB | 재합성 |
| 5 | 화면에 상품 이미지 | 추출 프레임의 `YSTD` ≥ 5 (단색·흰 카드 아님) | 렌더 경로 수정 후 재렌더 |
| 6 | 컨테이너 | MP4 / H.264(yuv420p) + AAC / `+faststart` | 리먹스 |

하나라도 미달이면 **업로드하지 않는다.** "올리고 나서 지우면 되지"는 금지 — 지운 영상도 계정 이력에 남고, 첫 3초가 평가되는 피드에서는 재업로드가 손해다.

---

## 1. 검수 절차

### 1-A. 트랙·길이 (오디오 누락·빈 오디오 잡기)

```bash
# 비디오·오디오 스트림 목록과 길이
ffprobe -v error -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate,duration \
        -of default=noprint_wrappers=1 "$F"

# 컨테이너 전체 길이
ffprobe -v error -show_entries format=duration -of csv=p=0 "$F"
```

판정 규칙
- `codec_type=audio` 줄이 **없으면** 즉시 실패(무음 영상이 아니라 오디오 트랙 자체가 없는 영상).
- 오디오 `duration`이 비디오 `duration`보다 **0.5초 이상 짧으면** 실패. 0.022초짜리 빈 트랙이 대표 사례다.
- 오디오 `duration`이 `N/A`로 나오면 `-show_streams`가 아닌 `-show_entries stream=duration_ts,time_base`로 한 번 더 확인한다. 그래도 없으면 실패로 본다.

### 1-B. 볼륨 (무음 더미 잡기)

```bash
ffmpeg -hide_banner -i "$F" -map 0:a:0 -af volumedetect -f null - 2>&1 | grep -E "mean_volume|max_volume"
```

- `mean_volume: -91.0 dB` → 완전 무음. 실패.
- `mean_volume`이 -40 dB보다 작으면 목소리가 사실상 안 들린다. 실패.
- `max_volume`이 -10 dB보다 작으면 전체가 눌려 있다. 실패.
- 반대로 `max_volume`이 0 dB에 붙어 있으면 클리핑이니 `-1 dB` 정도로 낮춰 재합성한다.

### 1-C. 화면에 이미지가 실제로 그려졌는지

렌더 스크립트가 상품 이미지를 **로드하지 못하면 흰 카드 위에 글자만** 남는다. 눈으로 보기 전에 기계로 거른다.

```bash
# 1초·5초·10초 프레임의 밝기 표준편차(YSTD). 단색/흰 배경이면 5 미만.
for T in 1 5 10; do
  echo -n "t=${T}s YSTD="
  ffmpeg -hide_banner -ss "$T" -i "$F" -frames:v 1 \
    -vf "signalstats,metadata=print:key=lavfi.signalstats.YSTD" -f null - 2>&1 \
    | sed -n 's/.*YSTD=//p' | tail -1
done
```

- 세 값 중 **하나라도 5 미만**이면 그 구간은 빈 카드다. 실패.
- YSTD가 정상인데도 상품 사진이 비어 보이면, 프레임을 뽑아 눈으로 확인한다:
  ```bash
  ffmpeg -hide_banner -ss 5 -i "$F" -frames:v 1 -y /tmp/frame5.png
  ```
- 렌더 단계에서 미리 막는 편이 싸다. 사전 검사 3개를 먼저 돌린다.
  ```bash
  # 상품 이미지 경로가 실제로 존재하고 0바이트가 아닌지
  for p in $(grep -oE '(img|v)/[A-Za-z0-9._-]+\.(jpg|png|webp)' video_generator.py | sort -u); do
    [ -s "$p" ] || echo "MISSING or EMPTY: $p"
  done
  ```
- 렌더 로그에 "이미지 N장 로드" 같은 카운트를 남기고, 기대 장수와 다르면 렌더를 중단시킨다.

### 1-D. 규격·컨테이너

```bash
# 픽셀 포맷·프로파일·faststart 확인
ffprobe -v error -show_entries stream=codec_name,pix_fmt,profile,bit_rate -of default=noprint_wrappers=1 "$F"
ffprobe -v error -show_entries format=format_name,duration,size -of default=noprint_wrappers=1 "$F"
```

- 고정 기준: **1080×1920 / 15초 / 30fps / H.264 High, yuv420p / AAC 48kHz 스테레오 / `+faststart`**.
- yuv420p가 아니면 아이폰·일부 안드로이드에서 재생이 깨진다. 반드시 확인.
- 재인코딩이 필요하면:
  ```bash
  ffmpeg -hide_banner -i in.mp4 -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 \
         -c:a aac -ar 48000 -b:a 128k -movflags +faststart out.mp4
  ```
- **길이 상한·용량 상한은 플랫폼이 자주 바꾼다.** 인스타 릴스와 네이버 클립 모두 9:16 세로 MP4를 받지만, 업로드 화면에 표시되는 그날의 상한을 그때 확인한다. 우리 쪽 기준은 "15초·1080×1920"으로 고정해 두면 어느 쪽 상한에도 걸리지 않는다.

---

## 2. 사고 이력 (왜 이 항목이 있는가)

- **2026-11-14 · 오디오 0.022초**: 15초 영상의 오디오 트랙이 0.022초(샘플 11개)에서 끝나는 빈 트랙으로 올라갔다. 음성 합성(`edge-tts`) 결과가 합쳐지지 않은 채 렌더된 것으로 보였다. 업로드 후에야 "소리가 없다"는 지적을 받았다.
- **2026-11-14 · 상품 이미지 누락**: 렌더 스크립트가 `img/` 안의 상품 사진을 로드하지 못해 흰 카드에 초록 글자만 있는 장면이 나왔다. 같은 원인으로 여러 편이 동시에 결함 상태였다.
- **교훈 세 가지**
  1. 렌더 성공(파일 생성)과 상품 성공(볼 만한 영상)은 다르다. 파일이 생겼다는 것만으로 다음 단계로 넘어가지 않는다.
  2. 오디오는 "트랙이 있는가"가 아니라 "비디오 길이만큼 들리는가"로 검사한다.
  3. 이미지는 "경로가 맞는가"와 "화면에 그려졌는가"를 따로 본다. 둘 다 검사한다.

---

## 3. 한 번에 돌리는 검수 스크립트

`reels_qa.sh`로 저장해 두고 `sh reels_qa.sh v/영상.mp4`로 쓴다. 실패하면 종료 코드 1.

```bash
#!/bin/sh
# reels_qa.sh — 릴스/클립 발행 전 검수. 통과: exit 0, 실패: exit 1
F="$1"; FAIL=0
say() { printf '%s\n' "$*"; }
bad() { say "  ✗ $*"; FAIL=1; }

[ -s "$F" ] || { say "파일 없음/0바이트: $F"; exit 1; }

VD=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of csv=p=0 "$F")
WH=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$F")
PF=$(ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of csv=p=0 "$F")
AC=$(ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$F" | wc -l)
AD=$(ffprobe -v error -select_streams a:0 -show_entries stream=duration -of csv=p=0 "$F")

say "파일: $F"
say "  비디오 ${VD}s ${WH} ${PF} / 오디오 트랙 ${AC}개 (${AD:-없음}s)"

[ "$WH" = "1080x1920" ] || bad "해상도가 1080x1920이 아님: $WH"
[ "$PF" = "yuv420p" ] || bad "픽셀 포맷이 yuv420p가 아님: $PF"
awk "BEGIN{exit !($VD>14.5 && $VD<15.5)}" || bad "비디오 길이가 15초대가 아님: $VD"
[ "$AC" -ge 1 ] || bad "오디오 트랙이 없음"
if [ "$AC" -ge 1 ] && [ -n "$AD" ]; then
  awk "BEGIN{d=$VD-$AD; if(d<0)d=-d; exit !(d<0.3)}" || bad "오디오 길이가 비디오와 0.3초 이상 차이: ${AD}s"
fi
if [ "$AC" -ge 1 ] && [ -z "$AD" ]; then bad "오디오 길이를 읽을 수 없음"; fi
if [ "$AC" -ge 1 ]; then
  V=$(ffmpeg -hide_banner -i "$F" -map 0:a:0 -af volumedetect -f null - 2>&1)
  MEAN=$(printf '%s' "$V" | sed -n 's/.*mean_volume: \(-*[0-9.]*\) dB.*/\1/p' | tail -1)
  MAX=$(printf '%s' "$V"  | sed -n 's/.*max_volume: \(-*[0-9.]*\) dB.*/\1/p'  | tail -1)
  say "  볼륨 mean=${MEAN}dB max=${MAX}dB"
  awk "BEGIN{exit !($MEAN>-40)}" || bad "평균 볼륨이 너무 작음(무음 의심): ${MEAN}dB"
  awk "BEGIN{exit !($MAX>-10)}" || bad "최대 볼륨이 너무 작음: ${MAX}dB"
fi

for T in 1 5 10; do
  Y=$(ffmpeg -hide_banner -ss "$T" -i "$F" -frames:v 1 \
        -vf "signalstats,metadata=print:key=lavfi.signalstats.YSTD" -f null - 2>&1 \
      | sed -n 's/.*YSTD=//p' | tail -1)
  say "  t=${T}s YSTD=${Y:-읽기 실패}"
  if [ -z "$Y" ]; then bad "t=${T}s 프레임을 읽지 못함"
  else awk "BEGIN{exit !($Y>=5)}" || bad "t=${T}s 화면이 단색에 가까움(이미지 누락 의심)"; fi
done

[ "$FAIL" -eq 0 ] && say "  ✓ 통과 — 업로드 가능" || say "  ✗ 실패 — 업로드 금지"
exit "$FAIL"
```

### ffmpeg 없이 트랙만 급히 볼 때 (표준 라이브러리만)

PC에 ffmpeg가 없거나 파이프라인 안에서 바로 확인하고 싶을 때 쓴다. 오디오 트랙이 얼마나 짧은지는 이걸로도 잡힌다.

```python
#!/usr/bin/env python3
"""mp4probe.py — ffprobe 없이 MP4 트랙 요약. 사용: python3 mp4probe.py <file.mp4>"""
import struct, sys

def boxes(buf, start, end):
    i = start
    while i + 8 <= end:
        size = struct.unpack('>I', buf[i:i+4])[0]
        typ = buf[i+4:i+8].decode('latin-1')
        hdr = 8
        if size == 1:
            size = struct.unpack('>Q', buf[i+8:i+16])[0]; hdr = 16
        elif size == 0:
            size = end - i
        if size < hdr: break
        yield typ, i + hdr, min(i + size, end)
        i += size

def find(buf, s, e, path):
    for typ, a, b in boxes(buf, s, e):
        if typ == path[0]:
            return (a, b) if len(path) == 1 else find(buf, a, b, path[1:])
    return None

def probe(path):
    buf = open(path, 'rb').read()
    moov = find(buf, 0, len(buf), ['moov'])
    if not moov:
        return {'file': path, 'error': 'moov 없음 (조각 MP4일 수 있음)'}
    out = []
    for typ, s, e in boxes(buf, moov[0], moov[1]):
        if typ != 'trak': continue
        h = find(buf, s, e, ['mdia', 'hdlr'])
        kind = {'vide': 'video', 'soun': 'audio'}.get(
            buf[h[0]:h[1]][8:12].decode('latin-1'), 'other') if h else 'other'
        m = find(buf, s, e, ['mdia', 'mdhd'])
        dur = ts = None
        if m:
            v = buf[m[0]:m[1]]
            if v[0] == 1:
                ts = struct.unpack('>I', v[20:24])[0]; dur = struct.unpack('>Q', v[24:32])[0]
            else:
                ts = struct.unpack('>I', v[12:16])[0]; dur = struct.unpack('>I', v[16:20])[0]
        st = find(buf, s, e, ['mdia', 'minf', 'stbl', 'stsz'])
        samples = struct.unpack('>I', buf[st[0]+8:st[0]+12])[0] if st else None
        out.append({'kind': kind, 'duration_s': round(dur / ts, 3) if ts and dur else None,
                    'samples': samples})
    return {'file': path, 'tracks': out}

if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(probe(f))
```

실제 출력 예 (2026-11-15, 결함 영상 2편에서 동일하게 나옴):

```
{'file': 'v/….mp4', 'tracks': [{'kind': 'video', 'duration_s': 15.0, 'samples': 450},
                               {'kind': 'audio', 'duration_s': 0.022, 'samples': 11}]}
```

→ 비디오 15.0초 / 오디오 0.022초(샘플 11개). 이 상태로는 절대 업로드하지 않는다.
(한계: 조각 MP4(fragmented)는 트랙을 못 읽을 수 있다. 그때는 ffprobe로 확인한다.)

### 실패했을 때 조치 순서
1. 오디오가 짧거나 없음 → `edge-tts` 합성 결과 파일이 실제로 생성됐는지, 길이가 몇 초인지 먼저 확인. 합성 실패를 빈 파일로 넘기지 않게 합성 직후 길이 검사 후 렌더로 넘긴다.
2. 합성은 됐는데 영상이 짧음 → `-shortest`를 무심코 붙이면 짧은 쪽(빈 오디오)에 맞춰 잘린다. 오디오 길이를 확인한 뒤 붙인다.
3. 이미지가 안 보임 → 렌더 스크립트의 이미지 경로(상대/절대), 파일 존재, 로드 완료 대기(네트워크 이미지면 특히)를 확인. 로컬 파일이면 즉시 로드 실패가 로그에 남는다.
4. 재렌더 후 **1장부터 다시** 이 스크립트를 돌린다. 이미 통과한 파일도 다시 검사한다(같은 스크립트를 고쳤으면 전부 다시).

---

## 4. 발행 기록 (표를 계속 채운다)

| 날짜 | 파일 | 검수(YSTD/볼륨/길이) | 업로드처 | 결과 |
|---|---|---|---|---|
| 2026-11-14 | v/…f70bcbd1.mp4 | 오디오 0.022s · YSTD 미달 | (미업로드, 보류) | 실패 — 수정 요청 |

- 발행한 영상은 파일명·업로드 시각·채널을 남긴다. 나중에 "이 영상 소리 왜 없냐"는 말이 나오면 이 표가 답이 된다.
- 같은 파일을 다른 채널에 올릴 때도 검수는 다시 하지 않지만, **업로드 화면에서 실제 재생**은 한 번 확인한다.

## 5. 최종 확인 (사람이 1번)

기계 검사를 통과해도 마지막은 눈으로 본다. 30초면 된다.
- [ ] 첫 1초에 상품 또는 숫자가 보이는가
- [ ] 소리가 끝까지 들리는가(중간에 끊기지 않는가)
- [ ] 마지막 2초에 단서 문구(지형 해석/공개 자료 기준)가 있는가
- [ ] 자막이 화면 아래 UI(좋아요·캡션)에 가리지 않는가 — 아래 15%는 비워 둔다
- [ ] 파일명에 날짜와 상품명이 있는가
