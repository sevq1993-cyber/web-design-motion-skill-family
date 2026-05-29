# Architecture

This repository packages a small skill family, not one oversized prompt. The design goal is predictable routing: an AI agent should know whether a request is about visual direction, UI quality, site audit, redesign, animation, 3D, or design-system extraction.

The system is described in detail in the article:
[How We Built an AI Skill System for Web Design, Motion Design, and Vibe Coding](https://aicoding.am/blog/ai-web-design-motion-skill-system)

## Skill Layers

1. **Site workflow skills** decide whether the agent is auditing, redesigning, or creating a site.
2. **Shared quality skills** define visual direction and UI engineering gates.
3. **Motion router** chooses CSS, Motion, GSAP, Lottie, Rive, or 3D based on the actual interaction.
4. **Runtime skills** contain narrow implementation rules for the chosen animation technology.
5. **Browser QA** is expected after meaningful frontend changes.

## Routing Principles

- Existing site critique starts with evidence: URL, screenshots, local preview, product context, and current code.
- New site creation starts with audience, page goal, content truth, and visual differentiation.
- Redesign preserves routes, forms, SEO structure, analytics hooks, legal copy, accessibility wins, and product-critical behavior.
- Motion is a product-design decision first, a library decision second.
- References stay compact and linked from `SKILL.md`; no copied documentation dumps.

## What This System Avoids

- vague "make it beautiful" changes without acceptance criteria;
- fake logos, fake metrics, fake testimonials, and invented customer proof;
- generic gradient-card websites;
- animation libraries used as decoration instead of interaction design;
- broad parallax, 3D, or Lottie defaults for ordinary pages;
- stale packages and CDN snippets as modern defaults;
- finishing without browser verification.

