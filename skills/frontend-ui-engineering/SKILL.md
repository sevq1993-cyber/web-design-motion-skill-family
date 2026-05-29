---
name: frontend-ui-engineering
description: "Use when building, modifying, reviewing, or polishing user-facing web UI: responsive layout, accessibility, forms, states, navigation, density, product UI, dashboard UI, browser QA, anti-slop cleanup, and frontend quality gates."
---

# Frontend UI Engineering

Use this skill to turn design intent into robust UI.

## Rubric

Classify issues as:

- blocking: broken primary flow, inaccessible interaction, data loss, console-breaking error, impossible mobile layout;
- major: weak hierarchy, unclear action, broken focus, poor form errors, layout shift, overflow, bad contrast;
- minor: polish, alignment, copy clarity, spacing rhythm, hover/focus nuance.

## Quality Gates

- Primary action is visible and unambiguous.
- Navigation, labels, and routes stay stable unless the task requires changes.
- Forms have labels, errors, disabled/loading states, preserved input, and keyboard flow.
- Interactive elements have hover, focus, active, selected, disabled, loading, and empty states where relevant.
- Product UI is dense enough for repeated use without becoming cramped.
- Responsive layout works at mobile widths and high zoom/reflow.
- Touch targets are usable.
- Transitions are explicit and do not animate everything.
- Browser verification checks console, overflow, reduced motion, and layout stability.

## References

- Read `references/ui-quality-gates.md` for the detailed checklist when reviewing or polishing a UI.

