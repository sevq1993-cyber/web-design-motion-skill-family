# Motion Routing

## CSS

Use CSS for local UI states: hover, focus, active, selected, disabled, disclosure, subtle reveal, color, opacity, and transform changes. Prefer explicit property transitions instead of `transition: all`.

## Motion For React

Use Motion when the problem is component-level interaction: layout transitions, gestures, drag, exit animations, shared layout, route transitions, or animation state tied to React state.

Use the existing project stack first. In greenfield React work, use Motion's current React package and import pattern. Do not force a migration in an existing project unless the user asks or maintenance risk is clear.

## GSAP ScrollTrigger

Use GSAP ScrollTrigger only when the behavior is scroll-linked and materially benefits from GSAP: pinned sections, scrubbed timelines, multi-step choreography, complex sequencing, or precise refresh control after async layout.

In React, use a scoped lifecycle, cleanup, media-query handling, and refresh after fonts/images/content change layout.

## Lottie And Rive

Use dotLottie/Lottie for bounded vector animations exported by designers. Use Rive when the animation needs a state machine, inputs, pointer interaction, or runtime state.

Do not use either as a substitute for ordinary UI transitions.

## 3D

Use Three.js or React Three Fiber for real 3D. Decorative pseudo-3D effects should start with CSS and degrade to static UI under reduced motion or weak devices.

