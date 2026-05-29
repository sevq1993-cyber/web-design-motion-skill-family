---
name: lottie-animations
description: "Use when implementing designer-exported vector animation with dotLottie or Lottie: .lottie files, JSON Bodymovin legacy paths, React players, SSR-safe wrappers, workers, themes, slots, and playback controls."
---

# Lottie Animations

Use Lottie for bounded vector assets, not for ordinary UI transitions.

## Runtime Policy

- Prefer dotLottie for new work when the asset is available as a `.lottie` package.
- Use legacy Bodymovin JSON only when the project already depends on that path or the asset is only available as JSON.
- Wrap players so SSR, hydration, sizing, loading, and reduced motion are handled cleanly.
- Keep animation assets versioned and inspectable.

## Implementation Checks

- Confirm asset dimensions and container sizing.
- Provide fallback content for failure or reduced motion.
- Avoid huge autoplay loops that compete with primary content.
- Do not run lossy optimization without preserving the original and visually verifying the result.
- Use playback controls only when they serve the interaction.

