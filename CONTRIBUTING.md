# Contributing to Skills for Everyone

Thanks for helping. This repo stays useful by staying **small, tested, and honest** — please read these rules before opening a PR.

## Adding a new skill

1. **One skill, one job.** If your skill does two jobs, split it.
2. Create `skills/<your-skill-name>/SKILL.md`. The folder name must be lowercase kebab-case and **identical** to the `name:` value in the frontmatter.
3. Use this structure (copy any existing skill as a template):
   - YAML frontmatter: `name` + `description`
   - `## When to use this skill`
   - `## Workflow` (numbered steps the agent follows, in order)
   - `## Rules - never break these`
   - `## Output format`
   - `## Example` (a real user prompt + an excerpt of a good output)
4. **The description is the trigger.** The agent decides whether to load your skill from the description alone. State *what it does* and *when to use it*, with the phrases a real user would type. Keep it between 80 and 1024 characters.
5. Keep the whole file under **500 lines**. Move long reference material into a `references/` subfolder and point to it from the workflow.
6. Add the skill name to `bundles.json` (in its bundle list **and** in `all`, in the same position), and to the bundle table in `README.md` and `CATALOG.md`.
7. Run the validator — it must pass before you open the PR:
   ```bash
   python3 scripts/validate_skills.py
   ```
8. **Test it for real.** Install your skill into at least one agent (Claude Code, Antigravity, Cursor, Codex, or Gemini CLI), ask for the job *without naming the skill*, and confirm the agent loads it and follows the workflow. Say which agent you tested in your PR description. Do not claim a test you did not run.

## The honesty rules for content

Skills in this repo must never instruct an agent to:

- invent experience, clients, metrics, references, statistics, or qualifications
- promise results the user cannot control
- write a student's assignment, thesis, or exam answers *for* them (teaching, research structure, and practice are welcome)

If a workflow step could produce a fabricated claim, add a rule that blocks it.

## Fixing an existing skill

- A skill that doesn't trigger: the fix is almost always a better `description` — add the real phrases users type.
- A skill that gives wrong output: tighten the workflow steps or add a rule, and update the Example to show the corrected behaviour.
- Keep PRs focused: one skill per PR.

## Style

- Simple English first. Many users of this repo are not native English speakers — and neither are many of its readers.
- Short steps, in order, written as instructions to the agent ("Extract...", "Ask for...", "Never...").
- No marketing language inside `SKILL.md`. The README sells; the skill works.
