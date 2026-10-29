# Profile (My account) — Page Spec

The signed-in customer's account page. It brings together what the site already collects at checkout and in the cart: personal details, saved addresses, saved cards, and past orders. The page has no real backend. It shows a pre-generated **guest account** (see `SIGN_IN_SPEC.md`) stored in the browser.

Follows `DESIGN_CONTEXT.md` (CASTANIER design system) and `TECH_CONTEXT.md` (semantic HTML, SEO, responsive, WCAG, Tailwind only).

---

## 1. Summary

| | |
|---|---|
| **Route** | `/account` (already registered in `server.py`) |
| **File** | `account/index.html` |
| **Entry points** | Navbar "My account" icon on every page; "Sign in to guest profile" on `/sign-in` |
| **Access** | Signed in only. Signed-out visitors are redirected to `/sign-in` |
| **Stack** | HTML + Tailwind CSS v4 browser CDN + inline vanilla JavaScript, same as `cart/index.html` |

---

## 2. Page structure

```
Skip link → #main-content
Header (navbar, copied from cart/index.html)
Main
  Breadcrumb: Home / My account
  H1 "My account" + greeting "Bonjour, {firstName}"
  Two-column layout
    Left  (aside):  Account menu
    Right (section): Active section
      Overview | Orders | Addresses | Payment methods | Account details
Footer (copied from cart/index.html)
```

### Layout

- Container: `mx-auto max-w-7xl px-4 sm:px-6 lg:px-8`, section spacing `py-12 lg:py-20`.
- Desktop (`lg` and up): grid with a fixed-width menu, e.g. `lg:grid lg:grid-cols-[240px_1fr] lg:gap-12`.
- Tablet and mobile: the menu becomes a horizontal, scrollable row of links above the content, with no horizontal page overflow.

---

## 3. Account menu

An `<nav aria-label="Account">` holding a list of links:

| Label | Target |
|---|---|
| Overview | `#overview` (default) |
| Orders | `#orders` |
| Addresses | `#addresses` |
| Payment methods | `#payment-methods` |
| Account details | `#details` |
| Sign out | Button, see §5.6 |

- Links use the navigation style: Inter, 12–13px, uppercase, `tracking-[0.12em]`, hover Chestnut Brown.
- The active link gets `aria-current="page"`, Forest Green text, and a 1px Forest Green left border on desktop or bottom border on mobile. It must not rely on color alone.
- Sign out is visually separated from the other links by a Soft Border divider.

---

## 4. Sections

Each section is a `<section id="…" aria-labelledby="…">` with an H2 (Cormorant Garamond, 40px desktop / 30px mobile). Only one section is visible at a time (see §6.3).

### 4.1 Overview (default)

- **Latest order** information card (Warm Beige, 24px padding, 4px radius):
  - Order number, date, status badge
  - Up to 3 product thumbnails (3:4, `object-cover`)
  - Order total
  - Text button **"View order"** → opens that order in Orders
- **Section shortcuts:** a grid of 4 small information cards (Orders, Addresses, Payment methods, Account details). Each has a title, a one-line description, and links to its section. Example: "Addresses: manage where your orders are delivered."
- Grid: 1 column on mobile, 2 on `md`, 4 on `xl`.

### 4.2 Orders

A list of the guest account's orders, newest first. Each order is an `<article>` card with:

| Field | Example |
|---|---|
| Order number | `CAS-10421` |
| Date | 14 October 2026 (`<time datetime="2026-10-14">`) |
| Status | Delivered / Shipped / Processing (badge: text label + muted color) |
| Thumbnails | One per line item |
| Total | `400,80 €` |
| Action | **"View details"** secondary button |

**"View details"** expands the order in place (a `<details>` element or a button with `aria-expanded`) and shows:

- Line items: thumbnail, name, variant (size), quantity, unit price, line total, using the cart's row layout
- Subtotal, tax (20%), and total, using the cart's summary layout
- Shipping address used for the order

Empty state: "You haven't placed any orders yet." with a primary **"Shop the collection"** button → `/catalog`.

