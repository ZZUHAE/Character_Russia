#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""frontmatter_lint — Vault 메타데이터 계약 전수 검사.

근거 문서: _템플릿/_frontmatter_표준.md
사용법:  python _scripts/frontmatter_lint.py       (vault 루트에서 실행)
종료코드: 위반 0 → 0, 위반 있음 → 1
"""
import os
import re
import sys

CATEGORY_MOC = {
    "00_세계관개요": "_개요_MOC",
    "10_인물": "_인물_MOC",
    "20_지역": "_지역_MOC",
    "30_세력": "_세력_MOC",
    "40_체계": "_체계_MOC",
    "50_연표사건": "_연표_MOC",
    "60_용어개념": "_용어_MOC",
}
WRITING_FOLDERS = ["80_집필", "90_원고"]  # 하위 폴더 포함 재귀 검사
WRITING_MOC = "_집필_MOC"
TYPE_ENUM = {"인물", "지역", "세력", "체계", "사건", "용어", "세계관개요", "수치모델"}
WRITING_TYPE_ENUM = {"집필", "원고"}
STATUS_ENUM = {"씨앗", "초안", "구체화", "완성"}
MANUSCRIPT_STATUS_ENUM = {"구상", "초고", "퇴고", "탈고"}
MOC_DIRS = {v: k for k, v in CATEGORY_MOC.items()}
MOC_DIRS[WRITING_MOC] = "80_집필"
REQUIRED = ["type", "status", "description", "tags", "created", "modified", "aliases", "moc"]
MOC_REQUIRED = ["type", "tags", "description", "modified"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")


def parse_frontmatter(path):
    """첫 --- 블록을 {key: raw_value_str} 로. 없으면 None."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z가-힣][A-Za-z가-힣 ]*):(.*)$", line)
        if m:
            fm[m.group(1).strip()] = m.group(2).strip()
    return fm


def is_quoted(v):
    return len(v) >= 2 and v[0] == '"' and v[-1] == '"'


def lint_file(path, folder, expected_moc, writing=False):
    issues = []
    fname = os.path.basename(path)
    is_moc = bool(re.match(r"^_.*_MOC\.md$", fname))
    fm = parse_frontmatter(path)
    if fm is None:
        return ["frontmatter 블록 없음(--- 로 시작 안 함)"]

    required = MOC_REQUIRED if is_moc else REQUIRED
    for key in required:
        if key not in fm or fm[key] == "":
            issues.append(f"필수 필드 누락: {key}")

    type_enum = WRITING_TYPE_ENUM if writing else TYPE_ENUM
    if "type" in fm:
        if is_moc:
            if fm["type"] != "MOC":
                issues.append(f"MOC 파일 type은 'MOC'여야 함: '{fm['type']}'")
        elif fm["type"] not in type_enum:
            issues.append(f"type enum 위반: '{fm['type']}'")
    if not is_moc and "status" in fm:
        # 원고는 집필 트랙(구상→탈고), 그 외는 설정 트랙(씨앗→완성)
        status_enum = MANUSCRIPT_STATUS_ENUM if fm.get("type") == "원고" else STATUS_ENUM
        if fm["status"] not in status_enum:
            issues.append(f"status enum 위반: '{fm['status']}'")

    if "description" in fm and fm["description"]:
        d = fm["description"]
        if not is_quoted(d):
            issues.append("description 큰따옴표 래핑 안 됨")
        else:
            inner = d[1:-1].strip()
            if len(inner) < 10:
                issues.append(f"description 너무 짧음/제네릭 의심: {inner!r}")
            if "[[" in inner:
                issues.append("description 안에 위키링크 대괄호 남아있음")

    for k in ("created", "modified"):
        if k in fm and fm[k] and not DATE_RE.match(fm[k]):
            issues.append(f"{k} 날짜형식(YYYY-MM-DD) 아님: '{fm[k]}'")

    if not is_moc and "moc" in fm and fm["moc"]:
        v = fm["moc"]
        if not is_quoted(v):
            issues.append("moc 위키링크 따옴표 안 됨")
        expected = expected_moc
        m = re.search(r"\[\[([^\]|#]+)", v)
        target = m.group(1).strip() if m else None
        if expected and target != expected:
            issues.append(f"moc 값 불일치: '{target}' (기대 '{expected}')")
        if target and not os.path.exists(os.path.join(MOC_DIRS.get(target, folder), target + ".md")):
            issues.append(f"moc 대상 파일 없음: {target}.md")

    # YAML 값에 따옴표 없는 위키링크
    for k, v in fm.items():
        if "[[" in v and not is_quoted(v):
            issues.append(f"'{k}' 값에 따옴표 없는 위키링크")
    return issues


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    total = ok = 0
    failed = {}
    for folder in CATEGORY_MOC:
        if not os.path.isdir(folder):
            continue
        for fname in sorted(os.listdir(folder)):
            if not fname.endswith(".md"):
                continue
            path = os.path.join(folder, fname)
            total += 1
            issues = lint_file(path, folder, CATEGORY_MOC[folder])
            if issues:
                failed[path] = issues
            else:
                ok += 1
    for root_folder in WRITING_FOLDERS:
        if not os.path.isdir(root_folder):
            continue
        for dirpath, _dirs, fnames in os.walk(root_folder):
            for fname in sorted(fnames):
                if not fname.endswith(".md"):
                    continue
                path = os.path.join(dirpath, fname)
                total += 1
                issues = lint_file(path, dirpath, WRITING_MOC, writing=True)
                if issues:
                    failed[path] = issues
                else:
                    ok += 1
    print(f"검사 {total}개 · 통과 {ok} · 위반 {len(failed)}")
    if failed:
        print("-" * 60)
        for path, issues in failed.items():
            print(f"[FAIL] {path}")
            for it in issues:
                print(f"    - {it}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
