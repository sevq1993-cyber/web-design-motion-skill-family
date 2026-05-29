# Contributing

This repository is intentionally small. Contributions should improve routing clarity, runtime correctness, design quality, or validation without turning the skill family into a prompt dump.

## Rules

- Keep `SKILL.md` files concise.
- Put detailed guidance in linked `references/` files.
- Do not copy large external documents into this repository.
- Do not add private project names, local paths, tokens, screenshots, or customer data.
- Do not add stale animation packages, CDN snippets, or generated boilerplate as default guidance.
- Update `evals/routing-evals.json` when changing routing behavior.

## Validation

Run:

```bash
python3 scripts/validate-skills.py
```

If you have Codex's official skill validator available, also run it against every skill directory.

