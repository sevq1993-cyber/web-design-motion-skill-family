---
name: gsap-scrolltrigger
description: "Use for GSAP ScrollTrigger work: pinned sections, scrubbed scroll animation, scroll-linked timelines, complex sequencing, matchMedia behavior, refresh after async layout, and React-safe GSAP lifecycle."
---

# GSAP ScrollTrigger

Use this only when scroll-linked behavior needs GSAP's timeline and trigger model.

## Use For

- pinned sections;
- scrubbed timelines;
- multi-step scroll storytelling;
- scroll-linked progress;
- complex sequencing across multiple elements;
- refresh control after fonts, images, async content, or layout changes.

## React Safety

- Scope animations to component refs.
- Use a React-safe lifecycle and cleanup.
- Register plugins once in the right runtime environment.
- Use GSAP media-query handling for responsive variants.
- Refresh after async layout changes.
- Avoid global selectors that affect unrelated components.

## Correctness

- Prefer transforms and opacity over layout properties.
- Use explicit start/end values.
- Use refresh ordering intentionally when triggers depend on previous pinned sections.
- Do not use deprecated media-query APIs.
- Provide reduced-motion fallback or disable scroll-linked effects when appropriate.

