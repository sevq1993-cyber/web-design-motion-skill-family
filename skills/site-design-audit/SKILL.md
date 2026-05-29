---
name: site-design-audit
description: "Use when auditing an existing website or page by URL, localhost, screenshot, browser view, or code. Covers visual design, UX, UI quality, responsiveness, accessibility, motion, content credibility, and prioritized fixes."
---

# Site Design Audit

Use this for critique before large changes.

## Inputs

Prefer direct evidence: browser view, screenshots, local preview, key routes, product context, and current code. If only a prompt is available, state assumptions and keep recommendations tied to observable structure.

## Process

1. Identify page type, audience, primary task, and business goal.
2. Review visual direction with `frontend-design`.
3. Review implementation quality with `frontend-ui-engineering`.
4. If motion is requested or already present, route through `frontend-motion-style-system`.
5. Prioritize findings by impact: blocking, major, minor.
6. When asked to improve the site, implement the highest-impact fixes and verify in a browser.

## Preservation Rules

Do not silently change slugs, navigation labels, forms, analytics hooks, legal/cookie copy, accessibility wins, or SEO-critical structure.

## Output

Provide concise findings, the reasoning behind priority, concrete changes, and verification performed.

