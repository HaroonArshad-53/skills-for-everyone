# Setup Guide — Skills for Everyone

Complete installation for every supported agent. Total time: about 2 minutes.
If anything goes wrong, check [Troubleshooting](#troubleshooting) at the bottom before opening an issue.

## Before you start

You need three things:

1. **One supported AI agent installed** — Claude Code, Google Antigravity, Cursor, OpenAI Codex CLI, or Google Gemini CLI
2. **Python 3** — check with `python3 --version` (Windows: `python --version`). Any Python 3.8+ works. The installer uses only the standard library — nothing to pip install.
3. **Git** — check with `git --version`

## Method A — Installer script (recommended)

### Step 1: Download the repo

```bash
git clone https://github.com/HaroonArshad-53/skills-for-everyone.git
cd skills-for-everyone
```

Windows (PowerShell): the same two commands work as-is.

### Step 2: Install for your agent and bundle

macOS / Linux:

```bash
python3 install.py --tool claude --bundle freelancer      # Claude Code + Freelancer skills
python3 install.py --tool antigravity --bundle student   # Antigravity + Student skills
python3 install.py --tool cursor --bundle all            # Cursor + all 12 skills
python3 install.py --tool codex --bundle all             # Codex CLI + all 12 skills
python3 install.py --tool gemini --bundle all            # Gemini CLI + all 12 skills
```

Windows: replace `python3` with `python` — everything else is identical.

Useful options:

| Option | What it does |
|---|---|
| `--list` | Lists all 12 skills and the bundles they belong to |
| `--dry-run` | Shows exactly what would be copied, copies nothing |
| `--force` | Overwrites skills you already installed (use this when updating) |
| `--path /any/dir` | Installs to a custom skills directory instead of the tool default |

Default install locations:

| Agent | Directory (macOS/Linux) | Directory (Windows) |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `%USERPROFILE%\.claude\skills\` |
| Google Antigravity | `~/.gemini/antigravity/skills/` | `%USERPROFILE%\.gemini\antigravity\skills\` |
| Cursor | `~/.cursor/skills/` | `%USERPROFILE%\.cursor\skills\` |
| OpenAI Codex CLI | `~/.codex/skills/` | `%USERPROFILE%\.codex\skills\` |
| Google Gemini CLI | `~/.gemini/skills/` | `%USERPROFILE%\.gemini\skills\` |

> **Antigravity 2.0 note:** newer Antigravity versions may read skills from `~/.gemini/config/skills/` instead. If your skills do not appear after restarting (see Step 4), install again with:
> `python3 install.py --tool antigravity --bundle all --path ~/.gemini/config/skills`

### Step 3: Restart your agent

Close and reopen your agent, or simply start a **new chat/session**. Agents discover skills at startup — a chat that was already open will not see newly installed skills.

### Step 4: Verify it worked (do not skip this)

Paste this test prompt into a fresh chat:

> *How much should I charge for a 10-hour project on Upwork at 20 dollars per hour, due in 4 days?*

**Correct result:** the agent uses the pricing-calculator skill — it states its inputs, accounts for the rush and the 10% Upwork fee, and gives Low / Recommended / High quotes with the take-home amount for each. If it also offers to run `scripts/pricing.py`, let it — that is the skill working exactly as designed.

Second test (Student bundle):

> *Grill me for a data entry internship interview.*

**Correct result:** the interview-griller asks **one** question and waits for your answer — it does not dump a list of questions.

If both behave like this, setup is complete. 🎉

### Step 5: Use it

Just ask for the job in plain language. You do not need to name skills — the agent matches your request to a skill's description and loads it automatically. Full worked examples for all 12 skills: [EXAMPLES.md](EXAMPLES.md).

## Method B — Manual copy (no script)

1. Clone the repo (Step 1 above).
2. Copy any `skills/<skill-name>/` folder into your agent's skills directory from the table above.
   Example (Claude Code, one skill): `cp -r skills/proposal-writer ~/.claude/skills/`
3. Restart your agent and verify with Step 4.

## Method C — Community skills CLI

```bash
npx skills add HaroonArshad-53/skills-for-everyone
```

Follow the prompts to pick skills and your agent.

## Updating

```bash
cd skills-for-everyone
git pull
python3 install.py --tool <your-agent> --bundle <your-bundle> --force
```

## Uninstalling

Delete the skill folders from your agent's skills directory. To remove one skill (Claude Code example):

```bash
rm -rf ~/.claude/skills/proposal-writer
```

Windows: delete the folder in Explorer. Restart the agent afterwards.

## Troubleshooting

| Problem | Cause & fix |
|---|---|
| Skills don't appear / agent ignores them | The chat was already open. Start a **new** session. Then confirm the folders really are in the directory from the table above (each must contain a `SKILL.md`). |
| Antigravity still doesn't see them | Your version likely uses the other path. Reinstall with `--path ~/.gemini/config/skills` (see the Antigravity note in Step 2). |
| `python3: command not found` (Windows) | Use `python` instead of `python3`, or install Python from python.org and tick "Add to PATH". |
| Installer says "already exists, skipped" | That skill is already installed. Add `--force` to overwrite/update it. |
| The wrong skill loads | Name the job more specifically ("write my Upwork proposal for *this* job post:" + paste the post). Very short prompts match less reliably. |
| A skill loads but output ignores the format | Report it as an issue with your agent name, the exact prompt, and the output — that is exactly the feedback that improves a skill's workflow. |
| `git clone` fails with a network error | Download the ZIP instead: repo page → **Code** button → **Download ZIP**, unzip, and continue from Step 2. |
