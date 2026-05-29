# UI Quality Gates

## Structure

- Stable routes, nav labels, forms, analytics hooks, legal copy, and SEO-critical structure are preserved during redesign unless the user explicitly asks to change them.
- Layout uses clear constraints: max widths, grid tracks, aspect ratios, and fixed control dimensions where dynamic content could cause jumps.
- Text fits its containers at desktop and mobile sizes.

## Accessibility

- Keyboard focus is visible.
- Form fields have labels and error messages.
- Color contrast is sufficient.
- Reduced-motion behavior is implemented when motion is nontrivial.
- Content reflows at narrow widths and high zoom without horizontal scrolling.

## Product UI

- Tables, filters, search, bulk actions, empty states, and loading states are practical.
- Dashboards prioritize comparison and repeated use over marketing composition.
- Primary and destructive actions are visually distinct.
- Saved, loading, error, stale, and disabled states are clear.

## Anti-Slop

- No fake metrics, fake logos, fake testimonials, or invented integrations.
- No one-note gradient palette.
- No repeated card grid as the only design structure.
- No hover-scale on every card.
- No meaningless CTAs.
- No animation that delays user control.

