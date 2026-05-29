---
name: lightweight-3d-effects
description: "Use only for small decorative depth effects, pseudo-3D UI, WebGL-light accents, CSS perspective, tilt effects, and deciding when to use real Three.js or avoid 3D entirely. Requires reduced-motion and static fallbacks."
---

# Lightweight 3D Effects

Use this only when depth improves the experience. For real 3D scenes, use a dedicated Three.js or React Three Fiber workflow.

## Defaults

- Start with CSS perspective, transforms, shadows, layering, and responsive constraints.
- Use real WebGL only when there is a clear reason.
- Treat older tilt, background, and CDN snippet libraries as legacy or niche, not modern defaults.
- Avoid decorative depth that makes text harder to read or controls harder to use.

## QA

- Provide reduced-motion and static fallback.
- Check mobile performance and battery impact.
- Verify canvas/WebGL is not blank.
- Check console errors.
- Confirm the effect does not create overflow, layout shift, or content overlap.