### 4.3 Addresses

- A grid of address cards (1 column on mobile, 2 on `md`). Each card shows the name, address lines, postal code, city, region, country, and phone, with a **"Default"** label on the default address.
- Card actions: **Edit** and **Remove** text buttons.
- **"Add address"** secondary button.
- Add and Edit open an inline form under the list, reusing the checkout step 2 fields and their `autocomplete` values: `address-line1`, `address-line2`, `address-level2` (city), `address-level1` (region), `postal-code`, `country-name`, `tel`. There is a **"Save address"** primary button and a **"Cancel"** text button.
- Remove asks for confirmation inline ("Remove this address?" Confirm / Cancel). Do not use `window.confirm`.

### 4.4 Payment methods

- Card tiles show the brand, `•••• 4242`, the cardholder name, and `Expires 08/28`. Full numbers and security codes are never stored or shown.
- Actions: **Edit** (one step that replaces the card) and **Remove**.
- **"Add card"** secondary button, with an inline form reusing the checkout step 3 fields (`cc-name`, `cc-number`, `cc-exp`, `cc-csc`). On save, only the brand, last 4 digits, expiry, and name are kept.

### 4.5 Account details

A form with visible labels, 48px inputs, and checkout's input styling:

| Field | `autocomplete` | Notes |
|---|---|---|
| First name | `given-name` | Required |
| Last name | `family-name` | Required |
| Email | `email` | Required, `type="email"` |
| Phone | `tel` | Optional |
| Preferred size | — | `<select>` with XS, S, M, L, XL, matching the catalog size filter values `xs`…`xl` |

- **"Save changes"** primary button. It is disabled while saving and shows "Saved" in a polite `aria-live` status.
- Validation messages appear under the field, in muted red, linked to the field with `aria-describedby`.

---

## 5. Data

All data lives in `localStorage`, following the cart's `castanier-cart` pattern. Read it with `try/catch`, and fall back to the guest seed if it is missing or invalid.

### 5.1 Keys

| Key | Contents | Written by |
|---|---|---|
| `castanier-session` | `{ "customerId": "guest", "signedInAt": "<ISO date>" }` | Sign-in page |
| `castanier-profile` | The customer object (§5.2) | Sign-in page (seed), Profile page (edits) |
| `castanier-cart` | Existing cart items (read only, for the navbar bag count) | Cart page |

### 5.2 Customer object

```js
{
  id: "guest",
  firstName: "Camille",
  lastName: "Martin",
  email: "guest@castanier.fr",
  phone: "+33 6 12 34 56 78",
  preferredSize: "m",
  addresses: [
    {
      id: "addr-1",
      isDefault: true,
      fullName: "Camille Martin",
      line1: "12 rue des Châtaigniers",
      line2: "",
      city: "Paris",
      region: "Île-de-France",
      postalCode: "75006",
      country: "France",
      phone: "+33 6 12 34 56 78"
    }
  ],
  cards: [
    { id: "card-1", brand: "Visa", last4: "4242", expiry: "08/28", name: "Camille Martin" }
  ],
  orders: [
    {
      id: "CAS-10421",
      placedAt: "2026-10-14",
      status: "delivered",
      addressId: "addr-1",
      items: [ /* same shape as cart items */ ]
    },
    {
      id: "CAS-10388",
      placedAt: "2026-09-02",
      status: "shipped",
      addressId: "addr-1",
      items: [ /* … */ ]
    }
  ]
}
```

### 5.3 Order items

Order items use the **cart item shape** from `cart/index.html` so the same rendering code applies:

```js
{ id, name, category, imageUrl, imageAlt, variant, unitPriceCents, quantity }
```

Sample orders, built from the cart's sample products and images in `/assets/products/`:

| Order | Items | Subtotal | Tax (20%) | Total |
|---|---|---|---|---|
| CAS-10421 (delivered) | Etienne Pants (189 €), Henri Shirt (145 €), size M | 334,00 € | 66,80 € | 400,80 € |
| CAS-10388 (shipped) | Bastien Sweater (120 €), size M | 120,00 € | 24,00 € | 144,00 € |

