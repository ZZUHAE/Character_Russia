---
type: MOC
tags: [MOC, 집필]
description: "집필 레이어(80_집필 설계 문서)와 원고(90_원고 회차)의 색인. 회차 진행 현황·스레드·아크를 한 장에서 조망한다."
modified: 2026-07-11
---

# ✒️ 집필 MOC — 「북극성 아래」

> 소설 「북극성 아래」(제목 확정 2026-07-11) 레이어의 입구. 헌법: [[_집필_규칙]] · 문체: [[_문체_바이블]] → [[세계관_허브]]

## 설계 문서
- 규칙: [[_집필_규칙]](헌법) · [[_문체_바이블]](문체) · [[_검수_체크리스트]](확정 게이트)
- 톤·구조: [[_v3_설계서]](톤 계약 §2 · 권력 이양 사다리 §9) · [[_전체_구조_설계]](43화 초점 분포·연쇄·착지)
- 플롯 3층: [[플롯_아웃라인]](큰그림) · [[1부_플롯_v3]]·[[2부_플롯_v3]]·[[3부_플롯_v3]](부 블록) · [[작중_타임라인]]
- 스레드: [[러시아_내정]] · [[동아시아]] · [[동부전선]]
- 질감: [[_고증_바이블]] · 세계 확정사실: [[집필_확정_사실]] · 설계 연표: [[전체_연표]]
- 원고 규칙: [[_원고_안내]]

## 📖 1기 「북극성 아래」 — 회차 목록
```dataview
TABLE status AS "상태", when AS "작중 시점", pov AS "초점", description AS "요약"
FROM "90_원고/1기_북극성_아래"
WHERE type = "원고"
SORT file.name ASC
```

## 📊 1기 집필 현황
```dataview
TABLE length(rows) AS "회차 수"
FROM "90_원고/1기_북극성_아래"
WHERE type = "원고"
GROUP BY status
```

## ✒️ 2기 「원과 루블」 (1925)
- 설계: [[_작품_규칙]] · [[플롯_아웃라인_원과루블]] · [[인물_명부]] · 원장: [[집필_확정_사실_원과루블]]
```dataview
TABLE status AS "상태", when AS "작중 시점", pov AS "초점", description AS "요약"
FROM "90_원고/2기_원과_루블"
WHERE type = "원고"
SORT file.name ASC
```

## 🧵 스레드 · 아크
```dataview
TABLE status AS "상태", description AS "요약"
FROM "80_집필"
WHERE type = "집필"
SORT file.folder ASC, file.name ASC
```

## 🔍 무결성 — description 누락 (비어 있어야 정상)
```dataview
LIST
FROM "80_집필" OR "90_원고"
WHERE type != "MOC" AND (!description OR description = "")
```
