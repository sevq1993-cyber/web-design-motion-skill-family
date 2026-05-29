---
name: motion-react
description: "Use when React or JavaScript UI needs Motion components, gestures, layout transitions, exit animations, shared layout, drag, route transitions, or component-state animation. Prefer the current Motion React package for new work and respect existing stacks."
---

# Motion React

Use this for component-level React motion.

## Runtime Policy

- Existing project: follow the installed animation stack unless there is a clear reason to migrate.
- New React work: use the current Motion React package and import from its React entry point.
- Do not force migration only because a newer package exists.
- Do not use Motion for pinned or scrubbed scroll storytelling; route that to GSAP ScrollTrigger.

## Good Uses

- layout transitions;
- enter and exit animations;
- gestures and drag;
- shared layout;
- route transitions;
- state-driven component animation.

## Implementation Checks

- Keep animation state predictable and close to the component.
- Respect reduced motion for nontrivial movement.
- Avoid layout jumps and content overlap.
- Verify keyboard and focus behavior when animated components appear or disappear.

