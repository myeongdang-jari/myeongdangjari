# BRIDGE

## 개요
- 본 문서는 기획 산출물과 PC 로컬 빌더 프로그램 간의 작업 연동 규격서입니다.
- 웹페이지 생성, 템플릿 빌드 및 소셜 발행 스크립트는 PC 로컬 환경에서 실행합니다.
- 공개 저장소 규정에 따라 내부 수치 및 정산 정보는 포함하지 않습니다.
- 2026-11-16 갱신: 쿠팡 파트너스 계정에서 발급한 상품 링크 25건과 상품 사진으로 카탈로그를 다시 구성했습니다.
- 2026-11-17 갱신: 겨울 인기 품목과 호기심 상품 7건을 더해 상품 링크 32건으로 늘렸습니다.
- 2026-11-21 갱신(2차): 유튜브 쇼츠 검증 기준을 「최근 30일 업로드 · 조회 10만 이상」으로 낮춘 대표님 확정에 맞춰 편의점·마트 신상 3건(오리온 꼬북칩 얼얼한 샹궈맛 102g 12개·롯데웰푸드 ABC 초콜릿 187g 3개·이디야 비니스트 토피넛 라떼분말 20g 30개입)을 더하고 세 건 모두 30일 안에 올라온 쇼츠 근거(evidence)를 붙였습니다. 상품 링크 63건입니다.
- 2026-11-21 갱신: 욕실·수납 3건(홈스타 핑크파워 욕실 찌든때 클리너 750ml 2개·물빠짐 샤워봉 거치 선반 세트·무타공 욕실 수납선반 6종 세트)을 더하고 세 건 모두에 유튜브 쇼츠 근거(evidence)를 붙였습니다. 화장지(tissue)는 보류로 내려 새 글·페이지에서 빼고 JSON 배열에서도 제외해 상품 링크 60건입니다.
- 2026-11-20 갱신: 수면양말 2종(5종 SET·4켤레 세트)·하루온 붙이는 핫팩·순샘 주방세제 리필·코멧 접이식 빨래건조대·다이슨 에어랩·제스파 컴포르테 안마의자 7건을 더해 상품 링크 58건입니다.
- 2026-11-19 갱신(2차): 써모스 보온도시락·오리온 어드벤트 캘린더·따수미 난방텐트·코멧 아기물티슈·우드피카 유아 바라클라바 5건을 더해 상품 링크 51건입니다. 토스쇼핑 쉐어링크(https://toss.shopping/_m/5Y0O20Ah)도 브릿지 하단에 함께 걸었습니다.
- 2026-11-19 갱신: 미니 제습기·12L 제습기·극세사 차렵이불·욕실 온풍기·족욕기·목어깨 마사지기·필터 샤워기·화목난로 8건을 더해 상품 링크 46건입니다.
- 2026-11-18 갱신: 성에방지 커버·발열조끼·반반 전기그릴·붕어빵 메이커·1인용 사우나·무선 제설기 6건을 더해 상품 링크 38건입니다.
- 쇼츠 검증 기준(2026-11-21 대표님 확정): 최근 30일 안에 올라온 쇼츠 · 조회 10만 이상. 영상 속 상품 이름·브랜드를 알 수 있고, 쿠팡에 같은 브랜드·용량이 있으며, 묶음·대용량·로켓배송처럼 쿠팡에서 살 이유가 있는 것만 담습니다. 조회 10만으로 낮춘 만큼 터진 영상이 아닌 것도 들어오므로 why_coupang에 약한 부분을 솔직히 적습니다.
- 문구 규칙: 가격 숫자·최저가·써 본 척·효과 장담·이모지 없이 씁니다.

## 상품 데이터

### 상품 1
- id: partition-heater
- 이름: 홈플래닛 접이식 파티션 히터, D2401, 그레이
- 갈래: 겨울 난방·방풍
- 계정: ads
- 후킹 한 줄: 책상 아래로 시린 발목과 무릎만 따로 감싸 주는 접이식 발난로입니다.
- 요약: 삼면을 세워 찬 공기를 막고 원적외선 면발열로 데우는 방식이라 바람이 일지 않습니다. 쓰지 않을 때는 접어 세워 둘 수 있습니다.
- 쿠팡 검색어: 접이식 파티션 히터
- 상품 링크: https://link.coupang.com/a/iIEIHsSHfM
- 사진: img/products/partition-heater.jpg

### 상품 2
- id: electric-blanket
- 이름: HanilMedical 탄소열선 고급 전기요 HL-D205(25), 북극곰, M
- 갈래: 겨울 난방·방풍
- 계정: ads
- 후킹 한 줄: 잠자리에 들기 전 이불 속을 미리 데워 두는 탄소열선 전기요입니다.
- 요약: 탄소 열선을 촘촘히 넣어 온도가 고르게 퍼지고, 켜 둔 지 오래되면 스스로 꺼집니다. 세탁이 되는 소재라 겨울이 끝난 뒤 손질도 간단합니다.
- 쿠팡 검색어: 한일의료기 전기요
- 상품 링크: https://link.coupang.com/a/iCGTm4Ipcy
- 사진: img/products/electric-blanket.jpg

### 상품 3
- id: wind-pack
- 이름: 에코와이드 끼우는 문풍지 창문 틈새막이 외풍 창틀 바람막이 L, 4개
- 갈래: 겨울 난방·방풍
- 계정: ads
- 후킹 한 줄: 창틀 홈에 끼워 넣기만 하면 창문 틈으로 드는 바람을 줄여 줍니다.
- 요약: 접착제나 공구 없이 창틀 레일 홈에 끼우는 방식이라 이사 갈 때도 떼어 다시 쓸 수 있습니다. 네 개들이라 방마다 나눠 끼우기 좋습니다.
- 쿠팡 검색어: 창문 틈새막이
- 상품 링크: https://link.coupang.com/a/iCGEleYKcK
- 사진: img/products/wind-pack.jpg

### 상품 4
- id: bubble-wrap
- 이름: 뽁순이 3중 뽁뽁이 단열에어캡, 1개
- 갈래: 겨울 난방·방풍
- 계정: ads
- 후킹 한 줄: 창유리에 붙여 방 안 온기가 밖으로 빠져나가는 것을 줄이는 단열 시트입니다.
- 요약: 3중 에어캡 구조가 공기층을 만들어 유리에서 오는 냉기를 덜어 줍니다. 물만 뿌려 붙이는 방식이라 뜯어낼 때도 자국이 남지 않습니다.
- 쿠팡 검색어: 단열 뽁뽁이
- 상품 링크: https://link.coupang.com/a/iIEMwhrXoW
- 사진: img/products/bubble-wrap.jpg

### 상품 5
- id: door-curtain
- 이름: 유미코 겨울 현관 자석 방풍커튼, 1개
- 갈래: 겨울 난방·방풍
- 계정: ads
- 후킹 한 줄: 문을 여닫을 때마다 복도 한기가 밀려오는 현관에 두르는 자석 커튼입니다.
- 요약: 가운데가 자석으로 붙어 사람이 지나가면 스스로 닫히고, 문틀에 벨크로로 걸어 못을 쓰지 않습니다. 안감이 두툼해 바람을 막아 줍니다.
- 쿠팡 검색어: 현관 방풍커튼
- 상품 링크: https://link.coupang.com/a/iIEQEbGvW8
- 사진: img/products/door-curtain.jpg

### 상품 6
- id: weatherstrip
- 이름: 코멧 국내생산 사계절 우레탄 문풍지 3M, 5개
- 갈래: 겨울 난방·방풍
- 계정: ads
- 후킹 한 줄: 문과 창문 틈에 붙여 바람이 새는 자리를 막는 접착식 우레탄 폼입니다.
- 요약: 말랑한 우레탄이라 울퉁불퉁한 틈에도 모양대로 밀착되고 계절 상관없이 쓸 수 있습니다. 3M씩 다섯 롤이라 문마다 나눠 붙이기 좋습니다.
- 쿠팡 검색어: 문풍지
- 상품 링크: https://link.coupang.com/a/iIESNRkMGO
- 사진: img/products/weatherstrip.jpg

### 상품 7
- id: humidifier
- 이름: 홈플래닛 초음파 가습기 4L, RD210/화이트
- 갈래: 겨울 난방·방풍
- 계정: ads
- 후킹 한 줄: 난방으로 건조해진 방 공기에 물안개를 채우는 4L 초음파 가습기입니다.
- 요약: 물통을 위에서 열어 바로 채우고, 본체와 통이 분리돼 안쪽까지 씻을 수 있습니다. 통이 커서 물을 채우는 일이 잦지 않습니다.
- 쿠팡 검색어: 가습기 4L
- 상품 링크: https://link.coupang.com/a/iIE620JWfI
- 사진: img/products/humidifier.jpg

### 상품 8
- id: hand-warmer
- 이름: 하루온 군인핫팩 포켓용 대용량 핫팩 160g, 30개
- 갈래: 출퇴근·차량
- 계정: ads
- 후킹 한 줄: 주머니에 넣고 하루를 버티는 대용량 포켓 핫팩입니다.
- 요약: 160g 큰 사이즈라 온기가 오래갑니다. 30개입 한 상자라 아침에 하나씩 챙겨 나가기 좋습니다.
- 쿠팡 검색어: 하루온 핫팩
- 상품 링크: https://link.coupang.com/a/iCGMOaYd52
- 사진: img/products/hand-warmer.jpg

### 상품 9
- id: balaclava
- 이름: 라세르 겨울 방한 기모 바라클라바
- 갈래: 출퇴근·차량
- 계정: ads
- 후킹 한 줄: 목부터 정수리까지 한 번에 감싸는 기모 바라클라바입니다.
- 요약: 얼굴 둘레에 기모 안감을 넣어 찬 바람이 목덜미로 들어오는 것을 줄입니다. 헬멧이나 모자 안에 같이 쓸 수 있는 두께입니다.
- 쿠팡 검색어: 방한 바라클라바
- 상품 링크: https://link.coupang.com/a/iIEUEDeUua
- 사진: img/products/balaclava.jpg

### 상품 10
- id: anti-fog
- 이름: 소낙스 김서림 방지제 관리용품, 500ml, 1개
- 갈래: 출퇴근·차량
- 계정: ads
- 후킹 한 줄: 겨울 아침 차에 오르면 앞유리에 서리는 김을 줄여 주는 코팅제입니다.
- 요약: 유리 안쪽에 뿌려 닦아 두면 수증기가 맺히는 자리가 줄어듭니다. 500ml라 한 겨울 내내 차 한 대에 쓰기 넉넉합니다.
- 쿠팡 검색어: 김서림 방지제
- 상품 링크: https://link.coupang.com/a/iIE2GCK1TM
- 사진: img/products/anti-fog.jpg

### 상품 11
- id: ice-scraper
- 이름: 깔끔조아 스크래치 없는 회전형 길이조절 차량용 성에제거기, 1개
- 갈래: 출퇴근·차량
- 계정: ads
- 후킹 한 줄: 손이 닿지 않는 앞유리 가운데까지 밀어 내는 길이조절 스크래퍼입니다.
- 요약: 손잡이 각도가 돌아가고 길이가 늘어나 차 높이에 맞춰 쓸 수 있습니다. 브러시가 함께 달려 눈과 성에를 한 번에 정리합니다.
- 쿠팡 검색어: 차량 성에제거기
- 상품 링크: https://link.coupang.com/a/iIE47Fx8DY
- 사진: img/products/ice-scraper.jpg

### 상품 12
- id: sink-splash
- 이름: 달팽이리빙 퀴진드마망 실리콘 씽크대 물막이, 크림화이트, 1개
- 갈래: 주방·살림
- 계정: ads
- 후킹 한 줄: 설거지할 때 튀는 물이 옷과 바닥으로 가지 않게 세우는 실리콘 판입니다.
- 요약: 하단 흡착판으로 상판에 붙여 세우고, 말랑한 실리콘 재질이라 부딪혀도 소리가 나지 않습니다. 물때가 끼면 통째로 씻어 말리면 됩니다.
- 쿠팡 검색어: 싱크대 물막이
- 상품 링크: https://link.coupang.com/a/iIEWfbNl0e
- 사진: img/products/sink-splash.jpg

### 상품 13
- id: oil-screen
- 이름: 시샘 연마제없는 스텐 다용도 기름방지망, 33cm, 1개
- 갈래: 주방·살림
- 계정: ads
- 후킹 한 줄: 고기를 굽거나 튀길 때 튀는 기름을 막아 두는 스테인리스 망입니다.
- 요약: 촘촘한 망이라 김은 빠져나가고 기름은 막아 줍니다. 손잡이가 달려 있어 조리 중에도 집기 편합니다.
- 쿠팡 검색어: 기름튐 방지망
- 상품 링크: https://link.coupang.com/a/iIEXV8gHw4
- 사진: img/products/oil-screen.jpg

### 상품 14
- id: drain-filter
- 이름: 코멧 싱크대 배수구 거름망, 500개
- 갈래: 주방·살림
- 계정: take
- 후킹 한 줄: 배수구에 끼워 음식물 찌꺼기와 머리카락을 한 번에 걸러 내는 망입니다.
- 요약: 한 장씩 끼워 쓰고 가득 차면 그대로 버리면 됩니다. 500장이라 몇 달은 다시 사러 가지 않아도 됩니다.
- 쿠팡 검색어: 배수구 거름망
- 상품 링크: https://link.coupang.com/a/iIFajZuk5A
- 사진: img/products/drain-filter.jpg

### 상품 15
- id: tissue
- 이름: 쿠팡 베이직 천연펄프 3겹 롤 화장지 30m, 30개입, 1개
- 갈래: 주방·살림
- 계정: take
- 후킹 한 줄: 3겹 도톰한 롤 화장지 30롤 한 상자입니다.
- 요약: 천연펄프 3겹이라 물에 잘 풀리고 도톰한 편입니다. 30롤 한 상자라 다 쓰고 나서 다시 사러 가는 일이 줄어듭니다.
- 쿠팡 검색어: 3겹 화장지 30롤
- 상품 링크: https://link.coupang.com/a/iIEOjsfmXA
- 사진: img/products/tissue.jpg
- 상태: 보류 (2026-11-21) — 유튜브 쇼츠 30만 이상 근거를 확인하지 못해 새 글·페이지에 쓰지 않습니다. JSON 배열에서도 제외했습니다.

### 상품 16
- id: diatomite-mat
- 이름: 코멧 홈 빨아쓰는 규조토 발매트, 베이지 타원, 1개
- 갈래: 욕실·위생
- 계정: take
- 후킹 한 줄: 욕실에서 나와 젖은 발을 한 번만 디디면 물기를 빨아들이는 발매트입니다.
- 요약: 규조토가 섞인 연질 소재라 돌처럼 단단하지 않고 발에 부드럽습니다. 빨아서 말릴 수 있어 눅눅한 냄새 걱정이 덜합니다.
- 쿠팡 검색어: 규조토 발매트
- 상품 링크: https://link.coupang.com/a/iIE0nWcz24
- 사진: img/products/diatomite-mat.jpg

### 상품 17
- id: mold-gel
- 이름: 홈스타 바르는 곰팡이 싹 세정제, 120ml, 2개
- 갈래: 욕실·위생
- 계정: take
- 후킹 한 줄: 줄눈과 실리콘 틈에 발라 두면 문지르지 않아도 곰팡이가 들뜨는 젤형 세정제입니다.
- 요약: 흘러내리지 않는 젤이라 벽면에도 붙어 있습니다. 뾰족한 노즐로 좁은 틈에 바로 짜 넣을 수 있습니다.
- 쿠팡 검색어: 곰팡이 제거 젤
- 상품 링크: https://link.coupang.com/a/iIE8F8LqqO
- 사진: img/products/mold-gel.jpg

### 상품 18
- id: fish-cake
- 이름: 효성어묵 부산옛날어묵 종합 (냉동), 1kg, 1개
- 갈래: 겨울간식·식품
- 계정: take
- 후킹 한 줄: 냉동실에 두고 국이나 떡볶이에 꺼내 쓰는 종합 어묵입니다.
- 요약: 사각·봉·야채 어묵이 섞여 있어 요리마다 골라 쓰기 좋습니다. 1kg이라 몇 번 나눠 먹을 양입니다.
- 쿠팡 검색어: 효성어묵 종합
- 상품 링크: https://link.coupang.com/a/iCGPZ9URPM
- 사진: img/products/fish-cake.jpg

### 상품 19
- id: hoppang
- 이름: 삼립 호빵 발효미종 단팥 + 야채, 97g, 12개입, 1세트
- 갈래: 겨울간식·식품
- 계정: take
- 후킹 한 줄: 전자레인지나 찜기에 데워 겨울 저녁에 먹는 단팥·야채 호빵입니다.
- 요약: 단팥과 야채가 반씩 들어 있어 골라 먹는 재미가 있습니다. 낱개 포장이라 먹을 만큼만 데우면 됩니다.
- 쿠팡 검색어: 삼립 호빵
- 상품 링크: https://link.coupang.com/a/iIFbUN1Zwy
- 사진: img/products/hoppang.jpg

### 상품 20
- id: boongeoppang
- 이름: 비비고 단팥붕어빵 (냉동), 300g, 1개
- 갈래: 겨울간식·식품
- 계정: take
- 후킹 한 줄: 에어프라이어에 돌리면 겉은 바삭하고 속은 뜨거운 냉동 붕어빵입니다.
- 요약: 팬에 기름을 두르지 않고 에어프라이어로 데울 수 있습니다. 300g 한 봉이라 아이 간식으로 부담 없는 양입니다.
- 쿠팡 검색어: 비비고 붕어빵
- 상품 링크: https://link.coupang.com/a/iIFdE5NoCO
- 사진: img/products/boongeoppang.jpg

### 상품 21
- id: hot-choco
- 이름: 미떼 핫초코 오리지날, 30g, 30개입, 1개
- 갈래: 겨울간식·식품
- 계정: take
- 후킹 한 줄: 우유에 한 봉 풀면 되는 핫초코 30봉입니다.
- 요약: 개별 포장이라 한 잔씩 뜯어 타면 됩니다. 사무실이나 아이 간식으로 두고 쓰기 좋은 구성입니다.
- 쿠팡 검색어: 미떼 핫초코
- 상품 링크: https://link.coupang.com/a/iIFf8a2pjg
- 사진: img/products/hot-choco.jpg

### 상품 22
- id: music-box
- 이름: 홀리해요 크리스마스 오르골 무드등 플랫 스노우볼, 산타
- 갈래: 홈·데코
- 계정: take
- 후킹 한 줄: 손잡이를 들면 눈이 내리고 음악이 흐르는 납작한 스노우볼입니다.
- 요약: 세워 두거나 들고 다닐 수 있는 형태라 선반과 식탁 어디에나 놓입니다. 불을 켜면 은은한 무드등으로도 쓸 수 있습니다.
- 쿠팡 검색어: 크리스마스 오르골 스노우볼
- 상품 링크: https://link.coupang.com/a/iCIEE8o6uW
- 사진: img/products/music-box.jpg

### 상품 23
- id: music-box-lamp
- 이름: 스네몬 오르골 오로라 무드등, 핑크화이트
- 갈래: 홈·데코
- 계정: take
- 후킹 한 줄: 오로라 빛이 돌아가며 방 천장까지 물들이는 오르골 무드등입니다.
- 요약: 음악이 나오는 오르골에 오로라 조명이 함께 들어 있어 아이 방 취침등으로도 쓸 수 있습니다. 밝기를 낮춰 잠들 때 켜 두기 좋습니다.
- 쿠팡 검색어: 오르골 무드등
- 상품 링크: https://link.coupang.com/a/iIFhNLDGpw
- 사진: img/products/music-box-lamp.jpg

### 상품 24
- id: mini-tree
- 이름: 크리스마스 40cm 설레는 밤 완제 트리 풀세트 전구포함, 혼합색상
- 갈래: 홈·데코
- 계정: take
- 후킹 한 줄: 꾸미는 수고 없이 꺼내 세우면 모습이 갖춰지는 40cm 미니 트리입니다.
- 요약: 장식과 전구가 이미 달려 있어 처음 트리를 두는 집도 부담이 적습니다. 40cm라 원룸이나 아이 방 책상 위에도 놓입니다.
- 쿠팡 검색어: 미니 크리스마스 트리
- 상품 링크: https://link.coupang.com/a/iIFjGOaEQC
- 사진: img/products/mini-tree.jpg

### 상품 25
- id: fleece-blanket
- 이름: 더자리 마이블랭킷 극세사 담요
- 갈래: 홈·데코
- 계정: take
- 후킹 한 줄: 소파에 두고 무릎 덮기 좋은 극세사 담요입니다.
- 요약: 촘촘한 극세사라 가볍고 부드럽습니다. 이불 위에 한 겹 더 덮거나 차에 두고 쓰기 좋습니다.
- 쿠팡 검색어: 극세사 담요
- 상품 링크: https://link.coupang.com/a/iIFk7hUsDs
- 사진: img/products/fleece-blanket.jpg

### 상품 26
- id: electric-seat
- 이름: HanilMedical 1인용 전기방석 HL-100(20), 네이비, 450 x 450 mm
- 갈래: 잠자리
- 계정: take
- 후킹 한 줄: 소파나 의자에 앉아 있는 동안 엉덩이부터 따뜻하게 데우는 1인용 전기방석입니다.
- 요약: 전원을 넣으면 열선이 골고루 퍼지고, 쓰지 않을 때는 돌돌 말아 두면 됩니다. 등받이 의자나 소파 한쪽에 깔아 두기 좋은 크기입니다.
- 쿠팡 검색어: 전기방석 1인용
- 상품 링크: https://link.coupang.com/a/iJZa0xMjV6
- 사진: img/products/electric-seat.jpg

### 상품 27
- id: k2-gloves
- 이름: K2 세이프티 히트플렉스 니트 장갑, 1세트, 블랙
- 갈래: 출퇴근길
- 계정: ads
- 후킹 한 줄: 자전거 손잡이나 버스 손잡이를 잡는 아침, 손끝이 시린 것을 덜어 주는 니트 장갑입니다.
- 요약: 니트로 짠 장갑이라 손등에 닿는 감촉이 부드럽고, 두께가 두껍지 않아 가방이나 코트 주머니에 넣어 두기 좋습니다.
- 쿠팡 검색어: K2 방한장갑
- 상품 링크: https://link.coupang.com/a/iJZgIrr1O0
- 사진: img/products/k2-gloves.jpg

### 상품 28
- id: kimchi
- 이름: 종가 포기김치, 2.3kg, 1개
- 갈래: 겨울 야식
- 계정: take
- 후킹 한 줄: 김장을 직접 담그지 않는 집에서 겨울 내내 꺼내 먹기 좋은 포기김치입니다.
- 요약: 한 통으로 와서 김치통에 옮겨 담아 두면 됩니다. 국이나 찌개에 넣을 때도 한 포기씩 꺼내 쓰기 좋습니다.
- 쿠팡 검색어: 종가 포기김치
- 상품 링크: https://link.coupang.com/a/iJZojEkCYe
- 사진: img/products/kimchi.jpg

### 상품 29
- id: radiator
- 이름: 신일 컴팩트 라디에이터 5핀, SER-D5500KP
- 갈래: 겨울 준비
- 계정: take
- 후킹 한 줄: 보일러를 켜기엔 아까운 날, 방 하나만 데우는 전기 라디에이터입니다.
- 요약: 기름이 도는 방식이라 바람이 일지 않고 소리가 크지 않습니다. 바퀴가 달려 있어 방과 거실 사이를 옮겨 가며 쓸 수 있습니다.
- 쿠팡 검색어: 신일 라디에이터
- 상품 링크: https://link.coupang.com/a/iJZvbm24om
- 사진: img/products/radiator.jpg

### 상품 30
- id: tokyotomi-heater
- 이름: 토요토미 팬히터 LC-L53 풀세트 (국내 정품 A/S 가능) 도요토미, BLACK
- 갈래: 별별템
- 계정: ads
- 후킹 한 줄: 캠핑하는 사람들이 먼저 찾는 일본식 팬히터입니다. 쿠팡에 정품으로 올라와 있습니다.
- 요약: 기름을 넣고 쓰는 난로라 환기에 신경 써야 하고, 무게가 있어 한 번 자리를 잡으면 거실 한쪽에 두고 쓰게 됩니다.
- 쿠팡 검색어: 토요토미 팬히터
- 상품 링크: https://link.coupang.com/a/iJZycVPxSu
- 사진: img/products/tokyotomi-heater.jpg

### 상품 31
- id: drone
- 이름: DJI Neo 2 플라이 모어 콤보 드론, 혼합색상, 1세트
- 갈래: 별별템
- 계정: ads
- 후킹 한 줄: 손바닥만 한 크기로 하늘 사진을 남기는 드론입니다. 쿠팡 가전 코너에 이런 것도 있습니다.
- 요약: 본체와 조종기, 배터리가 함께 오는 구성입니다. 겨울 여행에서 위에서 찍은 사진을 남기고 싶을 때 눈에 들어오는 세트입니다.
- 쿠팡 검색어: DJI Neo 2 드론
- 상품 링크: https://link.coupang.com/a/iJZCB6mDYq
- 사진: img/products/drone.jpg

### 상품 32
- id: premiere-projector
- 이름: 삼성전자 The Premiere 프로젝터 웜 화이트 254~330cm 방문설치, SP-LPDU9SAXXKR
- 갈래: 별별템
- 계정: ads
- 후킹 한 줄: 벽에 붙여 두고 쓰는 삼성 초단초점 프로젝터입니다. 장바구니에 담아 둘 수 있는 가전으로 쿠팡에 올라와 있습니다.
- 요약: 방문 설치로 배송되는 모델이라 자리를 잡아 주는 과정까지 포함되어 있습니다. 거실 벽 한 면을 화면으로 쓰고 싶을 때 비교해 볼 만한 상품입니다.
- 쿠팡 검색어: 삼성 더 프리미어 프로젝터
- 상품 링크: https://link.coupang.com/a/iJZGHOUWlM
- 사진: img/products/premiere-projector.jpg

### 상품 33
- id: frost-cover
- 이름: 카템 3중 차단 마그네틱 성에방지 커버, 전차종, 1세트
- 갈래: 출퇴근길
- 계정: take
- 후킹 한 줄: 아침에 성에를 긁는 대신 밤에 덮어 두는 앞유리 커버입니다.
- 요약: 자석과 문틈 고정 방식이라 덮어 두고 아침에 걷어 내면 됩니다. 사이드미러까지 함께 덮는 구성이라 유리에 앉은 성에를 밀어 내는 시간을 줄이는 쪽입니다.
- 쿠팡 검색어: 차량 성에방지커버
- 상품 링크: https://link.coupang.com/a/iLFf9cx10m
- 사진: img/products/frost-cover.jpg

### 상품 34
- id: heating-vest
- 이름: 에쉬울프 USB 발열조끼 스마트 온열조끼, DR013
- 갈래: 출퇴근길
- 계정: take
- 후킹 한 줄: 보조배터리를 꽂으면 앞판과 뒷판이 데워지는 조끼입니다.
- 요약: 패딩 안에 껴입거나 단독으로 입고 다닐 수 있는 두께입니다. USB 연결 방식이라 쓰는 보조배터리 용량에 따라 사용 시간이 달라지고, KC 인증 표기가 있는지 확인해 두는 편이 좋습니다.
- 쿠팡 검색어: USB 발열조끼
- 상품 링크: https://link.coupang.com/a/iLFuzgsa9k
- 사진: img/products/heating-vest.jpg

### 상품 35
- id: electric-grill
- 이름: 홈플래닛 반반 멀티 전기그릴(개별 온도 조절), AD-SK18
- 갈래: 연말 홈파티
- 계정: take
- 후킹 한 줄: 한쪽은 굽고 한쪽은 끓이는 반반 상판 전기그릴입니다.
- 요약: 좌우 온도를 따로 조절해 고기와 국물 요리를 같이 올려 둘 수 있습니다. 상판이 넓어 식탁 가운데에 두고 여러 명이 둘러앉기 좋습니다.
- 쿠팡 검색어: 반반 전기그릴
- 상품 링크: https://link.coupang.com/a/iLEWQmy5U4
- 사진: img/products/electric-grill.jpg

### 상품 36
- id: fishbread-maker
- 이름: 위즈웰 간식 메이커 3종 세트 붕어빵 + 와플 + 샌드위치, WSW-6137
- 갈래: 겨울 간식
- 계정: take
- 후킹 한 줄: 플레이트를 바꿔 끼우면 붕어빵, 와플, 샌드위치가 되는 전기 메이커입니다.
- 요약: 붕어빵틀과 와플판, 샌드위치판이 한 세트로 옵니다. 아이와 같이 반죽을 붓고 기다리는 겨울 방학 간식용입니다.
- 쿠팡 검색어: 붕어빵 메이커
- 상품 링크: https://link.coupang.com/a/iLE0sQqZEq
- 사진: img/products/fishbread-maker.jpg

### 상품 37
- id: home-sauna
- 이름: [휴먼사우나] 로벤스 편백나무+히노끼 스톤찜질+좌훈+족욕찜질 원적외선 반신욕기, LPH-300
- 갈래: 별별템
- 계정: ads
- 후킹 한 줄: 집에 들이는 1인용 반신욕기입니다. 편백나무 안에서 앉는 자리와 스톤을 데우는 구조입니다.
- 요약: 원적외선 방식이라 물을 끓이지 않고 앉는 자리와 스톤을 데웁니다. 크기와 무게가 있어 둘 자리와 문 폭을 먼저 재 보고 정하는 편이 좋습니다.
- 쿠팡 검색어: 1인용 가정용 사우나
- 상품 링크: https://link.coupang.com/a/iLFmqwxj0C
- 사진: img/products/home-sauna.jpg

### 상품 38
- id: snow-blower
- 이름: 클라빈다 충전식 무선 전동 리튬 배터리 제설기 소형 다기능 휴대용 가정용 고출력 접이식, 1세트
- 갈래: 별별템
- 계정: ads
- 후킹 한 줄: 눈이 온 날 아침, 삽 대신 미는 충전식 제설기입니다.
- 요약: 충전 배터리로 눈을 밀어 내는 소형 제설기입니다. 배터리 포함 여부와 날개 폭이 값을 가릅니다. 같은 검색에 손에 드는 송풍기형이 섞여 나오니 상품 구분을 확인해 보세요.
- 쿠팡 검색어: 무선 제설기
- 상품 링크: https://link.coupang.com/a/iLF6x1Pvky
- 사진: img/products/snow-blower.jpg

### 상품 39
- id: mini-dehumidifier
- 이름: EXTEDRG 제습기 2.8L 강력제습 가정용 저소음 원룸 미니 제습기, D9
- 갈래: 결로·습기
- 계정: take
- 후킹 한 줄: 창틀에 물방울이 맺히는 날, 방 안 물을 물통으로 모으는 작은 제습기입니다.
- 요약: 옷장이나 욕실처럼 좁은 자리에 두는 2.8L 소형입니다. 물통이 차면 표시가 뜨고, 습도가 내려가면 스스로 멈춥니다.
- 쿠팡 검색어: 미니 제습기
- 상품 링크: https://link.coupang.com/a/iNjEeRx34C
- 사진: img/products/mini-dehumidifier.jpg

### 상품 40
- id: dehumidifier-12l
- 이름: 롯데알미늄 제습기 12L, LDH-7000N
- 갈래: 결로·습기
- 계정: take
- 후킹 한 줄: 빨래를 널어 둔 방의 물을 하루 12L까지 빼내는 컴프레서 제습기입니다.
- 요약: 일일 제습량 12L, 사용면적 약 10평으로 표기된 모델입니다. 물통은 2L이고 연속배수 호스를 연결할 수 있어 물 비우는 일을 줄일 수 있습니다.
- 쿠팡 검색어: 가정용 제습기 12L
- 상품 링크: https://link.coupang.com/a/iNjUwx2rpA
- 사진: img/products/dehumidifier-12l.jpg

### 상품 41
- id: winter-duvet
- 이름: 코멧 홈 양면 극세사 솔리드 차렵이불
- 갈래: 겨울 침구
- 계정: take
- 후킹 한 줄: 커버를 씌우지 않고 바로 덮는 겨울 극세사 차렵이불입니다.
- 요약: 솜이 안에 누벼 있어 이불커버 없이 쓰고, 빨래도 한 장만 하면 됩니다. 앞뒤 색이 달라 뒤집어 덮을 수 있습니다.
- 쿠팡 검색어: 극세사 차렵이불
- 상품 링크: https://link.coupang.com/a/iNjFeUXyNw
- 사진: img/products/winter-duvet.jpg

### 상품 42
- id: bathroom-heater
- 이름: 한경희생활과학 PTC 온풍기 욕실 난방기 스탠드 벽걸이 전기히터, HAAN-4000(블랙)
- 갈래: 욕실 난방
- 계정: take
- 후킹 한 줄: 욕실 벽에 걸거나 세워 두고 샤워 전에 켜 두는 온풍기입니다.
- 요약: 벽에 걸거나 세워 두는 겸용형이라 좁은 욕실에서 놓을 자리를 골라 쓸 수 있습니다. 물이 닿는 곳에 두는 제품이라 설치 위치와 전원은 설명서를 따라 확인해 두는 편이 좋습니다.
- 쿠팡 검색어: 욕실 온풍기
- 상품 링크: https://link.coupang.com/a/iNkaGmHDW0
- 사진: img/products/bathroom-heater.jpg

### 상품 43
- id: foot-spa
- 이름: 이노크아든 사파이어 스파 족욕기, FM-505, 화이트
- 갈래: 겨울 발 보온
- 계정: take
- 후킹 한 줄: 물을 받아 온도를 맞춰 두는 습식 족욕기입니다.
- 요약: 온도를 정해 두면 맞춰 가열하고, 바닥에 지압 롤러와 거품 기능이 있습니다. 고정형이라 둘 자리와 콘센트 위치를 먼저 정하는 편이 좋습니다.
- 쿠팡 검색어: 가정용 족욕기
- 상품 링크: https://link.coupang.com/a/iNjK48KKbs
- 사진: img/products/foot-spa.jpg

### 상품 44
- id: neck-massager
- 이름: 제스파 플러스 목어깨 등 허리 마사지기, ZP187, 퍼플
- 갈래: 겨울 몸풀기
- 계정: take
- 후킹 한 줄: 목에 걸치고 기대서 쓰는 목·어깨 마사지기입니다.
- 요약: 4개의 안마볼이 돌아가며 방향을 바꾸고, 온열을 함께 켤 수 있습니다. 15분이 지나면 스스로 꺼지고, 차량용 전원선이 함께 들어 있습니다.
- 쿠팡 검색어: 목어깨 마사지기
- 상품 링크: https://link.coupang.com/a/iNjJRe2DPU
- 사진: img/products/neck-massager.jpg

### 상품 45
- id: filter-shower
- 이름: 코멧 홈 파워수압 필터 샤워기 본품 + 필터 2개입, 실버
- 갈래: 욕실
- 계정: take
- 후킹 한 줄: 헤드 안쪽 필터로 물을 한 번 거르는 샤워기입니다.
- 요약: 본체와 필터 2개가 한 세트로 옵니다. 필터는 2~3개월 주기로 갈아 끼우고, 수압을 올려 주는 판이 들어 있습니다.
- 쿠팡 검색어: 필터 샤워기
- 상품 링크: https://link.coupang.com/a/iNjGtwDojc
- 사진: img/products/filter-shower.jpg

### 상품 46
- id: firewood-stove
- 이름: 아웃도어웍스 화목난로, OW200
- 갈래: 별별템
- 계정: ads
- 후킹 한 줄: 장작을 넣고 불을 보는 캠핑용 화목난로입니다.
- 요약: 연통과 함께 세팅하는 스테인리스 난로입니다. 불을 쓰는 제품이라 실내에서는 환기와 설치 자리, 소방 안전을 먼저 확인해야 합니다.
- 쿠팡 검색어: 캠핑 화목난로
- 상품 링크: https://link.coupang.com/a/iNjIJWmvVk
- 사진: img/products/firewood-stove.jpg

### 상품 47
- id: thermos-lunchbox
- 이름: 써모스 일체형 대용량 보온도시락 + 보온백 + 수저 세트, 샌드베이지, 1개
- 갈래: 주방·도시락
- 계정: take
- 후킹 한 줄: 국물이나 반찬이 식지 않게 싸 가는 보온도시락입니다.
- 요약: 1500ml를 네 단으로 나눠 담는 일체형이고 보온백과 수저가 같이 옵니다. 보냉도 되는 제품으로 표기돼 있습니다.
- 쿠팡 검색어: 써모스 보온도시락
- 상품 링크: https://link.coupang.com/a/iNGqzfSzhA
- 사진: img/products/thermos-lunchbox.jpg

### 상품 48
- id: advent-calendar
- 이름: 오리온 크리스마스 어드벤트 캘린더 과자세트, 9종, 1세트
- 갈래: 크리스마스
- 계정: myeongjanae
- 후킹 한 줄: 12월에 하루씩 열어 보는 크리스마스 달력입니다.
- 요약: 과자 9종이 들어 있는 혼합 세트입니다. 상자 겉면에 작은 문들이 있어 12월에 하나씩 열어 보는 방식입니다.
- 쿠팡 검색어: 어드벤트 캘린더
- 상품 링크: https://link.coupang.com/a/iNGrtQRPe8
- 사진: img/products/advent-calendar.jpg

### 상품 49
- id: heating-tent
- 이름: 따수미 패브릭 난방텐트 3인용
- 갈래: 겨울 난방·방풍
- 계정: take
- 후킹 한 줄: 침대 위에 씌워 방 하나만 덥히는 난방텐트입니다.
- 요약: 지퍼로 여닫고 바닥이 없는 구조라 침대 위에 덮어 쓰는 방식입니다. 3인용(킹) 크기로 나온 제품입니다.
- 쿠팡 검색어: 패브릭 난방텐트
- 상품 링크: https://link.coupang.com/a/iNGssAUnfM
- 사진: img/products/heating-tent.jpg

### 상품 50
- id: baby-wipes
- 이름: 코멧 오리지널 유아용 아기물티슈 캡형, 100매입
- 갈래: 생필품
- 계정: myeongjanae
- 후킹 한 줄: 한 장씩 뽑아 쓰는 아기물티슈입니다.
- 요약: 캡을 눌러 한 장씩 뽑는 캡형 100매입입니다. 상품평이 49만 개가 넘고 한 달에 10만 명 이상이 산 상품입니다.
- 쿠팡 검색어: 코멧 아기물티슈
- 상품 링크: https://link.coupang.com/a/iNGtoaNmy4
- 사진: img/products/baby-wipes.jpg

### 상품 51
- id: kids-balaclava
- 이름: 우드피카 유아용 패치 바라클라바 넥워머
- 갈래: 겨울 방한
- 계정: take
- 후킹 한 줄: 목부터 머리까지 한 번에 덮는 아동용 넥워머입니다.
- 요약: 단추로 여미는 아크릴 니트라 목도리처럼 풀리지 않습니다. 아동·유아용으로 나온 제품입니다.
- 쿠팡 검색어: 유아 바라클라바
- 상품 링크: https://link.coupang.com/a/iNGukGGgi4
- 사진: img/products/kids-balaclava.jpg

## 데이터 인터페이스 (JSON)

### 상품 52
- id: socks-5set
- 이름: 퍼니스코 여성 겨울 수면 양말 5종 SET
- 갈래: 겨울 침구·수면
- 계정: take
- 후킹 한 줄: 밤에 발이 시려 양말을 신고 자는 집에 두는 무압박 수면양말입니다.
- 요약: 밴딩을 세게 조이지 않아 신고 자도 발목에 자국이 덜 남습니다. 다섯 켤레가 한 세트라 빨아 가며 돌려 신기 좋습니다.
- 쿠팡 검색어: 여성 수면양말 5종
- 상품 링크: https://link.coupang.com/a/iO8Bl4KKOa
- 사진: img/products/socks-5set.jpg

### 상품 53
- id: socks-4set
- 이름: 이지하임 4켤레 털빠짐없는 편안한 무압박 남녀공용 수면양말 세트
- 갈래: 겨울 침구·수면
- 계정: take
- 후킹 한 줄: 수면양말을 신고 나면 털이 묻어 나와 고민이던 집에 두는 네 켤레 세트입니다.
- 요약: 상품명에 털 빠짐을 줄인 소재로 표기돼 있습니다. 남녀공용으로 나와 온 가족이 나눠 신을 수 있습니다.
- 쿠팡 검색어: 무압박 수면양말 4켤레
- 상품 링크: https://link.coupang.com/a/iO8FgfqG8O
- 사진: img/products/socks-4set.jpg

### 상품 54
- id: hotpack-attach
- 이름: 하루온 붙이는 핫팩 50g 10개입, 2개
- 갈래: 겨울 방한
- 계정: take
- 후킹 한 줄: 옷 안쪽에 붙여 두면 손에 쥐지 않아도 등과 배가 따뜻한 핫팩입니다.
- 요약: 10개입 봉지 두 개로 오는 구성입니다. 상품평이 5만 2천 개가 넘고, 최근 한 달 사이 7천 명 이상이 산 것으로 표시돼 있습니다.
- 쿠팡 검색어: 하루온 붙이는 핫팩
- 상품 링크: https://link.coupang.com/a/iO8CicdLVc
- 사진: img/products/hotpack-attach.jpg

### 상품 55
- id: dish-soap
- 이름: 순샘 구연산 자몽향 주방세제 리필, 1.4L, 3개
- 갈래: 살림·세제
- 계정: take
- 후킹 한 줄: 설거지할 때 기름이 잘 빠지지 않아 세제를 더 짜게 되는 집에 두는 리필입니다.
- 요약: 1.4L 리필 세 통 구성입니다. 구연산이 들어간 자몽향 세제로 표기돼 있습니다.
- 쿠팡 검색어: 순샘 주방세제 리필
- 상품 링크: https://link.coupang.com/a/iO8DtBKacu
- 사진: img/products/dish-soap.jpg

### 상품 56
- id: drying-rack
- 이름: 코멧 홈 접이식 대형 빨래건조대, 그레이, 1개
- 갈래: 살림·빨래
- 계정: take
- 후킹 한 줄: 겨울엔 밖에 못 널어 거실에 건조대를 펴 두게 되는 집에 두는 접이식 건조대입니다.
- 요약: 쓰지 않을 때는 접어 세워 둘 수 있습니다. 상품평이 2만 2천 개가 넘는 상품입니다.
- 쿠팡 검색어: 코멧 접이식 빨래건조대
- 상품 링크: https://link.coupang.com/a/iO8Eo2uBq0
- 사진: img/products/drying-rack.jpg

### 상품 57
- id: dyson-airwrap
- 이름: 다이슨 에어랩 id 멀티 스타일러 앤 드라이어, 161845-01, 블루 + 코퍼
- 갈래: 뷰티·가전
- 계정: ads
- 후킹 한 줄: 겨울 외출 전에 머리를 말리고 모양까지 잡고 싶다는 말이 나올 때 눈에 들어오는 기계입니다.
- 요약: 본체와 여러 가지 헤드가 함께 오는 구성입니다. 머리를 말리는 일과 모양을 잡는 일을 한 자리에서 끝내는 쪽입니다.
- 쿠팡 검색어: 다이슨 에어랩
- 상품 링크: https://link.coupang.com/a/iO8Gt4yyfk
- 사진: img/products/dyson-airwrap.jpg

### 상품 58
- id: massage-chair
- 이름: 제스파 컴포르테 안마의자 + 전용 러그 방문설치, ZPC2034(안마의자), ZP540(러그), 퓨어화이트
- 갈래: 가전·설치
- 계정: ads
- 후킹 한 줄: 퇴근하고 소파 대신 앉겠다고 하는 자리에 놓는 전신 안마의자입니다.
- 요약: 안마의자와 전용 러그가 함께 오고 방문 설치로 배송됩니다. 크기와 무게가 있어 둘 자리와 문 폭을 먼저 재 보고 정하는 편이 좋습니다.
- 쿠팡 검색어: 제스파 컴포르테 안마의자
- 상품 링크: https://link.coupang.com/a/iO8HqggG16
- 사진: img/products/massage-chair.jpg

### 상품 59
- id: homstar-pink
- 이름: 홈스타 핑크파워 욕실 찌든때 클리너, 750ml, 2개
- 갈래: 욕실·위생
- 계정: take
- 후킹 한 줄: 욕실 타일과 줄눈의 찌든 때에 뿌려 두는 거품형 세정제입니다.
- 요약: 분사대가 달린 750ml 두 통 구성입니다. 거품을 붙여 두었다가 물로 헹구는 방식으로 쓰고, 욕실과 주방에 한 통씩 나눠 둘 수 있습니다.
- 쿠팡 검색어: 홈스타 핑크파워
- 상품 링크: https://link.coupang.com/a/iQCW1zM8US
- 사진: img/products/homstar-pink.jpg

### 상품 60
- id: shower-rod-shelf
- 이름: 물빠짐 샤워봉 거치 선반 + 보조캡 3종 + 방수테이프 세트, 화이트, 1세트
- 갈래: 욕실 수납
- 계정: take
- 후킹 한 줄: 샤워봉에 걸어 물이 빠지는 자리에 두는 선반입니다.
- 요약: 샤워봉에 걸어 고정하는 방식이라 타공 없이 설치합니다. 바닥이 물빠짐 구조라 샴푸병 밑에 물이 고이지 않고, 보조캡과 방수테이프가 함께 옵니다.
- 쿠팡 검색어: 샤워봉 선반
- 상품 링크: https://link.coupang.com/a/iQC1PH3waW
- 사진: img/products/shower-rod-shelf.jpg

### 상품 61
- id: bathroom-shelf-set
- 이름: 다용도 무타공 욕실 수납선반 6종 세트 일자형 드라이기 거치대 비누받침대 칫솔걸이, 화이트, 1세트
- 갈래: 욕실 수납
- 계정: take
- 후킹 한 줄: 못을 쓰지 않고 붙이는 욕실 수납 6종 세트입니다.
- 요약: 일자형 선반과 비누받침, 칫솔걸이, 드라이기 거치대를 한 세트로 묶은 구성입니다. 물이 빠지는 구조라 세면대 옆에 두기 좋습니다.
- 쿠팡 검색어: 무타공 욕실선반 세트
- 상품 링크: https://link.coupang.com/a/iQC5PCoQuq
- 사진: img/products/bathroom-shelf-set.jpg

### 상품 62
- id: kobukchip-sanghu
- 이름: 오리온 꼬북칩 얼얼한 샹궈맛, 102g, 12개
- 갈래: 편의점 간식·과자
- 계정: ads
- 후킹 한 줄: 편의점에서 한 봉씩 집어 오던 매운 과자를 열두 봉 한 번에 받는 구성입니다.
- 요약: 샹궈 향과 얼얼한 매운맛이 도는 102g 봉입니다. 열두 봉이라 야식이나 간식으로 하나씩 꺼내 먹기 좋고, 편의점에 들러 낱봉으로 사 모으는 일이 줄어듭니다. 신상이라 상품평은 아직 적습니다.
- 쿠팡 검색어: 꼬북칩 얼얼한 샹궈맛
- 상품 링크: https://link.coupang.com/a/iQESmpr2vQ
- 사진: img/products/kobukchip-sanghu.jpg

### 상품 63
- id: abc-choco-187
- 이름: 롯데웰푸드 ABC 초콜릿, 187g, 3개
- 갈래: 간식·초콜릿
- 계정: ads
- 후킹 한 줄: 마트에서 한 봉씩 사 오던 ABC 초콜릿을 세 봉 묶어 받는 구성입니다.
- 요약: 187g 봉지 세 개로 옵니다. 책상 서랍이나 가방에 나눠 두고 하나씩 꺼내 먹기 좋고, 로켓배송으로 다음 날 도착합니다.
- 쿠팡 검색어: 롯데 ABC 초콜릿 187g
- 상품 링크: https://link.coupang.com/a/iQEVKNmeo8
- 사진: img/products/abc-choco-187.jpg

### 상품 64
- id: ediya-toffe-nut
- 이름: 이디야 비니스트 토피넛 라떼분말, 20g, 30개입, 1개
- 갈래: 겨울 음료·커피
- 계정: take
- 후킹 한 줄: 코스트코에서 상자째 사 오던 토피넛 라떼 스틱을 서른 봉으로 받는 구성입니다.
- 요약: 20g 스틱 30개입 한 상자입니다. 뜨거운 물에 한 봉 풀면 되고 상품평이 8천 개가 넘습니다. 코스트코에 가지 않아도 로켓배송으로 다음 날 도착합니다.
- 쿠팡 검색어: 이디야 토피넛 라떼
- 상품 링크: https://link.coupang.com/a/iQEYy7kS3E
- 사진: img/products/ediya-toffe-nut.jpg
```json
[
  {
    "id": "partition-heater",
    "name": "홈플래닛 접이식 파티션 히터, D2401, 그레이",
    "partners_link": "https://link.coupang.com/a/iIEIHsSHfM",
    "image": "img/products/partition-heater.jpg",
    "account": "ads",
    "category": "겨울 난방·방풍",
    "hook": "책상 아래로 시린 발목과 무릎만 따로 감싸 주는 접이식 발난로입니다.",
    "summary": [
      "삼면을 세워 찬 공기를 막고 원적외선 면발열로 데우는 방식이라 바람이 일지 않습니다. 쓰지 않을 때는 접어 세워 둘 수 있습니다."
    ],
    "search_keyword": "접이식 파티션 히터"
  },
  {
    "id": "electric-blanket",
    "name": "HanilMedical 탄소열선 고급 전기요 HL-D205(25), 북극곰, M",
    "partners_link": "https://link.coupang.com/a/iCGTm4Ipcy",
    "image": "img/products/electric-blanket.jpg",
    "account": "ads",
    "category": "겨울 난방·방풍",
    "hook": "잠자리에 들기 전 이불 속을 미리 데워 두는 탄소열선 전기요입니다.",
    "summary": [
      "탄소 열선을 촘촘히 넣어 온도가 고르게 퍼지고, 켜 둔 지 오래되면 스스로 꺼집니다. 세탁이 되는 소재라 겨울이 끝난 뒤 손질도 간단합니다."
    ],
    "search_keyword": "한일의료기 전기요"
  },
  {
    "id": "wind-pack",
    "name": "에코와이드 끼우는 문풍지 창문 틈새막이 외풍 창틀 바람막이 L, 4개",
    "partners_link": "https://link.coupang.com/a/iCGEleYKcK",
    "image": "img/products/wind-pack.jpg",
    "account": "ads",
    "category": "겨울 난방·방풍",
    "hook": "창틀 홈에 끼워 넣기만 하면 창문 틈으로 드는 바람을 줄여 줍니다.",
    "summary": [
      "접착제나 공구 없이 창틀 레일 홈에 끼우는 방식이라 이사 갈 때도 떼어 다시 쓸 수 있습니다. 네 개들이라 방마다 나눠 끼우기 좋습니다."
    ],
    "search_keyword": "창문 틈새막이"
  },
  {
    "id": "bubble-wrap",
    "name": "뽁순이 3중 뽁뽁이 단열에어캡, 1개",
    "partners_link": "https://link.coupang.com/a/iIEMwhrXoW",
    "image": "img/products/bubble-wrap.jpg",
    "account": "ads",
    "category": "겨울 난방·방풍",
    "hook": "창유리에 붙여 방 안 온기가 밖으로 빠져나가는 것을 줄이는 단열 시트입니다.",
    "summary": [
      "3중 에어캡 구조가 공기층을 만들어 유리에서 오는 냉기를 덜어 줍니다. 물만 뿌려 붙이는 방식이라 뜯어낼 때도 자국이 남지 않습니다."
    ],
    "search_keyword": "단열 뽁뽁이"
  },
  {
    "id": "door-curtain",
    "name": "유미코 겨울 현관 자석 방풍커튼, 1개",
    "partners_link": "https://link.coupang.com/a/iIEQEbGvW8",
    "image": "img/products/door-curtain.jpg",
    "account": "ads",
    "category": "겨울 난방·방풍",
    "hook": "문을 여닫을 때마다 복도 한기가 밀려오는 현관에 두르는 자석 커튼입니다.",
    "summary": [
      "가운데가 자석으로 붙어 사람이 지나가면 스스로 닫히고, 문틀에 벨크로로 걸어 못을 쓰지 않습니다. 안감이 두툼해 바람을 막아 줍니다."
    ],
    "search_keyword": "현관 방풍커튼"
  },
  {
    "id": "weatherstrip",
    "name": "코멧 국내생산 사계절 우레탄 문풍지 3M, 5개",
    "partners_link": "https://link.coupang.com/a/iIESNRkMGO",
    "image": "img/products/weatherstrip.jpg",
    "account": "ads",
    "category": "겨울 난방·방풍",
    "hook": "문과 창문 틈에 붙여 바람이 새는 자리를 막는 접착식 우레탄 폼입니다.",
    "summary": [
      "말랑한 우레탄이라 울퉁불퉁한 틈에도 모양대로 밀착되고 계절 상관없이 쓸 수 있습니다. 3M씩 다섯 롤이라 문마다 나눠 붙이기 좋습니다."
    ],
    "search_keyword": "문풍지"
  },
  {
    "id": "humidifier",
    "name": "홈플래닛 초음파 가습기 4L, RD210/화이트",
    "partners_link": "https://link.coupang.com/a/iIE620JWfI",
    "image": "img/products/humidifier.jpg",
    "account": "ads",
    "category": "겨울 난방·방풍",
    "hook": "난방으로 건조해진 방 공기에 물안개를 채우는 4L 초음파 가습기입니다.",
    "summary": [
      "물통을 위에서 열어 바로 채우고, 본체와 통이 분리돼 안쪽까지 씻을 수 있습니다. 통이 커서 물을 채우는 일이 잦지 않습니다."
    ],
    "search_keyword": "가습기 4L"
  },
  {
    "id": "hand-warmer",
    "name": "하루온 군인핫팩 포켓용 대용량 핫팩 160g, 30개",
    "partners_link": "https://link.coupang.com/a/iCGMOaYd52",
    "image": "img/products/hand-warmer.jpg",
    "account": "ads",
    "category": "출퇴근·차량",
    "hook": "주머니에 넣고 하루를 버티는 대용량 포켓 핫팩입니다.",
    "summary": [
      "160g 큰 사이즈라 온기가 오래갑니다. 30개입 한 상자라 아침에 하나씩 챙겨 나가기 좋습니다."
    ],
    "search_keyword": "하루온 핫팩"
  },
  {
    "id": "balaclava",
    "name": "라세르 겨울 방한 기모 바라클라바",
    "partners_link": "https://link.coupang.com/a/iIEUEDeUua",
    "image": "img/products/balaclava.jpg",
    "account": "ads",
    "category": "출퇴근·차량",
    "hook": "목부터 정수리까지 한 번에 감싸는 기모 바라클라바입니다.",
    "summary": [
      "얼굴 둘레에 기모 안감을 넣어 찬 바람이 목덜미로 들어오는 것을 줄입니다. 헬멧이나 모자 안에 같이 쓸 수 있는 두께입니다."
    ],
    "search_keyword": "방한 바라클라바"
  },
  {
    "id": "anti-fog",
    "name": "소낙스 김서림 방지제 관리용품, 500ml, 1개",
    "partners_link": "https://link.coupang.com/a/iIE2GCK1TM",
    "image": "img/products/anti-fog.jpg",
    "account": "ads",
    "category": "출퇴근·차량",
    "hook": "겨울 아침 차에 오르면 앞유리에 서리는 김을 줄여 주는 코팅제입니다.",
    "summary": [
      "유리 안쪽에 뿌려 닦아 두면 수증기가 맺히는 자리가 줄어듭니다. 500ml라 한 겨울 내내 차 한 대에 쓰기 넉넉합니다."
    ],
    "search_keyword": "김서림 방지제"
  },
  {
    "id": "ice-scraper",
    "name": "깔끔조아 스크래치 없는 회전형 길이조절 차량용 성에제거기, 1개",
    "partners_link": "https://link.coupang.com/a/iIE47Fx8DY",
    "image": "img/products/ice-scraper.jpg",
    "account": "ads",
    "category": "출퇴근·차량",
    "hook": "손이 닿지 않는 앞유리 가운데까지 밀어 내는 길이조절 스크래퍼입니다.",
    "summary": [
      "손잡이 각도가 돌아가고 길이가 늘어나 차 높이에 맞춰 쓸 수 있습니다. 브러시가 함께 달려 눈과 성에를 한 번에 정리합니다."
    ],
    "search_keyword": "차량 성에제거기"
  },
  {
    "id": "sink-splash",
    "name": "달팽이리빙 퀴진드마망 실리콘 씽크대 물막이, 크림화이트, 1개",
    "partners_link": "https://link.coupang.com/a/iIEWfbNl0e",
    "image": "img/products/sink-splash.jpg",
    "account": "ads",
    "category": "주방·살림",
    "hook": "설거지할 때 튀는 물이 옷과 바닥으로 가지 않게 세우는 실리콘 판입니다.",
    "summary": [
      "하단 흡착판으로 상판에 붙여 세우고, 말랑한 실리콘 재질이라 부딪혀도 소리가 나지 않습니다. 물때가 끼면 통째로 씻어 말리면 됩니다."
    ],
    "search_keyword": "싱크대 물막이"
  },
  {
    "id": "oil-screen",
    "name": "시샘 연마제없는 스텐 다용도 기름방지망, 33cm, 1개",
    "partners_link": "https://link.coupang.com/a/iIEXV8gHw4",
    "image": "img/products/oil-screen.jpg",
    "account": "ads",
    "category": "주방·살림",
    "hook": "고기를 굽거나 튀길 때 튀는 기름을 막아 두는 스테인리스 망입니다.",
    "summary": [
      "촘촘한 망이라 김은 빠져나가고 기름은 막아 줍니다. 손잡이가 달려 있어 조리 중에도 집기 편합니다."
    ],
    "search_keyword": "기름튐 방지망"
  },
  {
    "id": "drain-filter",
    "name": "코멧 싱크대 배수구 거름망, 500개",
    "partners_link": "https://link.coupang.com/a/iIFajZuk5A",
    "image": "img/products/drain-filter.jpg",
    "account": "take",
    "category": "주방·살림",
    "hook": "배수구에 끼워 음식물 찌꺼기와 머리카락을 한 번에 걸러 내는 망입니다.",
    "summary": [
      "한 장씩 끼워 쓰고 가득 차면 그대로 버리면 됩니다. 500장이라 몇 달은 다시 사러 가지 않아도 됩니다."
    ],
    "search_keyword": "배수구 거름망"
  },
  {
    "id": "diatomite-mat",
    "name": "코멧 홈 빨아쓰는 규조토 발매트, 베이지 타원, 1개",
    "partners_link": "https://link.coupang.com/a/iIE0nWcz24",
    "image": "img/products/diatomite-mat.jpg",
    "account": "take",
    "category": "욕실·위생",
    "hook": "욕실에서 나와 젖은 발을 한 번만 디디면 물기를 빨아들이는 발매트입니다.",
    "summary": [
      "규조토가 섞인 연질 소재라 돌처럼 단단하지 않고 발에 부드럽습니다. 빨아서 말릴 수 있어 눅눅한 냄새 걱정이 덜합니다."
    ],
    "search_keyword": "규조토 발매트"
  },
  {
    "id": "mold-gel",
    "name": "홈스타 바르는 곰팡이 싹 세정제, 120ml, 2개",
    "partners_link": "https://link.coupang.com/a/iIE8F8LqqO",
    "image": "img/products/mold-gel.jpg",
    "account": "take",
    "category": "욕실·위생",
    "hook": "줄눈과 실리콘 틈에 발라 두면 문지르지 않아도 곰팡이가 들뜨는 젤형 세정제입니다.",
    "summary": [
      "흘러내리지 않는 젤이라 벽면에도 붙어 있습니다. 뾰족한 노즐로 좁은 틈에 바로 짜 넣을 수 있습니다."
    ],
    "search_keyword": "곰팡이 제거 젤"
  },
  {
    "id": "fish-cake",
    "name": "효성어묵 부산옛날어묵 종합 (냉동), 1kg, 1개",
    "partners_link": "https://link.coupang.com/a/iCGPZ9URPM",
    "image": "img/products/fish-cake.jpg",
    "account": "take",
    "category": "겨울간식·식품",
    "hook": "냉동실에 두고 국이나 떡볶이에 꺼내 쓰는 종합 어묵입니다.",
    "summary": [
      "사각·봉·야채 어묵이 섞여 있어 요리마다 골라 쓰기 좋습니다. 1kg이라 몇 번 나눠 먹을 양입니다."
    ],
    "search_keyword": "효성어묵 종합"
  },
  {
    "id": "hoppang",
    "name": "삼립 호빵 발효미종 단팥 + 야채, 97g, 12개입, 1세트",
    "partners_link": "https://link.coupang.com/a/iIFbUN1Zwy",
    "image": "img/products/hoppang.jpg",
    "account": "take",
    "category": "겨울간식·식품",
    "hook": "전자레인지나 찜기에 데워 겨울 저녁에 먹는 단팥·야채 호빵입니다.",
    "summary": [
      "단팥과 야채가 반씩 들어 있어 골라 먹는 재미가 있습니다. 낱개 포장이라 먹을 만큼만 데우면 됩니다."
    ],
    "search_keyword": "삼립 호빵"
  },
  {
    "id": "boongeoppang",
    "name": "비비고 단팥붕어빵 (냉동), 300g, 1개",
    "partners_link": "https://link.coupang.com/a/iIFdE5NoCO",
    "image": "img/products/boongeoppang.jpg",
    "account": "take",
    "category": "겨울간식·식품",
    "hook": "에어프라이어에 돌리면 겉은 바삭하고 속은 뜨거운 냉동 붕어빵입니다.",
    "summary": [
      "팬에 기름을 두르지 않고 에어프라이어로 데울 수 있습니다. 300g 한 봉이라 아이 간식으로 부담 없는 양입니다."
    ],
    "search_keyword": "비비고 붕어빵"
  },
  {
    "id": "hot-choco",
    "name": "미떼 핫초코 오리지날, 30g, 30개입, 1개",
    "partners_link": "https://link.coupang.com/a/iIFf8a2pjg",
    "image": "img/products/hot-choco.jpg",
    "account": "take",
    "category": "겨울간식·식품",
    "hook": "우유에 한 봉 풀면 되는 핫초코 30봉입니다.",
    "summary": [
      "개별 포장이라 한 잔씩 뜯어 타면 됩니다. 사무실이나 아이 간식으로 두고 쓰기 좋은 구성입니다."
    ],
    "search_keyword": "미떼 핫초코"
  },
  {
    "id": "music-box",
    "name": "홀리해요 크리스마스 오르골 무드등 플랫 스노우볼, 산타",
    "partners_link": "https://link.coupang.com/a/iCIEE8o6uW",
    "image": "img/products/music-box.jpg",
    "account": "take",
    "category": "홈·데코",
    "hook": "손잡이를 들면 눈이 내리고 음악이 흐르는 납작한 스노우볼입니다.",
    "summary": [
      "세워 두거나 들고 다닐 수 있는 형태라 선반과 식탁 어디에나 놓입니다. 불을 켜면 은은한 무드등으로도 쓸 수 있습니다."
    ],
    "search_keyword": "크리스마스 오르골 스노우볼"
  },
  {
    "id": "music-box-lamp",
    "name": "스네몬 오르골 오로라 무드등, 핑크화이트",
    "partners_link": "https://link.coupang.com/a/iIFhNLDGpw",
    "image": "img/products/music-box-lamp.jpg",
    "account": "take",
    "category": "홈·데코",
    "hook": "오로라 빛이 돌아가며 방 천장까지 물들이는 오르골 무드등입니다.",
    "summary": [
      "음악이 나오는 오르골에 오로라 조명이 함께 들어 있어 아이 방 취침등으로도 쓸 수 있습니다. 밝기를 낮춰 잠들 때 켜 두기 좋습니다."
    ],
    "search_keyword": "오르골 무드등"
  },
  {
    "id": "mini-tree",
    "name": "크리스마스 40cm 설레는 밤 완제 트리 풀세트 전구포함, 혼합색상",
    "partners_link": "https://link.coupang.com/a/iIFjGOaEQC",
    "image": "img/products/mini-tree.jpg",
    "account": "take",
    "category": "홈·데코",
    "hook": "꾸미는 수고 없이 꺼내 세우면 모습이 갖춰지는 40cm 미니 트리입니다.",
    "summary": [
      "장식과 전구가 이미 달려 있어 처음 트리를 두는 집도 부담이 적습니다. 40cm라 원룸이나 아이 방 책상 위에도 놓입니다."
    ],
    "search_keyword": "미니 크리스마스 트리"
  },
  {
    "id": "fleece-blanket",
    "name": "더자리 마이블랭킷 극세사 담요",
    "partners_link": "https://link.coupang.com/a/iIFk7hUsDs",
    "image": "img/products/fleece-blanket.jpg",
    "account": "take",
    "category": "홈·데코",
    "hook": "소파에 두고 무릎 덮기 좋은 극세사 담요입니다.",
    "summary": [
      "촘촘한 극세사라 가볍고 부드럽습니다. 이불 위에 한 겹 더 덮거나 차에 두고 쓰기 좋습니다."
    ],
    "search_keyword": "극세사 담요"
  },
  {
    "id": "electric-seat",
    "name": "HanilMedical 1인용 전기방석 HL-100(20), 네이비, 450 x 450 mm",
    "partners_link": "https://link.coupang.com/a/iJZa0xMjV6",
    "image": "img/products/electric-seat.jpg",
    "account": "take",
    "category": "잠자리",
    "hook": "소파나 의자에 앉아 있는 동안 엉덩이부터 따뜻하게 데우는 1인용 전기방석입니다.",
    "summary": [
      "전원을 넣으면 열선이 골고루 퍼지고, 쓰지 않을 때는 돌돌 말아 두면 됩니다. 등받이 의자나 소파 한쪽에 깔아 두기 좋은 크기입니다."
    ],
    "search_keyword": "전기방석 1인용"
  },
  {
    "id": "k2-gloves",
    "name": "K2 세이프티 히트플렉스 니트 장갑, 1세트, 블랙",
    "partners_link": "https://link.coupang.com/a/iJZgIrr1O0",
    "image": "img/products/k2-gloves.jpg",
    "account": "ads",
    "category": "출퇴근길",
    "hook": "자전거 손잡이나 버스 손잡이를 잡는 아침, 손끝이 시린 것을 덜어 주는 니트 장갑입니다.",
    "summary": [
      "니트로 짠 장갑이라 손등에 닿는 감촉이 부드럽고, 두께가 두껍지 않아 가방이나 코트 주머니에 넣어 두기 좋습니다."
    ],
    "search_keyword": "K2 방한장갑"
  },
  {
    "id": "kimchi",
    "name": "종가 포기김치, 2.3kg, 1개",
    "partners_link": "https://link.coupang.com/a/iJZojEkCYe",
    "image": "img/products/kimchi.jpg",
    "account": "take",
    "category": "겨울 야식",
    "hook": "김장을 직접 담그지 않는 집에서 겨울 내내 꺼내 먹기 좋은 포기김치입니다.",
    "summary": [
      "한 통으로 와서 김치통에 옮겨 담아 두면 됩니다. 국이나 찌개에 넣을 때도 한 포기씩 꺼내 쓰기 좋습니다."
    ],
    "search_keyword": "종가 포기김치"
  },
  {
    "id": "radiator",
    "name": "신일 컴팩트 라디에이터 5핀, SER-D5500KP",
    "partners_link": "https://link.coupang.com/a/iJZvbm24om",
    "image": "img/products/radiator.jpg",
    "account": "take",
    "category": "겨울 준비",
    "hook": "보일러를 켜기엔 아까운 날, 방 하나만 데우는 전기 라디에이터입니다.",
    "summary": [
      "기름이 도는 방식이라 바람이 일지 않고 소리가 크지 않습니다. 바퀴가 달려 있어 방과 거실 사이를 옮겨 가며 쓸 수 있습니다."
    ],
    "search_keyword": "신일 라디에이터"
  },
  {
    "id": "tokyotomi-heater",
    "name": "토요토미 팬히터 LC-L53 풀세트 (국내 정품 A/S 가능) 도요토미, BLACK",
    "partners_link": "https://link.coupang.com/a/iJZycVPxSu",
    "image": "img/products/tokyotomi-heater.jpg",
    "account": "ads",
    "category": "별별템",
    "hook": "캠핑하는 사람들이 먼저 찾는 일본식 팬히터입니다. 쿠팡에 정품으로 올라와 있습니다.",
    "summary": [
      "기름을 넣고 쓰는 난로라 환기에 신경 써야 하고, 무게가 있어 한 번 자리를 잡으면 거실 한쪽에 두고 쓰게 됩니다."
    ],
    "search_keyword": "토요토미 팬히터"
  },
  {
    "id": "drone",
    "name": "DJI Neo 2 플라이 모어 콤보 드론, 혼합색상, 1세트",
    "partners_link": "https://link.coupang.com/a/iJZCB6mDYq",
    "image": "img/products/drone.jpg",
    "account": "ads",
    "category": "별별템",
    "hook": "손바닥만 한 크기로 하늘 사진을 남기는 드론입니다. 쿠팡 가전 코너에 이런 것도 있습니다.",
    "summary": [
      "본체와 조종기, 배터리가 함께 오는 구성입니다. 겨울 여행에서 위에서 찍은 사진을 남기고 싶을 때 눈에 들어오는 세트입니다."
    ],
    "search_keyword": "DJI Neo 2 드론"
  },
  {
    "id": "premiere-projector",
    "name": "삼성전자 The Premiere 프로젝터 웜 화이트 254~330cm 방문설치, SP-LPDU9SAXXKR",
    "partners_link": "https://link.coupang.com/a/iJZGHOUWlM",
    "image": "img/products/premiere-projector.jpg",
    "account": "ads",
    "category": "별별템",
    "hook": "벽에 붙여 두고 쓰는 삼성 초단초점 프로젝터입니다. 장바구니에 담아 둘 수 있는 가전으로 쿠팡에 올라와 있습니다.",
    "summary": [
      "방문 설치로 배송되는 모델이라 자리를 잡아 주는 과정까지 포함되어 있습니다. 거실 벽 한 면을 화면으로 쓰고 싶을 때 비교해 볼 만한 상품입니다."
    ],
    "search_keyword": "삼성 더 프리미어 프로젝터"
  },
  {
    "id": "frost-cover",
    "name": "카템 3중 차단 마그네틱 성에방지 커버, 전차종, 1세트",
    "partners_link": "https://link.coupang.com/a/iLFf9cx10m",
    "image": "img/products/frost-cover.jpg",
    "account": "take",
    "category": "출퇴근길",
    "hook": "아침에 성에를 긁는 대신 밤에 덮어 두는 앞유리 커버입니다.",
    "summary": [
      "자석과 문틈 고정 방식이라 덮어 두고 아침에 걷어 내면 됩니다. 사이드미러까지 함께 덮는 구성이라 유리에 앉은 성에를 밀어 내는 시간을 줄이는 쪽입니다."
    ],
    "search_keyword": "차량 성에방지커버"
  },
  {
    "id": "heating-vest",
    "name": "에쉬울프 USB 발열조끼 스마트 온열조끼, DR013",
    "partners_link": "https://link.coupang.com/a/iLFuzgsa9k",
    "image": "img/products/heating-vest.jpg",
    "account": "take",
    "category": "출퇴근길",
    "hook": "보조배터리를 꽂으면 앞판과 뒷판이 데워지는 조끼입니다.",
    "summary": [
      "패딩 안에 껴입거나 단독으로 입고 다닐 수 있는 두께입니다. USB 연결 방식이라 쓰는 보조배터리 용량에 따라 사용 시간이 달라지고, KC 인증 표기가 있는지 확인해 두는 편이 좋습니다."
    ],
    "search_keyword": "USB 발열조끼"
  },
  {
    "id": "electric-grill",
    "name": "홈플래닛 반반 멀티 전기그릴(개별 온도 조절), AD-SK18",
    "partners_link": "https://link.coupang.com/a/iLEWQmy5U4",
    "image": "img/products/electric-grill.jpg",
    "account": "take",
    "category": "연말 홈파티",
    "hook": "한쪽은 굽고 한쪽은 끓이는 반반 상판 전기그릴입니다.",
    "summary": [
      "좌우 온도를 따로 조절해 고기와 국물 요리를 같이 올려 둘 수 있습니다. 상판이 넓어 식탁 가운데에 두고 여러 명이 둘러앉기 좋습니다."
    ],
    "search_keyword": "반반 전기그릴"
  },
  {
    "id": "fishbread-maker",
    "name": "위즈웰 간식 메이커 3종 세트 붕어빵 + 와플 + 샌드위치, WSW-6137",
    "partners_link": "https://link.coupang.com/a/iLE0sQqZEq",
    "image": "img/products/fishbread-maker.jpg",
    "account": "take",
    "category": "겨울 간식",
    "hook": "플레이트를 바꿔 끼우면 붕어빵, 와플, 샌드위치가 되는 전기 메이커입니다.",
    "summary": [
      "붕어빵틀과 와플판, 샌드위치판이 한 세트로 옵니다. 아이와 같이 반죽을 붓고 기다리는 겨울 방학 간식용입니다."
    ],
    "search_keyword": "붕어빵 메이커"
  },
  {
    "id": "home-sauna",
    "name": "[휴먼사우나] 로벤스 편백나무+히노끼 스톤찜질+좌훈+족욕찜질 원적외선 반신욕기, LPH-300",
    "partners_link": "https://link.coupang.com/a/iLFmqwxj0C",
    "image": "img/products/home-sauna.jpg",
    "account": "ads",
    "category": "별별템",
    "hook": "집에 들이는 1인용 반신욕기입니다. 편백나무 안에서 앉는 자리와 스톤을 데우는 구조입니다.",
    "summary": [
      "원적외선 방식이라 물을 끓이지 않고 앉는 자리와 스톤을 데웁니다. 크기와 무게가 있어 둘 자리와 문 폭을 먼저 재 보고 정하는 편이 좋습니다."
    ],
    "search_keyword": "1인용 가정용 사우나"
  },
  {
    "id": "snow-blower",
    "name": "클라빈다 충전식 무선 전동 리튬 배터리 제설기 소형 다기능 휴대용 가정용 고출력 접이식, 1세트",
    "partners_link": "https://link.coupang.com/a/iLF6x1Pvky",
    "image": "img/products/snow-blower.jpg",
    "account": "ads",
    "category": "별별템",
    "hook": "눈이 온 날 아침, 삽 대신 미는 충전식 제설기입니다.",
    "summary": [
      "충전 배터리로 눈을 밀어 내는 소형 제설기입니다. 배터리 포함 여부와 날개 폭이 값을 가릅니다. 같은 검색에 손에 드는 송풍기형이 섞여 나오니 상품 구분을 확인해 보세요."
    ],
    "search_keyword": "무선 제설기"
  },
  {
    "id": "mini-dehumidifier",
    "name": "EXTEDRG 제습기 2.8L 강력제습 가정용 저소음 원룸 미니 제습기, D9",
    "partners_link": "https://link.coupang.com/a/iNjEeRx34C",
    "image": "img/products/mini-dehumidifier.jpg",
    "account": "take",
    "category": "결로·습기",
    "hook": "창틀에 물방울이 맺히는 날, 방 안 물을 물통으로 모으는 작은 제습기입니다.",
    "summary": [
      "옷장이나 욕실처럼 좁은 자리에 두는 2.8L 소형입니다. 물통이 차면 표시가 뜨고, 습도가 내려가면 스스로 멈춥니다."
    ],
    "search_keyword": "미니 제습기"
  },
  {
    "id": "dehumidifier-12l",
    "name": "롯데알미늄 제습기 12L, LDH-7000N",
    "partners_link": "https://link.coupang.com/a/iNjUwx2rpA",
    "image": "img/products/dehumidifier-12l.jpg",
    "account": "take",
    "category": "결로·습기",
    "hook": "빨래를 널어 둔 방의 물을 하루 12L까지 빼내는 컴프레서 제습기입니다.",
    "summary": [
      "일일 제습량 12L, 사용면적 약 10평으로 표기된 모델입니다. 물통은 2L이고 연속배수 호스를 연결할 수 있어 물 비우는 일을 줄일 수 있습니다."
    ],
    "search_keyword": "가정용 제습기 12L"
  },
  {
    "id": "winter-duvet",
    "name": "코멧 홈 양면 극세사 솔리드 차렵이불",
    "partners_link": "https://link.coupang.com/a/iNjFeUXyNw",
    "image": "img/products/winter-duvet.jpg",
    "account": "take",
    "category": "겨울 침구",
    "hook": "커버를 씌우지 않고 바로 덮는 겨울 극세사 차렵이불입니다.",
    "summary": [
      "솜이 안에 누벼 있어 이불커버 없이 쓰고, 빨래도 한 장만 하면 됩니다. 앞뒤 색이 달라 뒤집어 덮을 수 있습니다."
    ],
    "search_keyword": "극세사 차렵이불"
  },
  {
    "id": "bathroom-heater",
    "name": "한경희생활과학 PTC 온풍기 욕실 난방기 스탠드 벽걸이 전기히터, HAAN-4000(블랙)",
    "partners_link": "https://link.coupang.com/a/iNkaGmHDW0",
    "image": "img/products/bathroom-heater.jpg",
    "account": "take",
    "category": "욕실 난방",
    "hook": "욕실 벽에 걸거나 세워 두고 샤워 전에 켜 두는 온풍기입니다.",
    "summary": [
      "벽에 걸거나 세워 두는 겸용형이라 좁은 욕실에서 놓을 자리를 골라 쓸 수 있습니다. 물이 닿는 곳에 두는 제품이라 설치 위치와 전원은 설명서를 따라 확인해 두는 편이 좋습니다."
    ],
    "search_keyword": "욕실 온풍기"
  },
  {
    "id": "foot-spa",
    "name": "이노크아든 사파이어 스파 족욕기, FM-505, 화이트",
    "partners_link": "https://link.coupang.com/a/iNjK48KKbs",
    "image": "img/products/foot-spa.jpg",
    "account": "take",
    "category": "겨울 발 보온",
    "hook": "물을 받아 온도를 맞춰 두는 습식 족욕기입니다.",
    "summary": [
      "온도를 정해 두면 맞춰 가열하고, 바닥에 지압 롤러와 거품 기능이 있습니다. 고정형이라 둘 자리와 콘센트 위치를 먼저 정하는 편이 좋습니다."
    ],
    "search_keyword": "가정용 족욕기"
  },
  {
    "id": "neck-massager",
    "name": "제스파 플러스 목어깨 등 허리 마사지기, ZP187, 퍼플",
    "partners_link": "https://link.coupang.com/a/iNjJRe2DPU",
    "image": "img/products/neck-massager.jpg",
    "account": "take",
    "category": "겨울 몸풀기",
    "hook": "목에 걸치고 기대서 쓰는 목·어깨 마사지기입니다.",
    "summary": [
      "4개의 안마볼이 돌아가며 방향을 바꾸고, 온열을 함께 켤 수 있습니다. 15분이 지나면 스스로 꺼지고, 차량용 전원선이 함께 들어 있습니다."
    ],
    "search_keyword": "목어깨 마사지기"
  },
  {
    "id": "filter-shower",
    "name": "코멧 홈 파워수압 필터 샤워기 본품 + 필터 2개입, 실버",
    "partners_link": "https://link.coupang.com/a/iNjGtwDojc",
    "image": "img/products/filter-shower.jpg",
    "account": "take",
    "category": "욕실",
    "hook": "헤드 안쪽 필터로 물을 한 번 거르는 샤워기입니다.",
    "summary": [
      "본체와 필터 2개가 한 세트로 옵니다. 필터는 2~3개월 주기로 갈아 끼우고, 수압을 올려 주는 판이 들어 있습니다."
    ],
    "search_keyword": "필터 샤워기"
  },
  {
    "id": "firewood-stove",
    "name": "아웃도어웍스 화목난로, OW200",
    "partners_link": "https://link.coupang.com/a/iNjIJWmvVk",
    "image": "img/products/firewood-stove.jpg",
    "account": "ads",
    "category": "별별템",
    "hook": "장작을 넣고 불을 보는 캠핑용 화목난로입니다.",
    "summary": [
      "연통과 함께 세팅하는 스테인리스 난로입니다. 불을 쓰는 제품이라 실내에서는 환기와 설치 자리, 소방 안전을 먼저 확인해야 합니다."
    ],
    "search_keyword": "캠핑 화목난로"
  },
  {
    "id": "thermos-lunchbox",
    "name": "써모스 일체형 대용량 보온도시락 + 보온백 + 수저 세트, 샌드베이지, 1개",
    "partners_link": "https://link.coupang.com/a/iNGqzfSzhA",
    "image": "img/products/thermos-lunchbox.jpg",
    "account": "take",
    "category": "주방·도시락",
    "hook": "국물이나 반찬이 식지 않게 싸 가는 보온도시락입니다.",
    "summary": [
      "1500ml를 네 단으로 나눠 담는 일체형이고 보온백과 수저가 같이 옵니다. 보냉도 되는 제품으로 표기돼 있습니다."
    ],
    "search_keyword": "써모스 보온도시락"
  },
  {
    "id": "advent-calendar",
    "name": "오리온 크리스마스 어드벤트 캘린더 과자세트, 9종, 1세트",
    "partners_link": "https://link.coupang.com/a/iNGrtQRPe8",
    "image": "img/products/advent-calendar.jpg",
    "account": "myeongjanae",
    "category": "크리스마스",
    "hook": "12월에 하루씩 열어 보는 크리스마스 달력입니다.",
    "summary": [
      "과자 9종이 들어 있는 혼합 세트입니다. 상자 겉면에 작은 문들이 있어 12월에 하나씩 열어 보는 방식입니다."
    ],
    "search_keyword": "어드벤트 캘린더"
  },
  {
    "id": "heating-tent",
    "name": "따수미 패브릭 난방텐트 3인용",
    "partners_link": "https://link.coupang.com/a/iNGssAUnfM",
    "image": "img/products/heating-tent.jpg",
    "account": "take",
    "category": "겨울 난방·방풍",
    "hook": "침대 위에 씌워 방 하나만 덥히는 난방텐트입니다.",
    "summary": [
      "지퍼로 여닫고 바닥이 없는 구조라 침대 위에 덮어 쓰는 방식입니다. 3인용(킹) 크기로 나온 제품입니다."
    ],
    "search_keyword": "패브릭 난방텐트"
  },
  {
    "id": "baby-wipes",
    "name": "코멧 오리지널 유아용 아기물티슈 캡형, 100매입",
    "partners_link": "https://link.coupang.com/a/iNGtoaNmy4",
    "image": "img/products/baby-wipes.jpg",
    "account": "myeongjanae",
    "category": "생필품",
    "hook": "한 장씩 뽑아 쓰는 아기물티슈입니다.",
    "summary": [
      "캡을 눌러 한 장씩 뽑는 캡형 100매입입니다. 상품평이 49만 개가 넘고 한 달에 10만 명 이상이 산 상품입니다."
    ],
    "search_keyword": "코멧 아기물티슈"
  },
  {
    "id": "kids-balaclava",
    "name": "우드피카 유아용 패치 바라클라바 넥워머",
    "partners_link": "https://link.coupang.com/a/iNGukGGgi4",
    "image": "img/products/kids-balaclava.jpg",
    "account": "take",
    "category": "겨울 방한",
    "hook": "목부터 머리까지 한 번에 덮는 아동용 넥워머입니다.",
    "summary": [
      "단추로 여미는 아크릴 니트라 목도리처럼 풀리지 않습니다. 아동·유아용으로 나온 제품입니다."
    ],
    "search_keyword": "유아 바라클라바"
  },
  {
    "id": "socks-5set",
    "name": "퍼니스코 여성 겨울 수면 양말 5종 SET",
    "partners_link": "https://link.coupang.com/a/iO8Bl4KKOa",
    "image": "img/products/socks-5set.jpg",
    "account": "take",
    "category": "겨울 침구·수면",
    "hook": "밤에 발이 시려 양말을 신고 자는 집에 두는 무압박 수면양말입니다.",
    "summary": [
      "밴딩을 세게 조이지 않아 신고 자도 발목에 자국이 덜 남습니다. 다섯 켤레가 한 세트라 빨아 가며 돌려 신기 좋습니다."
    ],
    "search_keyword": "여성 수면양말 5종"
  },
  {
    "id": "socks-4set",
    "name": "이지하임 4켤레 털빠짐없는 편안한 무압박 남녀공용 수면양말 세트",
    "partners_link": "https://link.coupang.com/a/iO8FgfqG8O",
    "image": "img/products/socks-4set.jpg",
    "account": "take",
    "category": "겨울 침구·수면",
    "hook": "수면양말을 신고 나면 털이 묻어 나와 고민이던 집에 두는 네 켤레 세트입니다.",
    "summary": [
      "상품명에 털 빠짐을 줄인 소재로 표기돼 있습니다. 남녀공용으로 나와 온 가족이 나눠 신을 수 있습니다."
    ],
    "search_keyword": "무압박 수면양말 4켤레"
  },
  {
    "id": "hotpack-attach",
    "name": "하루온 붙이는 핫팩 50g 10개입, 2개",
    "partners_link": "https://link.coupang.com/a/iO8CicdLVc",
    "image": "img/products/hotpack-attach.jpg",
    "account": "take",
    "category": "겨울 방한",
    "hook": "옷 안쪽에 붙여 두면 손에 쥐지 않아도 등과 배가 따뜻한 핫팩입니다.",
    "summary": [
      "10개입 봉지 두 개로 오는 구성입니다. 상품평이 5만 2천 개가 넘고, 최근 한 달 사이 7천 명 이상이 산 것으로 표시돼 있습니다."
    ],
    "search_keyword": "하루온 붙이는 핫팩"
  },
  {
    "id": "dish-soap",
    "name": "순샘 구연산 자몽향 주방세제 리필, 1.4L, 3개",
    "partners_link": "https://link.coupang.com/a/iO8DtBKacu",
    "image": "img/products/dish-soap.jpg",
    "account": "take",
    "category": "살림·세제",
    "hook": "설거지할 때 기름이 잘 빠지지 않아 세제를 더 짜게 되는 집에 두는 리필입니다.",
    "summary": [
      "1.4L 리필 세 통 구성입니다. 구연산이 들어간 자몽향 세제로 표기돼 있습니다."
    ],
    "search_keyword": "순샘 주방세제 리필"
  },
  {
    "id": "drying-rack",
    "name": "코멧 홈 접이식 대형 빨래건조대, 그레이, 1개",
    "partners_link": "https://link.coupang.com/a/iO8Eo2uBq0",
    "image": "img/products/drying-rack.jpg",
    "account": "take",
    "category": "살림·빨래",
    "hook": "겨울엔 밖에 못 널어 거실에 건조대를 펴 두게 되는 집에 두는 접이식 건조대입니다.",
    "summary": [
      "쓰지 않을 때는 접어 세워 둘 수 있습니다. 상품평이 2만 2천 개가 넘는 상품입니다."
    ],
    "search_keyword": "코멧 접이식 빨래건조대"
  },
  {
    "id": "dyson-airwrap",
    "name": "다이슨 에어랩 id 멀티 스타일러 앤 드라이어, 161845-01, 블루 + 코퍼",
    "partners_link": "https://link.coupang.com/a/iO8Gt4yyfk",
    "image": "img/products/dyson-airwrap.jpg",
    "account": "ads",
    "category": "뷰티·가전",
    "hook": "겨울 외출 전에 머리를 말리고 모양까지 잡고 싶다는 말이 나올 때 눈에 들어오는 기계입니다.",
    "summary": [
      "본체와 여러 가지 헤드가 함께 오는 구성입니다. 머리를 말리는 일과 모양을 잡는 일을 한 자리에서 끝내는 쪽입니다."
    ],
    "search_keyword": "다이슨 에어랩"
  },
  {
    "id": "massage-chair",
    "name": "제스파 컴포르테 안마의자 + 전용 러그 방문설치, ZPC2034(안마의자), ZP540(러그), 퓨어화이트",
    "partners_link": "https://link.coupang.com/a/iO8HqggG16",
    "image": "img/products/massage-chair.jpg",
    "account": "ads",
    "category": "가전·설치",
    "hook": "퇴근하고 소파 대신 앉겠다고 하는 자리에 놓는 전신 안마의자입니다.",
    "summary": [
      "안마의자와 전용 러그가 함께 오고 방문 설치로 배송됩니다. 크기와 무게가 있어 둘 자리와 문 폭을 먼저 재 보고 정하는 편이 좋습니다."
    ],
    "search_keyword": "제스파 컴포르테 안마의자"
  },
  {
    "id": "homstar-pink",
    "name": "홈스타 핑크파워 욕실 찌든때 클리너, 750ml, 2개",
    "partners_link": "https://link.coupang.com/a/iQCW1zM8US",
    "image": "img/products/homstar-pink.jpg",
    "account": "take",
    "category": "욕실·위생",
    "hook": "욕실 타일과 줄눈의 찌든 때에 뿌려 두는 거품형 세정제입니다.",
    "summary": [
      "분사대가 달린 750ml 두 통 구성입니다. 거품을 붙여 두었다가 물로 헹구는 방식으로 쓰고, 욕실과 주방에 한 통씩 나눠 둘 수 있습니다."
    ],
    "search_keyword": "홈스타 핑크파워",
    "evidence": {
      "shorts_url": "https://www.youtube.com/shorts/ln-Zo04IiU4",
      "views": 5600000,
      "uploaded": "2026-08-12",
      "store_word": "다이소",
      "why_coupang": "영상에서 이 제품은 다이소보다 쿠팡이 더 저렴하다고 짚었습니다. 두 통 구성으로 한 번에 받는 쪽입니다."
    }
  },
  {
    "id": "shower-rod-shelf",
    "name": "물빠짐 샤워봉 거치 선반 + 보조캡 3종 + 방수테이프 세트, 화이트, 1세트",
    "partners_link": "https://link.coupang.com/a/iQC1PH3waW",
    "image": "img/products/shower-rod-shelf.jpg",
    "account": "take",
    "category": "욕실 수납",
    "hook": "샤워봉에 걸어 물이 빠지는 자리에 두는 선반입니다.",
    "summary": [
      "샤워봉에 걸어 고정하는 방식이라 타공 없이 설치합니다. 바닥이 물빠짐 구조라 샴푸병 밑에 물이 고이지 않고, 보조캡과 방수테이프가 함께 옵니다."
    ],
    "search_keyword": "샤워봉 선반",
    "evidence": {
      "shorts_url": "https://www.youtube.com/shorts/ln-Zo04IiU4",
      "views": 5600000,
      "uploaded": "2026-08-12",
      "store_word": "다이소",
      "why_coupang": "샤워봉에 거는 방식이라 타공 없이 쓰고, 보조캡과 방수테이프까지 한 세트로 옵니다."
    }
  },
  {
    "id": "bathroom-shelf-set",
    "name": "다용도 무타공 욕실 수납선반 6종 세트 일자형 드라이기 거치대 비누받침대 칫솔걸이, 화이트, 1세트",
    "partners_link": "https://link.coupang.com/a/iQC5PCoQuq",
    "image": "img/products/bathroom-shelf-set.jpg",
    "account": "take",
    "category": "욕실 수납",
    "hook": "못을 쓰지 않고 붙이는 욕실 수납 6종 세트입니다.",
    "summary": [
      "일자형 선반과 비누받침, 칫솔걸이, 드라이기 거치대를 한 세트로 묶은 구성입니다. 물이 빠지는 구조라 세면대 옆에 두기 좋습니다."
    ],
    "search_keyword": "무타공 욕실선반 세트",
    "evidence": {
      "shorts_url": "https://www.youtube.com/shorts/ln-Zo04IiU4",
      "views": 5600000,
      "uploaded": "2026-08-12",
      "store_word": "다이소",
      "why_coupang": "6종을 한 세트로 묶어 욕실 수납을 한 번에 맞추는 구성입니다."
    }
  },
  {
    "id": "kobukchip-sanghu",
    "name": "오리온 꼬북칩 얼얼한 샹궈맛, 102g, 12개",
    "partners_link": "https://link.coupang.com/a/iQESmpr2vQ",
    "image": "img/products/kobukchip-sanghu.jpg",
    "account": "ads",
    "category": "편의점 간식·과자",
    "hook": "편의점에서 한 봉씩 집어 오던 매운 과자를 열두 봉 한 번에 받는 구성입니다.",
    "summary": [
      "샹궈 향과 얼얼한 매운맛이 도는 102g 봉입니다. 열두 봉이라 야식이나 간식으로 하나씩 꺼내 먹기 좋고, 편의점에 들러 낱봉으로 사 모으는 일이 줄어듭니다. 신상이라 상품평은 아직 적습니다."
    ],
    "search_keyword": "꼬북칩 얼얼한 샹궈맛",
    "evidence": {
      "shorts_url": "https://www.youtube.com/shorts/x02aTqykcHY",
      "views": 104537,
      "uploaded": "2026-11-05",
      "store_word": "편의점",
      "why_coupang": "편의점에서 낱봉으로 집어 오는 102g을 열두 봉 묶음으로 받습니다. 신상이라 상품평이 적어 리뷰 인용 줄은 빼고 구성만 쓰는 편이 좋습니다."
    }
  },
  {
    "id": "abc-choco-187",
    "name": "롯데웰푸드 ABC 초콜릿, 187g, 3개",
    "partners_link": "https://link.coupang.com/a/iQEVKNmeo8",
    "image": "img/products/abc-choco-187.jpg",
    "account": "ads",
    "category": "간식·초콜릿",
    "hook": "마트에서 한 봉씩 사 오던 ABC 초콜릿을 세 봉 묶어 받는 구성입니다.",
    "summary": [
      "187g 봉지 세 개로 옵니다. 책상 서랍이나 가방에 나눠 두고 하나씩 꺼내 먹기 좋고, 로켓배송으로 다음 날 도착합니다."
    ],
    "search_keyword": "롯데 ABC 초콜릿 187g",
    "evidence": {
      "shorts_url": "https://www.youtube.com/shorts/ztY8I1H1tVI",
      "views": 151571,
      "uploaded": "2026-11-11",
      "store_word": "마트",
      "why_coupang": "영상은 마트 신상 ABC 소프트밀크 187g 한 봉을 소개합니다. 쿠팡에서는 같은 187g 봉을 세 개 묶음으로 받고 로켓배송으로 다음 날 옵니다."
    }
  },
  {
    "id": "ediya-toffe-nut",
    "name": "이디야 비니스트 토피넛 라떼분말, 20g, 30개입, 1개",
    "partners_link": "https://link.coupang.com/a/iQEYy7kS3E",
    "image": "img/products/ediya-toffe-nut.jpg",
    "account": "take",
    "category": "겨울 음료·커피",
    "hook": "코스트코에서 상자째 사 오던 토피넛 라떼 스틱을 서른 봉으로 받는 구성입니다.",
    "summary": [
      "20g 스틱 30개입 한 상자입니다. 뜨거운 물에 한 봉 풀면 되고 상품평이 8천 개가 넘습니다. 코스트코에 가지 않아도 로켓배송으로 다음 날 도착합니다."
    ],
    "search_keyword": "이디야 토피넛 라떼",
    "evidence": {
      "shorts_url": "https://www.youtube.com/shorts/kJlODeg5_hQ",
      "views": 125233,
      "uploaded": "2026-11-19",
      "store_word": "코스트코",
      "why_coupang": "영상은 코스트코에서 이디야 토피넛 라떼 한 상자를 장바구니에 담습니다. 쿠팡 같은 30개입 상자가 할인가로 올라와 있고, 회원이 아니어도 다음 날 도착합니다."
    }
  }
]
```
