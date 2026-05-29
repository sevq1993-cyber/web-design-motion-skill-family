#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

BAD_PATTERNS = [
    r"ScrollTrigger\.matchMedia",
    r"Max\.max",
    r"create-react-app",
    r"react-scripts",
    r"@tailwind base",
    r"<pondering>",
    r"Task tool",
    r"@latest",
    r"three\.js/r\d+",
    r"from ['\"]framer-motion['\"]",
    r"from ['\"]rive-react['\"]",
]

LINK_RE = re.compile(r"(?<![A-Za-z0-9_/-])((?:references|scripts|assets)/[A-Za-z0-9_.@+\-/]+)")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        _, raw, _ = text.split("---", 2)
    except ValueError as exc:
        raise ValueError(f"{path}: invalid frontmatter delimiter") from exc
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith(" ") and current_key:
            data[current_key] += " " + line.strip().strip('"')
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        data[current_key] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    errors: list[str] = []
    names: dict[str, Path] = {}

    for skill in sorted(SKILLS.iterdir()):
        if not skill.is_dir():
            continue
        skill_md = skill / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill}: missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text, skill_md)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        name = meta.get("name")
        description = meta.get("description")
        if not name:
            errors.append(f"{skill_md}: missing name")
        if not description:
            errors.append(f"{skill_md}: missing description")
        if name in names:
            errors.append(f"duplicate skill name {name}: {names[name]} and {skill_md}")
        if name:
            names[name] = skill_md
        for rel in sorted(set(match.rstrip(".,);:") for match in LINK_RE.findall(text))):
            if not (skill / rel).exists():
                errors.append(f"{skill_md}: missing linked resource {rel}")

    validator_path = Path(__file__).resolve()
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.resolve() == validator_path:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in BAD_PATTERNS:
            if re.search(pattern, text):
                errors.append(f"{path}: stale pattern {pattern}")

    for eval_file in (ROOT / "evals").glob("*.json"):
        try:
            json.loads(eval_file.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{eval_file}: invalid JSON: {exc}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed for {len(names)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
