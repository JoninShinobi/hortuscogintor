# Hey Eloise Font Installation Guide

The website is designed to use the **Hey Eloise** font. Here are your options for installing it:

## Option 1: Adobe Fonts (Recommended for Commercial Use)

If you have Adobe Creative Cloud:

1. Go to [Adobe Fonts](https://fonts.adobe.com/fonts/hey-eloise)
2. Sign in with your Adobe ID
3. Click "Add to Web Project" 
4. Create a new web project or add to existing
5. Copy the provided embed code
6. Add it to `templates/base.html` in the `<head>` section:
   ```html
   <link rel="stylesheet" href="https://use.typekit.net/YOUR-KIT-ID.css">
   ```

## Option 2: Purchase from Tart Workshop

For commercial use without Adobe CC:
- Visit [Tart Workshop](https://tartworkshop.com) to purchase a license
- Download the font files
- Place them in `/static/fonts/` directory

## Option 3: Use the Free Fallback Fonts (Already Configured)

The website is already configured with similar free Google Fonts as fallbacks:
- **Kalam** - Primary fallback (handwritten style)
- **Patrick Hand** - Secondary fallback
- **Caveat** - Tertiary fallback

These will automatically be used if Hey Eloise is not available.

## Installing Font Files Locally

If you have the Hey Eloise font files:

1. Obtain the font files in these formats (in order of preference):
   - `.woff2`
   - `.woff` 
   - `.ttf` or `.otf`

2. Place the files in: `/static/fonts/`

3. Name them:
   - `HeyEloise.woff2`
   - `HeyEloise.woff`
   - `HeyEloise.ttf`

4. The CSS is already configured to use these files automatically

## Current Font Stack

The website uses this font priority:
1. Hey Eloise (if installed)
2. Kalam (Google Font - automatically loaded)
3. Patrick Hand (Google Font - automatically loaded)
4. Caveat (Google Font - automatically loaded)
5. Generic cursive fallback

## Testing

To verify the font is working:
1. Run the server: `./run_server.sh`
2. Visit: http://127.0.0.1:8080
3. Check the navigation menu and headings - they should display in the decorative font

## Note on Licensing

- **Hey Eloise** is a commercial font
- Adobe Fonts subscription allows web use
- Direct purchase from Tart Workshop for self-hosting
- The fallback fonts (Kalam, Patrick Hand, Caveat) are free for all uses via Google Fonts