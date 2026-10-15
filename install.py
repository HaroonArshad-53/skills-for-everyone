#!/usr/bin/env python3
"""Installer for Skills for Everyone.

Copies skill folders into the skills directory of your AI agent.
Standard Agent Skills format (SKILL.md) - one install works across tools.

Examples:
    python3 install.py --tool claude --bundle freelancer
    python3 install.py --tool antigravity --bundle student
    python3 install.py --tool cursor --bundle all
    python3 install.py --list
    python3 install.py --tool codex --bundle all --dry-run
    python3 install.py --tool gemini --bundle all --path /custom/skills/dir

Tool default paths (global / user level):
    claude       ~/.claude/skills
    antigravity  ~/.gemini/antigravity/skills   (Antigravity 2.0 may use
                 ~/.gemini/config/skills instead - if your skills do not
                 appear, reinstall with --path ~/.gemini/config/skills)
    cursor       ~/.cursor/skills
    codex        ~/.codex/skills
    gemini       ~/.gemini/skills
"""
import argparse
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

TOOL_PATHS = {
    "claude": "~/.claude/skills",
    "antigravity": "~/.gemini/antigravity/skills",
    "cursor": "~/.cursor/skills",
    "codex": "~/.codex/skills",
    "gemini": "~/.gemini/skills",
}


def load_bundles():
    with open(os.path.join(ROOT, "bundles.json")) as f:
        return json.load(f)


def main():
    p = argparse.ArgumentParser(description="Install Skills for Everyone into your AI agent")
    p.add_argument("--tool", choices=sorted(TOOL_PATHS), help="which agent to install for")
    p.add_argument("--bundle", choices=["freelancer", "student", "all"], default="all")
    p.add_argument("--path", help="custom skills directory (overrides --tool default)")
    p.add_argument("--list", action="store_true", help="list all skills and bundles, then exit")
    p.add_argument("--dry-run", action="store_true", help="show what would be copied, copy nothing")
    p.add_argument("--force", action="store_true", help="overwrite skills that are already installed")
    a = p.parse_args()

    bundles = load_bundles()

    if a.list:
        for bundle in ("freelancer", "student"):
            print(f"\n[{bundle}] bundle")
            for name in bundles[bundle]:
                print(f"  - {name}")
        print(f"\nTotal: {len(bundles['all'])} skills")
        return

    if not a.tool and not a.path:
        p.error("give --tool (claude, antigravity, cursor, codex, gemini) or --path")

    dest_root = os.path.expanduser(a.path or TOOL_PATHS[a.tool])
    names = bundles[a.bundle]
    print(f"Installing bundle '{a.bundle}' ({len(names)} skills) -> {dest_root}")
    installed, skipped = 0, 0
    for name in names:
        src = os.path.join(ROOT, "skills", name)
        dst = os.path.join(dest_root, name)
        if not os.path.isfile(os.path.join(src, "SKILL.md")):
            print(f"  ERROR: {name} has no SKILL.md in this repo - skipped")
            skipped += 1
            continue
        if os.path.exists(dst) and not a.force:
            print(f"  skip (already exists, use --force to overwrite): {name}")
            skipped += 1
            continue
        if a.dry_run:
            print(f"  would copy: {name}")
            installed += 1
            continue
        os.makedirs(dest_root, exist_ok=True)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"  installed: {name}")
        installed += 1

    print(f"\nDone: {installed} installed, {skipped} skipped.")
    if not a.dry_run and installed:
        print("Restart your AI agent (or start a new chat) so it discovers the new skills.")
        if a.tool == "antigravity":
            print("Note: Antigravity 2.0 may read ~/.gemini/config/skills instead.")
            print("If the skills do not appear, run again with: --path ~/.gemini/config/skills")


if __name__ == "__main__":
    sys.exit(main())