Totals are calculated, not stored. Use the cart's method: integer cents, `tax = Math.round(subtotal * 0.2)`, and `Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" })`.

### 5.4 Seed

The guest seed object is defined once, in the sign-in page script. It is written to `castanier-profile` only if that key is empty, so the user's edits survive signing out and back in. The profile page keeps a copy of the seed as a fallback in case the key is missing or invalid.

### 5.5 Saving

Edits to addresses, cards, and details update the in-memory customer object, then write it back to `castanier-profile` and re-render the affected section.

### 5.6 Sign out

**Sign out** removes `castanier-session` and redirects to `/sign-in`. It keeps `castanier-profile`.

---

## 6. Implementation plan

### 6.1 Files

- Create `account/index.html`: a single self-contained page like `cart/index.html`.
- Copy the `<head>` setup from `cart/index.html`: Tailwind browser CDN, Google Fonts (Cormorant Garamond and Inter), and theme color.
- Copy the navbar, mobile menu, and footer markup from `cart/index.html` unchanged, so the page matches the rest of the site. Set the bag count from `castanier-cart`.

### 6.2 Auth guard

The first inline script in `<head>` reads `castanier-session`. If it is missing, it calls `location.replace("/sign-in")` before the page renders.

### 6.3 Section switching

- All five sections are in the HTML. JavaScript shows the one that matches `location.hash` (default `#overview`) and hides the others with the `hidden` attribute.
- Listen for `hashchange` so links, Back, and Forward all work. When a section changes, move focus to its H2 (`tabindex="-1"`) and update `aria-current` in the menu.
- Without JavaScript, all sections stay visible as one long page, and the menu links act as anchors.

### 6.4 Rendering

- Use `<template>` elements for the order card, order line, address card, and card tile. Fill them with `textContent` and never `innerHTML`, as in the cart's `#cart-item-template`.
- Use one `render()` function per section, called after load and after each save.

### 6.5 Build order

1. Page shell: head, navbar, footer, breadcrumb, H1, two-column layout, and menu.
2. Data layer: load and save `castanier-profile`, the seed fallback, and the auth guard.
3. Overview and Orders, including the expandable order details.
4. Account details form and validation.
5. Addresses: list, add, edit, and remove.
6. Payment methods: list, add, edit, and remove.
7. Sign out, hash routing, and focus management.
8. Check against the "Before merging" list in `DESIGN_CONTEXT.md`.

---

## 7. SEO, accessibility, responsive

- `<title>My account | CASTANIER</title>`, a meta description, and `<meta name="robots" content="noindex, nofollow">`, because private account pages are not indexed (same as checkout).
- JSON-LD: a `ProfilePage` with `BreadcrumbList`.
- One H1 ("My account"). Sections use H2, and cards use H3.
- Landmarks: `header`, `nav` (main), `nav aria-label="Account"`, `main`, and `footer`.
- Every image has descriptive alt text from `imageAlt`. Touch targets are at least 44×44px. Every control has a visible focus ring.
- Status badges always include a text label.
- Respect `prefers-reduced-motion`. Transitions run for 200–300ms and only on color or opacity.
- Mobile-first design: test at 375px, 768px, 1024px, and 1280px.

---

## 8. Acceptance checklist

- [ ] `/account` redirects to `/sign-in` when there is no session.
- [ ] After a guest sign-in, `/account` shows "Bonjour, Camille" and the Overview section.
- [ ] Orders lists 2 orders with correct totals (400,80 € and 144,00 €), and each one expands to show its details.
- [ ] Adding, editing, and removing an address or card persists after a reload.
- [ ] Changes to Account details persist after a reload, and required fields are validated.
- [ ] Sign out returns to `/sign-in`, and `/account` is blocked until the next sign-in.
- [ ] The navbar and footer match `cart/index.html` exactly.
- [ ] Keyboard-only navigation reaches every control, and focus is visible.
- [ ] There is no horizontal scroll at 375px.
