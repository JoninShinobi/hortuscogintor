# Django Unfold Text Visibility Fix

## Problem
Text appearing as "white on white" or invisible in Django Unfold admin interface, affecting both light and dark themes.

## Root Cause
Using incorrect CSS selectors `html[data-theme="dark"]` instead of Unfold's actual class-based theme system `html.dark`.

## Solution Location
File: `static/css/unfold_custom.css`

## Solution Implementation
Dual-theme CSS approach:

```css
/* DARK THEME SPECIFIC TEXT FIXES */
html.dark #content label,
html.dark #content .form-row label,
html.dark #content td,
html.dark #content th {
    color: rgb(229 231 235) !important; /* Light gray for dark backgrounds */
}

/* LIGHT THEME FIXES - for white on white text issue */
html:not(.dark) #content label,
html:not(.dark) #content .form-row label,
html:not(.dark) #content td,
html:not(.dark) #content th {
    color: rgb(17 24 39) !important; /* Dark gray for light backgrounds */
}

/* NUCLEAR OPTION - Force all text to be visible regardless of theme */
label,
td, th,
.results td, .results th,
table td, table th {
    color: rgb(17 24 39) !important;
}
```

## Key Learning
Unfold uses Alpine.js class binding (`x-bind:class="{'dark': ...}"`) not data attributes for theme switching.

## Color References
- Dark theme text: `rgb(229 231 235)` - light gray for dark backgrounds
- Light theme text: `rgb(17 24 39)` - dark gray for light backgrounds
- Help text dark: `rgb(156 163 175)` - medium gray
- Help text light: `rgb(107 114 128)` - medium gray