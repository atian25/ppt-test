const fs = require('fs');
const cheerio = require('cheerio');
const pptxgen = require('pptxgenjs');
const path = require('path');

async function createPPTX() {
    const htmlContent = fs.readFileSync('index.html', 'utf-8');
    const $ = cheerio.load(htmlContent);
    const slides = $('.slide');

    let pres = new pptxgen();
    pres.layout = 'LAYOUT_16x9';
    pres.author = 'SOLO';
    pres.title = 'SOLO 0418 直播 — 正文';

    slides.each((index, element) => {
        let slide = pres.addSlide();
        
        // Check background theme
        const isDark = $(element).hasClass('dark');
        slide.background = { fill: isDark ? "0a0a0b" : "f1efea" };
        const textColor = isDark ? "f1efea" : "0a0a0b";
        const secondaryColor = isDark ? "cccccc" : "555555";

        // Extract kicker
        const kicker = $(element).find('.kicker').text().trim();
        if (kicker) {
            slide.addText(kicker, { x: 0.5, y: 0.5, w: 9, h: 0.5, fontSize: 14, color: secondaryColor, charSpacing: 2 });
        }

        // Extract Hero title or large headers
        let title = $(element).find('.h-hero, .h-xl').first().text().trim() || $(element).find('.h3-zh').first().text().trim();
        if (title) {
            slide.addText(title, { 
                x: 0.5, y: kicker ? 1.2 : 1.0, 
                w: 9, h: 1.5, 
                fontSize: 48, 
                color: textColor, 
                bold: true,
                breakLine: true
            });
        }

        // Extract lead / body text
        const lead = $(element).find('.lead').text().trim();
        const body = $(element).find('.body-zh').text().trim();
        const content = lead || body;
        
        if (content) {
            slide.addText(content, { 
                x: 0.5, y: title ? 2.5 : 1.8, 
                w: 8.5, h: 1.5, 
                fontSize: 18, 
                color: secondaryColor,
                breakLine: true
            });
        }

        // Extract stats if any
        const statCards = $(element).find('.stat-card');
        if (statCards.length > 0) {
            let startX = 0.5;
            statCards.each((idx, statEl) => {
                const label = $(statEl).find('.stat-label').text().trim();
                const nb = $(statEl).find('.stat-nb').text().trim();
                const note = $(statEl).find('.stat-note').text().trim();

                // Adjusted sizes and heights to prevent overlapping
                slide.addText(nb, { x: startX, y: 3.2, w: 2.2, h: 0.8, fontSize: 32, bold: true, color: textColor, breakLine: true });
                slide.addText(label, { x: startX, y: 4.1, w: 2.2, h: 0.4, fontSize: 14, color: secondaryColor });
                if (note) {
                    slide.addText(note, { x: startX, y: 4.5, w: 2.2, h: 0.4, fontSize: 10, color: secondaryColor });
                }
                startX += 2.4;
            });
        }

        // Extract Callout / Quotes
        const quote = $(element).find('.q-big').text().trim();
        if (quote) {
            slide.addText(`"${quote}"`, {
                x: 0.5, y: title ? 3.5 : 2.5,
                w: 8, h: 1.5,
                fontSize: 28,
                italic: true,
                color: textColor
            });
        }
        
        // Extract local Images
        const img = $(element).find('img').first();
        if (img.length > 0) {
            const imgSrc = img.attr('src');
            // If it's a local path like images/01-slide-image.png
            if (imgSrc && !imgSrc.startsWith('http')) {
                const localImgPath = path.join(__dirname, imgSrc);
                if (fs.existsSync(localImgPath)) {
                    slide.addImage({ path: localImgPath, x: 5.5, y: 1.5, w: 4.2, h: 2.36 });
                }
            }
        }
    });

    const outPath = 'SOLO_0418_直播.pptx';
    await pres.writeFile({ fileName: outPath });
    console.log(`Generated ${outPath}`);
}

createPPTX().catch(console.error);
