---
type: MOC
tags: [MOC, 제2기, 1925]
description: "제2기(1919~1925 입헌 체제) 레이어의 진입점이자 색인. 서술 기준 1925년 — 새 체제 6년차, 총선 2회와 첫 헌정 위기를 이미 겪은 시점의 러시아 제국을 제도 문헌 수준으로 담는다. 1기 canon(1915 동결)과 분리된 제3층."
modified: 2026-08-03
---

# 제2기 — 1925년의 러시아 제국

> **서술 기준: 1925년.** 소설 「북극성 아래」가 도달하는 입헌 전환(1918/19 명문화)의 **이후**.
> 이 레이어는 종착점 없는 살아있는 세계 위키다 — 패키지 하나가 자족적으로 닫힐 뿐, 전체 완성 선언은 없다.

## 운영 규칙 (요약)

- **참조 방향**: 제2기 → 제1기 ✅ (새 제도가 옛 근거를 인용) / 제1기 → 제2기 ❌ (시간 역행, lint 위반)
- **1기 canon(00~60)은 1915 동결 유지.** 이 레이어가 아무리 자라도 1기는 안 건드린다.
- **소설 접점 3건만 공유**: 대위임 칙령 3조 · "총리는 두마의 신임으로 정한다" · 차르 존속/명목 최고사령관. 그 외는 배경 자유.
- **인물 최소주의**: 정식 인물 노트는 핵심 소수만. 새 이름은 `_부속/` 명부에만 등재.
- **가드레일 ⓛ**: 소비에트 요소 절대 금지 — [[_고증_바이블]] §ⓛ.
- 노트 양식·frontmatter 계약: [[_frontmatter_표준]] §8. 세부(`type: 제도`) 노트는 7절 구조.

## 색인

### 헌정
```dataview
TABLE status, depth, description FROM "05_제2기/헌정" WHERE type != "MOC" SORT file.name
```

### 입법부
```dataview
TABLE status, depth, description FROM "05_제2기/입법부" WHERE type != "MOC" SORT file.name
```

### 정부
```dataview
TABLE status, depth, description FROM "05_제2기/정부" WHERE type != "MOC" SORT file.name
```

### 군주
```dataview
TABLE status, depth, description FROM "05_제2기/군주" WHERE type != "MOC" SORT file.name
```

### 지방사법
```dataview
TABLE status, depth, description FROM "05_제2기/지방사법" WHERE type != "MOC" SORT file.name
```

### 사회
```dataview
TABLE status, depth, description FROM "05_제2기/사회" WHERE type != "MOC" SORT file.name
```

### 부속 자료 (표·명부·조문)
```dataview
TABLE description FROM "05_제2기/_부속" SORT file.name
```

## 패키지 진행 현황

| 패키지 | 주제 | 상태 |
|---|---|---|
| P0 | 국가헌장 (1919) | ✅ 닫힘 (2026-08-03) — [[국가헌장_1919]] + [[국가헌장_조문]] |
| P1 | 선거 제도 + 총선 2회 | 진행 중 |
| P2 | 정당 체계 | — |
| P3 | 의회 운영 | — |
| P4 | 정부 구조 | — |
| P5 | 군주에게 남은 것 | — |
| P6 | 지방·사법 | — |
| P7 | 새 체제와 사회 | — |
| P8 | 1919~1925 정치 연대기 | — |
| 확장 | 외교·군·산업·대한제국·문화·일상… | 종착점 없음 |

## 닫아둔 것

패키지가 닫힐 때마다 "의도적으로 안 판 곳"을 여기에 선언한다. `depth` 필드가 노트 단위 선언을 겸한다.

- **P0 이연 (2026-08-03)**: `헌정_전환의_경위`(1917 대위임→1918 환수 실패→1919 명문화의 법적 연쇄 — 소설 3부와 겹치는 구간이라 034~043 확정 후가 오히려 적기) · `_부속/헌장_제정_경과표`(초안·수정·표결 기록). 필요해지면 그때 짓는다.
- **P0 내장 ❓**: 헌장 서명·공포 일자(소설 3부 몫) · 1923 무재가 발효 법률의 정체(P8에서).

## 관계
- 설계 원천: 기획서 `.omc/plans/second-era-institutional-gazetteer.md` · 스펙 `.omc/specs/deep-interview-1925-world-wiki.md`
- 1기 진입점: [[세계관_허브]] · 동결 선언: [[세계관_범위와_경계]]
- 검산 분모: [[거시_회계_시트]] · [[제국_인구와_민족_구성]]
- 양식 프로토타입: [[제국_의사결정_권한_분장]]
