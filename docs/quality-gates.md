# Web Design Quality Gates

These gates are intentionally practical. They are not a visual style guide; they are checks that prevent common AI-generated website failures.

## Visual Direction

- The page type is clear: marketing, SaaS, dashboard, documentation, portfolio, editorial, commerce, or app tool.
- The target user and primary task are explicit.
- The first viewport communicates the actual product, offer, or object.
- Visual rhythm is varied without becoming noisy.
- Typography, spacing, contrast, and density match the domain.
- The design does not rely on generic gradients, decorative blobs, repetitive card grids, or meaningless CTAs.

## Product UI

- Primary actions are obvious.
- Forms have labels, validation, error states, and preserved input.
- Tables and dashboards support scanning, comparison, and repeated use.
- Empty, loading, error, disabled, hover, focus, and selected states exist where needed.
- Navigation labels, routes, forms, analytics hooks, legal copy, and SEO-critical structure are preserved during redesigns.

## Frontend Verification

- No console errors in the checked flows.
- No horizontal overflow at mobile widths.
- Layout works at narrow mobile sizes and high zoom/reflow.
- Touch targets are usable.
- Motion respects reduced-motion settings.
- Browser screenshots are taken only after fonts/assets are stable.
- New effects do not create layout shift or obscure content.

