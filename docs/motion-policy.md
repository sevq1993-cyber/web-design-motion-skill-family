# Motion Policy

Use the smallest runtime that can express the intended behavior cleanly.

| Situation | Default choice |
| --- | --- |
| hover, focus, active, disclosure, simple reveal | CSS transitions or keyframes |
| React layout transitions, gesture, drag, exit, shared layout | Motion for React |
| timeline choreography, pinning, scrubbed scroll, complex scroll storytelling | GSAP ScrollTrigger |
| designer-exported vector animation | dotLottie first, legacy Lottie JSON only when needed |
| interactive animation with states and inputs | Rive |
| real 3D, WebGL, camera, lighting, shaders | Three.js or React Three Fiber |
| decorative pseudo-3D | CSS first; niche libraries only with explicit justification |

## Motion Budget

Before implementing, define:

- purpose: orientation, feedback, hierarchy, delight, or narrative;
- scope: which elements move and which stay stable;
- budget: number of motion moments, runtime weight, and scroll cost;
- accessibility: reduced-motion behavior and keyboard/focus states;
- QA: console, overflow, layout shift, mobile, and reduced motion checks.

## Defaults

- Do not migrate an existing animation stack unless there is a clear maintenance or correctness reason.
- Do not use GSAP for unspecified React fades, hovers, or basic component transitions.
- Do not use Lottie or Rive without an asset or a reason to create one.
- Do not add smooth-scroll libraries as a default dependency.
- Do not animate layout-affecting properties when transforms or opacity are enough.

