#!/usr/bin/env python3
"""Valida guardrails da skill copy-humana.

Checa:
1. Presenca de hifen e travessao.
2. Cliches comuns de copy com cara de IA.
3. Excesso de exclamacoes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


BANNED_CHARS = ["-", "–", "—", "‑"]

CLICHE_PATTERNS = [
    r"\bno mundo atual\b",
    r"\bem um mundo onde\b",
    r"\bdescubra\b",
    r"\brevolucion[a-z]+\b",
    r"\btransforme sua vida\b",
    r"\bem poucos passos\b",
    r"\bsegredo que ningu[eé]m te contou\b",
    r"\bin today'?s fast[ -]?paced world\b",
    r"\bunlock the power\b",
    r"\bgame[ -]?changer\b",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Valida copy contra regras da skill")
    parser.add_argument("--file", type=str, help="Arquivo de texto para validar")
    parser.add_argument("--stdin", action="store_true", help="Ler texto da entrada padrao")
    parser.add_argument("--json", action="store_true", help="Saida em JSON")
    return parser.parse_args()


def load_text(args: argparse.Namespace) -> str:
    if args.stdin:
        return sys.stdin.read()
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    raise ValueError("Informe --file ou --stdin")


def collect_violations(text: str) -> list[dict]:
    violations: list[dict] = []
    lines = text.splitlines()

    for line_no, line in enumerate(lines, start=1):
        for char in BANNED_CHARS:
            if char in line:
                violations.append(
                    {
                        "type": "banned_char",
                        "line": line_no,
                        "match": char,
                        "snippet": line.strip()[:220],
                    }
                )

        if "!!" in line:
            violations.append(
                {
                    "type": "exclamation_noise",
                    "line": line_no,
                    "match": "!!",
                    "snippet": line.strip()[:220],
                }
            )

    lower_text = text.lower()
    for pattern in CLICHE_PATTERNS:
        for m in re.finditer(pattern, lower_text):
            line_no = lower_text[: m.start()].count("\n") + 1
            violations.append(
                {
                    "type": "ai_cliche",
                    "line": line_no,
                    "match": m.group(0),
                    "snippet": text.splitlines()[line_no - 1].strip()[:220]
                    if text.splitlines()
                    else "",
                }
            )

    return violations


def main() -> int:
    args = parse_args()
    try:
        text = load_text(args)
    except Exception as exc:
        print(f"Erro ao carregar texto: {exc}", file=sys.stderr)
        return 2

    violations = collect_violations(text)
    result = {
        "ok": len(violations) == 0,
        "violation_count": len(violations),
        "violations": violations,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if result["ok"]:
            print("OK: copy sem violacoes de guardrails.")
        else:
            print(f"Falhou: {result['violation_count']} violacoes encontradas.")
            for item in violations:
                print(
                    f"- linha {item['line']}: {item['type']} -> {item['match']} | {item['snippet']}"
                )

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
