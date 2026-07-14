---
type: MOC
tags: [MOC, 집필]
description: "집필 레이어(80_집필 설계 문서)와 원고(90_원고 회차)의 색인. 회차 진행 현황·스레드·아크를 한 장에서 조망한다."
modified: 2026-07-11
---

# ✒️ 집필 MOC — 「북극성 아래」

> 소설 「북극성 아래」(제목 확정 2026-07-11) 레이어의 입구. 헌법: [[_집필_규칙]] · 문체: [[_문체_바이블]] → [[세계관_허브]]

## 설계 문서
- 규칙: [[_집필_규칙]] · [[_문체_바이블]]
- 플롯 3층: [[플롯_아웃라인]](큰그림) · [[1부_플롯]](부 블록) · [[작중_타임라인]]
- 스레드: [[러시아_내정]] · [[동아시아]] · [[동부전선]]
- 인물 아크: [[_인물_아크_안내]] (규칙 v2 · 화약 마스터 목록) · 세계 확정사실: [[집필_확정_사실]]
- 원고 규칙: [[_원고_안내]]

## 📖 원고 — 회차 목록
```dataview
TABLE status AS "상태", when AS "작중 시점", pov AS "초점", description AS "요약"
FROM "90_원고"
WHERE type = "원고"
SORT file.name ASC
```

## 📊 집필 현황
```dataview
TABLE length(rows) AS "회차 수"
FROM "90_원고"
WHERE type = "원고"
GROUP BY status
```

## 🧵 스레드 · 아크
```dataview
TABLE status AS "상태", description AS "요약"
FROM "80_집필"
WHERE type = "집필"
SORT file.folder ASC, file.name ASC
```

## 👥 인물 아크 — stale 감시 (반영 회차 오름차순, 뒤처진 것 위로)
> 진짜 파수꾼은 lint 하드체크(`last_ep`가 최신 확정회차−5 초과 지연 = 위반). 이 표는 Obsidian판 소프트 감시.
```dataview
TABLE character AS "canon", tier AS "급", last_ep AS "반영", status AS "상태", threads AS "스레드"
FROM "80_집필/인물_아크"
WHERE type = "인물아크"
SORT last_ep ASC, tier ASC
```

## 🔍 무결성 — description 누락 (비어 있어야 정상)
```dataview
LIST
FROM "80_집필" OR "90_원고"
WHERE type != "MOC" AND (!description OR description = "")
```
