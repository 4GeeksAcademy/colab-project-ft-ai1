> #### 1) Home page
>
> - **Top bar (navbar)** with:
>   - Logo
>   - Search bar
>   - User account menu
> - **Hero section** highlighting special products or brand campaigns.
> - Two sections with horizontal product lists (_cards_):
>   - **New arrivals**
>   - **Best sellers**
> - **Footer** with sections:
>   - **Categories:** footwear, shirts, pants, accessories
>   - **Legal:** terms and conditions, privacy policy, about the brand
>   - **Contact**
> - **The navbar and footer are reused** across all other views.
>
> #### 2) Catalog
>
> - Keeps **navbar and footer**.
> - Includes a **filter bar** before the list:
>   - Filter by **category**
>   - Filter by **size**
> - Product list in a **4×5 grid** (20 products visible as reference).
>
> #### 3) Product view
>
> - Two-column layout:
>   - **Left:** product image taking roughly **half the width**.
>   - **Right:** main product information:
>     - Name
>     - Code or reference
>     - Size
>     - Price
>     - Quantity selector
>     - **"Add to cart"** button
> - Below, a **detailed description** section:
>   - Materials
>   - Recommended use / scenarios for wearing the item
>
> #### 4) Cart
>
> - Full cart view (not a side panel).
> - List of added products with:
>   - Thumbnail
>   - Unit price
>   - Quantity
>   - Total per product
> - Summary box with:
>   - Subtotal
>   - Tax
>   - Total
>   - **"Purchase"** button
> - Add **3 sample products** to show the visual behavior.
>
> #### 5) Payment form (Checkout)
>
> Flow in **3 steps**:
>
> 1. **Personal details**
> 2. **Shipping address**
> 3. **Card payment** (card details)
>
> #### 6) Profile (My account)
>
> - Keeps **navbar and footer**; opened from **"My account"** when signed in.
> - Side menu with sections: **Overview**, **Orders**, **Addresses**, **Payment methods**, **Account details**, **Sign out**.
> - Shows the **guest account's** sample orders, address, and card.
> - Full spec: `profile/PROFILE_SPEC.md`.
>
> #### 7) Sign in
>
> - Keeps **navbar and footer**; opened from **"My account"** when signed out.
> - Email and password form, plus a **"Sign in to guest profile"** button.
> - Full spec: `profile/SIGN_IN_SPEC.md`.
