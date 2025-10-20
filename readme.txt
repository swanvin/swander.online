====================================================
   SWANDER.Online Deployment Guide
   (HTML + CSS Static Site)
====================================================

Project Summary:
----------------
SWANDER ($SWND) is a meme coin website designed for 
a fast, viral launch on Solana. This bundle includes:

  • index.html          → main static site
  • style.css           → site styles
  • /assets/            → put your logo, poster, stickers here
  • /animated/          → optional animated version
  • README.txt          → you’re reading it!

----------------------------------------------------
1️⃣  Local Setup
----------------------------------------------------
1. Create a folder named swander_online on your computer.
2. Save index.html, style.css, and README.txt into it.
3. Create a subfolder called assets and add:
     - logo.png
     - poster.png
     - sticker1.png ... sticker5.png
4. (Optional) Create another folder called animated
   and later place your animated launch version there.

----------------------------------------------------
2️⃣  Editing the Contract Link
----------------------------------------------------
Once your token is created on Pump.fun / Moonshot:

1. Copy your SWANDER contract address or Raydium link.
2. Open index.html with a text editor.
3. Find this line:

   <!-- Paste your SWANDER contract address here once it’s live -->

4. In the <a href="#">Buy $SWND</a> and CTA buttons, 
   replace the "#" with your live link, like:

   <a href="https://raydium.io/swap/?input=SOL&output=SWND">Buy $SWND</a>

5. Save the file.

----------------------------------------------------
3️⃣  Deploying via GitHub Pages (Free)
----------------------------------------------------
1. Go to https://github.com and sign in.
2. Create a new repository named swander.online.
3. Upload all your files (index.html, style.css, etc.).
4. Click "Settings" → "Pages" in the sidebar.
5. Under "Source", choose "Deploy from a branch" → "main" → "/ (root)".
6. Click Save.
7. In 1–2 minutes you’ll get a link like:
      https://<yourusername>.github.io/swander.online
8. Visit that link — your site is live!

To use your own domain:
  - Buy swander.online from your registrar.
  - In your DNS settings, create an A record:
        Host: @
        Value: 185.199.108.153
  - In GitHub Pages settings, add "swander.online" as a custom domain.
  - GitHub automatically provides SSL (https).

----------------------------------------------------
4️⃣  Deploying via Vercel (Alternative, Easy)
----------------------------------------------------
1. Go to https://vercel.com and log in with GitHub.
2. Click “New Project” → import the swander.online repo.
3. Click “Deploy”.
4. In 1 minute you’ll get a live URL like:
      https://swander-online.vercel.app
5. Click "Add Domain" and enter swander.online.
6. Vercel will prompt you to update DNS automatically.

----------------------------------------------------
5️⃣  Updating Content
----------------------------------------------------
• To change images: replace the files in /assets/.
• To edit text: open index.html and update paragraphs.
• To change colors or fonts: edit style.css.

----------------------------------------------------
6️⃣  Troubleshooting
----------------------------------------------------
• Blank page? Make sure filenames match exactly.
• Styles missing? Ensure "style.css" is in same folder as index.html.
• DNS not connecting? Double-check A-record or wait up to 1 hour.

----------------------------------------------------
7️⃣  Support Notes
----------------------------------------------------
No personal info or contact links are included.
This site is static and safe to host anywhere.
All memes belong to the flock 🦢

© 2025 SWANDER
