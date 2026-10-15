#!/usr/bin/env python3
"""Validate every skill in this repo against the Agent Skills format rules.

Checks per skill folder under skills/:
  - folder name is lowercase kebab-case and equals the frontmatter name
  - SKILL.md exists, starts with YAML frontmatter containing name + description
  - description is 80-1024 characters (long enough to trigger, within spec)
  - body has the required sections: When to use, Workflow, Rules, Output format, Example
  - body is under 500 lines (progressive-disclosure guideline)
Also checks bundles.json covers every skill exactly once across bundles,
and that README.md mentions every skill name.

Usage: python3 scripts/validate_skills.py
Exit code 0 = all checks passed.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_SECTIONS = ["## When to use this skill", "## Workflow", "## Rules", "## Output format", "## Example"]


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def main():
    skills_dir = os.path.join(ROOT, "skills")
    names = sorted(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)))
    errors = []
    for name in names:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            errors.append(f"{name}: folder name is not kebab-case")
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            errors.append(f"{name}: SKILL.md missing")
            continue
        text = open(path).read()
        fm = parse_frontmatter(text)
        if not fm:
            errors.append(f"{name}: frontmatter missing or malformed")
            continue
        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name '{fm.get('name')}' != folder name")
        desc = fm.get("description", "")
        if not (80 <= len(desc) <= 1024):
            errors.append(f"{name}: description length {len(desc)} outside 80-1024")
        for sec in REQUIRED_SECTIONS:
            if sec not in text:
                errors.append(f"{name}: missing section '{sec}'")
        lines = text.count("\n") + 1
        if lines >= 500:
            errors.append(f"{name}: {lines} lines, must stay under 500")

    bundles = json.load(open(os.path.join(ROOT, "bundles.json")))
    flat = bundles.get("freelancer", []) + bundles.get("student", [])
    if sorted(flat) != names:
        errors.append(f"bundles.json mismatch: bundles={sorted(flat)} vs folders={names}")
    if bundles.get("all") != flat:
        errors.append("bundles.json 'all' is not freelancer + student in order")

    readme_path = os.path.join(ROOT, "README.md")
    if os.path.isfile(readme_path):
        readme = open(readme_path).read()
        for name in names:
            if name not in readme:
                errors.append(f"README.md does not mention skill '{name}'")
    else:
        errors.append("README.md missing")

    if errors:
        print(f"FAILED - {len(errors)} problem(s):")
        for e in errors:
            print(" -", e)
        return 1
    print(f"OK - {len(names)} skills validated, 0 problems.")
    for n in names:
        print(" -", n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
