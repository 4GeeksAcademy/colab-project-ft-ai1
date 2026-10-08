# CASTANIER — Shared Design System

## 1. Brand Identity

**Brand:** CASTANIER  
**Industry:** French boutique clothing / contemporary luxury fashion  
**Aesthetic:** French heritage, quiet luxury, earthy minimalism, natural elegance.

### Design Principles
- Minimalist, editorial, sophisticated.
- Inspired by chestnut trees, the French countryside, and vintage European fashion.
- Generous whitespace and carefully balanced layouts.
- Avoid overly bright colors, heavy shadows, excessive animations, and crowded interfaces.
- Prioritize beautiful fashion photography and clear typography.
- Every page must feel like part of the same luxury boutique.

---

## 2. Color Palette

All developers must use the shared colors. Do not introduce new colors without team agreement.

| Token | HEX | Purpose |
|---|---|---|
| Forest Green | `#283D32` | Primary buttons, headers, accents |
| Chestnut Brown | `#76513D` | Secondary accents, decorative elements |
| Warm Beige | `#E8DECD` | Secondary backgrounds, cards |
| Ivory | `#F8F5EF` | Main page background |
| Sage Green | `#A3AD91` | Subtle accents, hover details |
| Dark Espresso | `#28241F` | Primary text |
| Muted Taupe | `#81796E` | Secondary text, captions |
| Soft Border | `#D8D0C3` | Dividers, card borders |
| Pure White | `#FFFFFF` | Contrast and overlays |

### Color Rules
- Main page background: Ivory.
- Navigation and footer: Forest Green or Ivory.
- Main text: Dark Espresso.
- Primary action buttons: Forest Green with white text.
- Secondary buttons: Transparent with Forest Green border/text.
- Cards: Ivory, white, or Warm Beige.
- Brown should be used for accents, not large blocks of body text.
- Maintain WCAG AA contrast: at least 4.5:1 for normal text.
- Do not use pure black for general body text.

---

## 3. Typography

### Font Families

**Headings:** Cormorant Garamond (Google Fonts)  
**Body / Navigation / Buttons:** Inter (Google Fonts)

### Typography Scale

| Element | Desktop | Mobile | Weight |
|---|---|---|---|
| Hero Heading | 72px | 42px | 400 |
| H1 | 56px | 36px | 400 |
| H2 | 40px | 30px | 400 |
| H3 | 28px | 24px | 500 |
| H4 | 22px | 20px | 500 |
| Body | 16px | 16px | 400 |
| Small Text | 14px | 14px | 400 |
| Caption | 12px | 12px | 500 |
| Buttons | 13px | 13px | 500 |

### Typography Rules
- Headings use Cormorant Garamond with a line height of 1.1–1.2.
- Body uses Inter with a line height of 1.6–1.7.
- Headings use normal or medium weight; avoid heavy bold.
- Navigation, categories, and buttons use uppercase text with increased letter spacing.
- Use `tracking-[0.12em]` for buttons and small labels.
- Use `tracking-[0.04em]` for larger display headings where appropriate.
- Avoid mixing additional font families.

---

## 4. Layout and Spacing

### Standard Layout
- Maximum content width: `1280px`
- Centered containers: `mx-auto max-w-7xl`
- Desktop horizontal padding: `px-8`
- Tablet horizontal padding: `px-6`
- Mobile horizontal padding: `px-4`
- Section vertical spacing: `py-20` desktop, `py-12` mobile
- Standard grid gap: `gap-6` or `gap-8`

### Spacing Rules
Use the Tailwind spacing scale consistently.

- 4px: Fine details
- 8px: Icon spacing
- 12px: Small element spacing
- 16px: Standard internal spacing
- 24px: Card padding and component spacing
- 32px: Larger groups
- 48px: Between major elements
- 80px: Desktop section separation

Avoid arbitrary spacing unless required by the design.

---

## 5. Buttons

### Primary Button
- Background: Forest Green
- Text: White
- Hover: Chestnut Brown
- Height: 48px
- Horizontal padding: 32px
- Border radius: 4px
- Uppercase Inter, 13px, medium weight
- Letter spacing: 0.12em
- Transition: 200ms ease

**Tailwind example:**  
`bg-[#283D32] text-white hover:bg-[#76513D] h-12 px-8 rounded-[4px] text-[13px] font-medium uppercase tracking-[0.12em] transition-colors duration-200`

### Secondary Button
- Transparent background
- 1px Forest Green border
- Forest Green text
- Hover: Forest Green background, white text
- Same dimensions as primary button

### Text / Editorial Button
- No filled background
- Underlined text or subtle bottom border
- Underline animates or changes color on hover
- Suitable for "Discover More", "View Collection", and editorial links

### Button Rules
- No pill-shaped buttons.
- No bright gradients.
- Use consistent sizes throughout the site.
- Include visible keyboard focus states.
- Disable buttons during loading or submission.

---

## 6. Cards

### Product Cards
- Background: Ivory or transparent
- Image aspect ratio: 3:4
- Image behavior: `object-cover`
- Border radius: 2–4px maximum
- No heavy box shadows
- Product name: Inter, 14–16px, medium weight
- Price: Inter, 14px, muted brown or espresso
- Description: 13px, muted taupe

