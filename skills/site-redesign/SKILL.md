---
name: site-redesign
description: "Use when redesigning an existing website or page while preserving product behavior, routes, forms, SEO, analytics hooks, legal copy, accessibility wins, and content truth. Covers visual redesign, UI quality, responsiveness, and optional motion."
---

# Site Redesign

Use this when the user wants a stronger version of an existing site, not a new unrelated concept.

## Workflow

1. Audit the current site first: goal, audience, strengths, failures, and constraints.
2. Define the redesign direction with `frontend-design`.
3. Apply UI quality gates with `frontend-ui-engineering`.
4. Use `frontend-motion-style-system` only when motion, scroll, media, or 3D is part of the request or clearly improves the result.
5. Implement in the existing stack and style architecture.
6. Verify desktop, mobile, console errors, overflow, reduced motion, and key flows.

## Preserve

- routes and slugs;
- navigation meaning;
- forms and field names;
- analytics and conversion hooks;
- legal, cookie, and compliance copy;
- SEO metadata and heading structure when important;
- existing accessibility improvements.

## Avoid

- replacing product UI with a marketing hero;
- inventing new proof claims;
- broad rewrites when targeted fixes solve the problem;
- decorative animation that does not support comprehension.

