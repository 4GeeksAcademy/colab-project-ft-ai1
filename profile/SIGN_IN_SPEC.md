# Sign in — Page Spec

The entry point to the customer account. The site has no backend, so the real email and password form is for display only. The working path is **"Sign in to guest profile"**, which signs in a pre-generated guest account and opens the profile page (`PROFILE_SPEC.md`).

The page follows `DESIGN_CONTEXT.md` (the CASTANIER design system) and `TECH_CONTEXT.md`.

---

## 1. Summary

| | |
|---|---|
| **Route** | `/sign-in` (already registered in `server.py`) |
| **File** | `sign-in/index.html` |
| **Entry points** | The navbar "My account" icon when signed out, Sign out on `/account`, and the auth redirect from `/account` |
| **Signed-in visitors** | Redirected straight to `/account` |
| **Stack** | HTML, Tailwind CSS v4 through the browser CDN, and inline vanilla JavaScript, the same as `cart/index.html` |

---

## 2. Page structure

```
Skip link → #main-content
Header (navbar, copied from cart/index.html)
Main (Ivory background, centered)
  Sign-in card
    H1 "Sign in"
    Welcome text
    Notice area (aria-live)
    Form: Email, Password, "Sign in"
    Divider "or"
    "Sign in to guest profile"
    Guest note
Footer (copied from cart/index.html)
```

### Layout

- Container: `mx-auto max-w-7xl px-4 sm:px-6 lg:px-8`, with `py-12 lg:py-20`.
- The card is centered at `max-w-md`, full width on mobile. It uses a Warm Beige or white background, a 1px Soft Border, a 4px radius, 24px padding (32px on `md` and up), and no shadow.

---

## 3. Content

### 3.1 Heading and intro

- **H1:** "Sign in" (Cormorant Garamond, 56px desktop / 36px mobile).
- **Intro** (Inter 16px, Muted Taupe): "Welcome back to CASTANIER. Sign in to view your orders, addresses and saved details."

### 3.2 Sign-in form (display only)

| Field | Type | `autocomplete` |
|---|---|---|
| Email | `email` | `email` |
| Password | `password` | `current-password` |

- Both fields have visible labels (Inter 13px, medium) and use the 48px input style from checkout.
- **"Sign in"**: a full-width primary button (Forest Green, white text, uppercase, `tracking-[0.12em]`).
- **On submit:** call `preventDefault()` and show this notice in the `aria-live="polite"` area above the form: "Accounts aren't available in this demo. Use **Sign in to guest profile** below." Then move focus to the guest button.
- Empty or invalid email: show a field error under the input (muted red, linked through `aria-describedby`) instead of the notice.

### 3.3 Divider

A thin Soft Border line with a centered "or" label (Caption, 12px, Muted Taupe, uppercase).

### 3.4 Guest sign-in

- **"Sign in to guest profile"**: a full-width secondary button (transparent background, Forest Green border and text, filled on hover).
- **Note** below it (Small text, 14px, Muted Taupe): "Explore a sample account with past orders, a saved address and a saved card."
- **On click:** sign in (see §4), disable the button and show "Signing in…", then go to `/account`.

---

## 4. Data and behavior

These keys match `PROFILE_SPEC.md` §5.

| Key | Action on guest sign-in |
|---|---|
| `castanier-profile` | If empty or invalid, write the guest seed. Otherwise leave it, so earlier edits are kept |
| `castanier-session` | Write `{ "customerId": "guest", "signedInAt": new Date().toISOString() }` |

- **Seed:** the full guest customer object (Camille Martin, `guest@castanier.fr`, preferred size M, 1 address, 1 card, orders CAS-10421 and CAS-10388) is defined once in this page's script. The exact values are in `PROFILE_SPEC.md` §5.2–5.3.
- **Redirect:** after writing, call `location.assign("/account")`.
- **Already signed in:** an inline `<head>` script checks `castanier-session` and calls `location.replace("/account")`.
- **Errors:** wrap every `localStorage` access in `try/catch`. If storage is unavailable, show "Your browser is blocking storage, so the guest profile can't be opened." in the notice area.

---

## 5. Implementation plan

### 5.1 Files

- Create `sign-in/index.html` as a self-contained page.
- Copy the `<head>` setup (Tailwind CDN, fonts, theme color), the navbar, the mobile menu and the footer from `cart/index.html` without changes. Set the bag count from `castanier-cart`.

### 5.2 Build order

1. Page shell: head, navbar, footer, and the centered card.
2. Form markup with labels, the notice area and the divider.
3. The display-only submit handler and email validation.
4. Guest sign-in: the seed, the session and the redirect.
5. The already-signed-in redirect.
6. Check against the "Before merging" list in `DESIGN_CONTEXT.md`.

---

## 6. SEO, accessibility, responsive

- `<title>Sign in | CASTANIER</title>`, a meta description, and `<meta name="robots" content="noindex, nofollow">`.
- JSON-LD: `WebPage` with a `BreadcrumbList` (Home / Sign in).
- One H1. The form is a `<form>` with an accessible name (`aria-labelledby` pointing to the H1).
- The notice area uses `role="status"` / `aria-live="polite"`. Errors are not shown by color alone, because each one has a text message.
- Touch targets are at least 44×44px, every control has a visible focus ring, and the full flow works by keyboard alone.
- Respect `prefers-reduced-motion`. No horizontal scroll at 375px.

---

## 7. Acceptance checklist

- [ ] `/sign-in` shows the card with the email and password form and the guest button.
- [ ] Submitting the form shows the demo notice and moves focus to the guest button.
- [ ] "Sign in to guest profile" opens `/account` signed in as Camille Martin.
- [ ] Visiting `/sign-in` while signed in redirects to `/account`.
- [ ] After Sign out on `/account`, signing in as guest again keeps the earlier profile edits.
- [ ] The navbar and footer match `cart/index.html` exactly.
- [ ] Keyboard-only and screen-reader flows work, with visible focus and announced notices.