**Hover behavior:**
- Image subtly scales to 1.03.
- Product image may transition to an alternate image.
- Transition duration: 300ms.
- Avoid moving the entire card.

### Collection Cards
- Large editorial photography.
- Aspect ratio: 4:5 or 3:4.
- Text either underneath or over a subtle dark image overlay.
- Minimal text: collection name + one action.
- No excessive borders or shadows.

### Information Cards
- Warm Beige background.
- 1px Soft Border when necessary.
- Padding: 24px.
- Border radius: 4px.
- No decorative gradients.

---

## 7. Navigation and Footer

### Navigation
- Desktop navbar height: 80px.
- Mobile navbar height: 64px.
- Logo: CASTANIER in uppercase with generous letter spacing.
- Background: Ivory.
- Links: Inter, 12–13px, uppercase.
- Link hover: Chestnut Brown.
- Use understated icons.
- Sticky navigation is permitted, but must remain consistent.
- Mobile uses an accessible collapsible menu.

### Footer
- Forest Green background.
- Ivory text.
- Clear columns for navigation, customer care, and contact.
- Thin, subtle divider lines.
- Minimal icons and social links.
- No oversized animations.

---

## 8. Forms and Inputs

- Input height: 48px minimum.
- Background: White or Ivory.
- Border: 1px Soft Border.
- Border radius: 4px.
- Text color: Dark Espresso.
- Placeholder: Muted Taupe.
- Focus: Forest Green border and visible focus ring.
- Labels: Inter, 13px, medium weight.
- Error messages: Accessible muted red, used only for errors.
- All fields must have visible labels.
- Ensure all forms support keyboard navigation.

---

## 9. Images and Visual Direction

### Photography
- Natural lighting.
- Warm, muted tones.
- Countryside, stone, wood, linen, botanical elements.
- Editorial clothing photography with clean backgrounds.
- Avoid oversaturated colors.
- Preserve consistent image ratios on listing pages.

### Image Treatments
- Use subtle overlays when needed for text readability.
- No excessive filters.
- Use `object-cover` for cropped editorial photography.
- Use `object-contain` only where displaying the full product is important.
- Optimize images and lazy-load below-the-fold imagery.

---

## 10. Animations and Interactions

- Default transitions: 200–300ms.
- Use subtle opacity, color, or scale changes.
- No bouncing buttons or dramatic motion.
- Smooth scrolling where appropriate.
- Respect `prefers-reduced-motion`.
- Keep animation consistent between branches.

---

## 11. Responsive Breakpoints

Use Tailwind's default breakpoints:

- Mobile: below `640px`
- Small tablet: `sm` — 640px+
- Tablet: `md` — 768px+
- Desktop: `lg` — 1024px+
- Large desktop: `xl` — 1280px+

### Responsive Guidelines
- Mobile-first implementation.
- Product grid: 2 columns mobile, 3 tablet, 4 desktop.
- Navigation collapses on smaller screens.
- Content must never overflow horizontally.
- Buttons and inputs must remain comfortable to tap.
- Hero typography and spacing must scale responsively.

---

## 12. Accessibility

- Use semantic HTML (`header`, `nav`, `main`, `section`, `footer`).
- Use only one H1 per page.
- Follow a logical heading hierarchy.
- Every meaningful image requires descriptive alt text.
- All interactive elements must be keyboard accessible.
- Provide visible focus states.
- Minimum recommended touch target: 44×44px.
- Do not communicate information using color alone.
- Follow WCAG 2.2 AA where practical.

---

## 13. Development Rules for All Branches

**Tech stack:** HTML + Tailwind CSS + JavaScript where needed.

### Shared Conventions
1. All pages must follow this design system.
2. Reuse shared color and typography tokens.
3. Do not create new button, card, navbar, or form styles independently.
4. Do not introduce new font families.
5. Follow consistent Tailwind class naming and ordering.
6. Use semantic HTML.
7. Ensure all pages work on mobile and desktop.
8. Use consistent hover and focus states.
9. Avoid unnecessary custom CSS where Tailwind utilities are sufficient.
10. Any intentional deviation must be discussed and documented before merging.

### Shared Files
Recommended project structure:

- `index.html` — Main entry point
- `src/styles.css` — Global styles and design tokens
- `src/components/` — Shared component snippets/templates if applicable
- `src/pages/` — Individual page implementations, if using a multi-page setup
- `assets/images/` — Shared images
- `assets/icons/` — Shared icons
- `context.md` — Shared design and development guidelines

The exact folder structure may vary by build setup, but shared styles and tokens must have a single source of truth.

### Before Merging a Branch
- Check palette consistency.
- Check typography consistency.
- Check buttons/cards against specifications.
- Test mobile and desktop layouts.
- Test hover, focus, and keyboard navigation.
- Check accessibility and image optimization.
- Confirm there are no unnecessary duplicated styles.

**The objective: every branch should look and feel as though one designer and one development team created the entire CASTANIER website.**