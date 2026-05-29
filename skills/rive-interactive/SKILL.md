---
name: rive-interactive
description: "Use when web or React UI needs Rive animations, .riv files, state machines, interactive inputs, runtime-driven animation states, WebGL/canvas runtime choices, sizing, and reduced-motion fallback."
---

# Rive Interactive

Use Rive when animation behavior is stateful or interactive.

## Use For

- state-machine animations;
- pointer or input-driven animation;
- onboarding characters or product illustrations with states;
- success, progress, or empty-state animation where runtime state matters.

## Runtime Policy

- Prefer the current official React runtime for new React work.
- Choose WebGL, canvas, or lite runtime based on feature needs, performance, and bundle constraints.
- Isolate Rive wrappers so sizing, loading, failure, and cleanup are consistent.
- Check runtime support for the exact feature used by the asset.

## Checks

- Keep `.riv` assets explicit in the repo or documented asset pipeline.
- Provide static fallback for reduced motion or failed runtime loading.
- Verify canvas sizing at desktop and mobile breakpoints.
- Avoid using Rive for simple hover, focus, or reveal effects.

