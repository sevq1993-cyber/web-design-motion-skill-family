---
name: frontend-motion-style-system
description: "Use when frontend work has visual, motion, media, scroll, 3D, or style ambiguity: make it feel alive, add animation, improve motion design, add scroll effects, polish visual rhythm, choose between CSS, Motion, GSAP, Lottie, Rive, or 3D. Also use for natural-language animation requests in English or Russian."
---

# Frontend Motion Style System

This is the router for ambiguous visual and motion requests. Use it before picking an animation runtime.

## Workflow

1. Read the page goal, audience, existing stack, and current visual direction.
2. Define a small motion budget: purpose, moments, runtime weight, reduced-motion behavior, and QA checks.
3. Pick the smallest fitting runtime:
   - CSS for hover, focus, active, disclosure, and simple reveals.
   - Motion for React layout, gesture, drag, exit, shared layout, and route transitions.
   - GSAP ScrollTrigger for pinning, scrubbed timelines, scroll storytelling, and complex sequencing.
   - dotLottie/Lottie for bounded designer-exported vector assets.
   - Rive for interactive state-machine animation.
   - Three.js or React Three Fiber for real 3D scenes.
4. Keep motion tied to meaning: orientation, feedback, hierarchy, flow, or narrative.
5. Verify reduced motion, mobile, console errors, overflow, and layout stability.

## Do Not Default To

- GSAP for unspecified React animation.
- parallax, smooth scrolling, 3D, Lottie, or Rive without a product reason.
- hover-scale spam, pulse loops, or animation on every card.
- motion that hides content, delays primary actions, or breaks reflow.

## References

- Read `references/motion-routing.md` when choosing between runtimes or designing scroll effects.

