# Academic Portfolio Website

An academic portfolio website based on Jon Barron's template, featuring your research papers and professional information.

## 📁 Project Structure

```
.
├── index.html          # Main HTML file
├── stylesheet.css      # CSS styling
├── bibtex/            # BibTeX citations
│   └── astrodiff.bib
└── images/            # Images folder
    ├── profile.jpg         # Your profile photo
    ├── astrodiff_before.jpg # Paper image (before)
    ├── astrodiff_after.jpg  # Paper image (after)
    ├── tsdsr.jpg           # TSD-SR paper image
    └── purdue_logo.png     # Institution logo
```

## 🚀 Deployment Instructions

### Option 1: GitHub Pages (Free & Easy)

1. **Create a GitHub Repository**
   ```bash
   # Create a new repository named "yourusername.github.io"
   # This will be your personal GitHub Pages site
   ```

2. **Upload Files**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/yourusername.github.io.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to Settings → Pages
   - Source: Deploy from branch
   - Branch: main, folder: / (root)
   - Save

4. **Access Your Site**
   - Your website will be live at: `https://yourusername.github.io`
   - Changes pushed to main branch auto-deploy

### Option 2: Netlify (Free with More Features)

1. **Prepare Files**
   - Put all files in a folder
   - Zip the folder

2. **Deploy to Netlify**
   - Go to [Netlify Drop](https://app.netlify.com/drop)
   - Drag and drop your folder
   - Site instantly deployed!

3. **Custom Domain (Optional)**
   - In Netlify dashboard → Domain settings
   - Add custom domain

### Option 3: University/Institution Hosting

Many universities provide web hosting for students:

1. **Check Your Institution's Policy**
   - Usually at: `www.university.edu/~yourusername/`
   
2. **Upload via SFTP/SSH**
   ```bash
   # Example for Purdue (adjust for your institution)
   scp -r * yourusername@data.cs.purdue.edu:~/public_html/
   ```

3. **Set Permissions**
   ```bash
   chmod 755 ~/public_html
   chmod 644 ~/public_html/*
   ```

## 🎨 Customization Guide

### Essential Updates

1. **Personal Information (index.html)**
   - Replace "Joonyeoup Kim" with your name
   - Update bio paragraphs
   - Update email address
   - Add your Google Scholar, GitHub, LinkedIn links

2. **Images Required**
   
   Create these images and place in `images/` folder:
   
   - `profile.jpg` - Your professional photo (square, ~500x500px)
   - `astrodiff_before.jpg` - Turbulent/blurry astronomical image (160x160px)
   - `astrodiff_after.jpg` - Restored/clear astronomical image (160x160px)
   - `tsdsr.jpg` - Aerial image for TSD-SR paper (160x160px)
   - `purdue_logo.png` - Your institution logo (160x60px)

3. **Paper Details**
   - Update paper titles, authors, venues
   - Add actual links to code repositories
   - Update paper descriptions

### Creating Paper Preview Images

For the hover effect on your AstroDiff paper:

1. **Before Image** (`astrodiff_before.jpg`)
   - Show a turbulent/blurry astronomical image
   - Resize to 160x160px
   
2. **After Image** (`astrodiff_after.jpg`)
   - Show the restored/clear version
   - Same dimensions (160x160px)

Example using ImageMagick:
```bash
# Resize images
convert original_before.jpg -resize 160x160^ -gravity center -crop 160x160+0+0 astrodiff_before.jpg
convert original_after.jpg -resize 160x160^ -gravity center -crop 160x160+0+0 astrodiff_after.jpg
```

### Adding More Papers

To add a new paper, copy this template into the papers section:

```html
<tr>
  <td style="padding:20px;width:25%;vertical-align:middle">
    <div class="one">
      <img src='images/your_paper.jpg' width="160">
    </div>
  </td>
  <td style="padding:20px;width:75%;vertical-align:middle">
    <a href="PAPER_URL">
      <span class="papertitle">Your Paper Title</span>
    </a>
    <br>
    <strong>Your Name</strong>, Co-authors
    <br>
    <em>Conference/Journal</em>, Year
    <br>
    <a href="ARXIV_URL">arXiv</a>
    /
    <a href="CODE_URL">Code</a>
    /
    <a href="bibtex/your_paper.bib">BibTeX</a>
    <p></p>
    <p>
      Brief description of your paper's contribution.
    </p>
  </td>
</tr>
```

### Adding Sections

You can add more sections like:
- **News/Updates**
- **Awards & Honors**
- **Talks & Presentations**
- **Service**
- **Blog Posts**

Example News section:
```html
<table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
  <tr>
    <td style="padding:20px;width:100%;vertical-align:middle">
      <h2>News</h2>
      <ul>
        <li>[Jun 2024] Paper accepted to arXiv!</li>
        <li>[May 2024] Started internship at Company X</li>
      </ul>
    </td>
  </tr>
</tbody></table>
```

## 📱 Mobile Responsiveness

The template is mobile-friendly by default. The viewport meta tag ensures proper scaling:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

## 🔍 SEO Optimization

Add these meta tags for better search engine visibility:

```html
<meta name="description" content="Academic portfolio of [Your Name], featuring research in computer vision and image restoration">
<meta name="keywords" content="computer vision, image restoration, diffusion models, astronomical imaging">
<meta property="og:title" content="Your Name - Academic Portfolio">
<meta property="og:description" content="Research in computer vision and image restoration">
<meta property="og:image" content="https://yoursite.com/images/profile.jpg">
```

## 📧 Contact Form (Optional)

To add a contact form, you can use [Formspree](https://formspree.io/):

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <input type="email" name="email" placeholder="Your email">
  <textarea name="message" placeholder="Your message"></textarea>
  <button type="submit">Send</button>
</form>
```

## 🎯 Quick Start Checklist

- [ ] Replace all placeholder text with your information
- [ ] Add your profile photo (images/profile.jpg)
- [ ] Create paper preview images (160x160px)
- [ ] Update all social media links
- [ ] Add your institution logo
- [ ] Update paper descriptions and links
- [ ] Test all links work correctly
- [ ] Deploy to hosting platform
- [ ] Share your website URL!

## 📝 License

This template is based on [Jon Barron's website](https://jonbarron.info/). Feel free to use and modify for your own academic portfolio.

## 🆘 Troubleshooting

**Images not showing?**
- Check file paths are correct (case-sensitive on Linux servers)
- Ensure images are in the `images/` folder
- Verify image file extensions match HTML references

**Fonts not loading?**
- The Lato font loads from Google Fonts CDN
- If blocked, fonts will fallback to Verdana/Helvetica

**GitHub Pages not updating?**
- Check Actions tab for deployment status
- Clear browser cache (Ctrl+Shift+R)
- Wait 5-10 minutes for changes to propagate

## 💡 Tips

1. **Keep it Updated**: Add new papers and achievements regularly
2. **High-Quality Images**: Use clear, professional images
3. **Concise Descriptions**: Keep paper descriptions brief but informative
4. **Test Responsiveness**: Check on mobile devices
5. **Analytics**: Add Google Analytics to track visitors

---

Created with the template from [Jon Barron](https://jonbarron.info/)