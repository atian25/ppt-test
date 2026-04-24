const fs = require('fs');
const cheerio = require('cheerio');
const pptxgen = require('pptxgenjs');
const path = require('path');

async function createPPTX() {
    const htmlContent = fs.readFileSync('index.html', 'utf-8');
    const $ = cheerio.load(htmlContent);
    const slides = $('.slide');

    let pres = new pptxgen();
    pres.layout = 'LAYOUT_16x9'; // 10 x 5.625 inches
    pres.author = 'SOLO';
    pres.title = 'SOLO 0418 直播 — 正文';

    slides.each((index, element) => {
        let slide = pres.addSlide();
        
        // Colors
        const isDark = $(element).hasClass('dark');
        const bgFill = isDark ? "1E1E1E" : "F9F9F7";
        const textMain = isDark ? "F9F9F7" : "1E1E1E";
        const textMuted = isDark ? "A0A0A0" : "666666";
        const textAccent = isDark ? "8AB4F8" : "0F52BA";
        
        slide.background = { fill: bgFill };

        // Top Chrome/Kicker
        const chromeLeft = $(element).find('.chrome > div').first().text().trim();
        const chromeRight = $(element).find('.chrome > div').last().text().trim();
        const kicker = $(element).find('.kicker').text().trim();

        if (chromeLeft) {
            slide.addText(chromeLeft.toUpperCase(), { x: 0.5, y: 0.3, w: 4, h: 0.3, fontSize: 10, color: textMuted, fontFace: 'Courier New' });
        }
        if (chromeRight) {
            slide.addText(chromeRight.toUpperCase(), { x: 5.5, y: 0.3, w: 4, h: 0.3, fontSize: 10, color: textMuted, align: 'right', fontFace: 'Courier New' });
        }

        let currentY = 1.0;

        // Is it a Hero slide? (Centered)
        const isHero = $(element).hasClass('hero');
        
        if (kicker && !isHero) {
            slide.addText(kicker, { x: 0.5, y: currentY, w: 9, h: 0.3, fontSize: 14, color: textAccent, bold: true });
            currentY += 0.4;
        }

        // Title
        let title = $(element).find('.h-hero, .h-xl').first().text().trim();
        if (title) {
            let fontSize = isHero ? 54 : 36;
            let titleY = isHero ? 2.0 : currentY;
            let titleAlign = isHero ? 'center' : 'left';
            slide.addText(title, { 
                x: 0.5, y: titleY, w: 9, h: 1.2, 
                fontSize: fontSize, color: textMain, bold: true, align: titleAlign,
                valign: 'top'
            });
            if (!isHero) currentY += 1.2;
        }

        // Subtitle (for hero)
        let sub = $(element).find('.h-sub').first().text().trim();
        if (sub && isHero) {
            slide.addText(sub, { x: 0.5, y: 3.3, w: 9, h: 0.5, fontSize: 24, color: textMuted, align: 'center' });
        }

        // Lead / Body
        const lead = $(element).find('.lead').text().trim();
        if (lead) {
            let leadY = isHero ? 4.0 : currentY;
            let leadAlign = isHero ? 'center' : 'left';
            slide.addText(lead, { 
                x: isHero ? 1.5 : 0.5, y: leadY, w: isHero ? 7 : 8.5, h: 1.0, 
                fontSize: 20, color: textMuted, align: leadAlign, valign: 'top'
            });
            if (!isHero) currentY += 1.0;
        }

        // Check layout types
        const hasGrid4 = $(element).find('.grid-4').length > 0;
        const hasGrid3 = $(element).find('.grid-3').length > 0;
        const hasSplit = $(element).find('.split').length > 0;
        const hasImg = $(element).find('img').length > 0;
        const hasCallout = $(element).find('.callout .q-big').length > 0;

        // Stat Cards
        const statCards = $(element).find('.stat-card');
        if (statCards.length > 0) {
            let cols = hasGrid4 ? 4 : (hasGrid3 ? 3 : statCards.length);
            let colWidth = 9.0 / cols;
            
            statCards.each((idx, statEl) => {
                const label = $(statEl).find('.stat-label').text().trim();
                const nb = $(statEl).find('.stat-nb').text().trim().replace(/\s+/g, ' '); // compress spaces
                const note = $(statEl).find('.stat-note').text().trim();

                let startX = 0.5 + (idx * colWidth);
                let statY = currentY + 0.2;

                // Label on top
                slide.addText(label.toUpperCase(), { x: startX, y: statY, w: colWidth - 0.2, h: 0.3, fontSize: 12, color: textMuted, bold: true });
                // Number
                slide.addText(nb, { x: startX, y: statY + 0.3, w: colWidth - 0.2, h: 0.8, fontSize: cols === 4 ? 28 : 40, color: textMain, bold: true });
                // Note
                if (note) {
                    slide.addText(note, { x: startX, y: statY + 1.1, w: colWidth - 0.2, h: 0.3, fontSize: 12, color: textMuted });
                }
            });
        }

        // Split columns (Before / After)
        if (hasSplit) {
            const cols = $(element).find('.split .col');
            cols.each((idx, colEl) => {
                const meta = $(colEl).find('.meta').text().trim();
                const h3 = $(colEl).find('.h3-zh').text().trim();
                const p = $(colEl).find('.body-zh').text().trim();

                let startX = 0.5 + (idx * 4.5);
                let splitY = currentY;

                if (meta) slide.addText(meta, { x: startX, y: splitY, w: 4, h: 0.3, fontSize: 12, color: textMuted, bold: true });
                if (h3) slide.addText(h3, { x: startX, y: splitY + 0.4, w: 4, h: 0.5, fontSize: 20, color: textMain, bold: true });
                if (p) slide.addText(p, { x: startX, y: splitY + 1.0, w: 4.2, h: 2.0, fontSize: 16, color: textMuted, valign: 'top' });
            });
        }

        // Image + Text
        if (hasImg && !hasSplit && statCards.length === 0) {
            // Text is already rendered as title/lead, let's adjust their width and add image
            // We will just place the image on the right
            const img = $(element).find('img').first();
            const imgSrc = img.attr('src');
            
            // Re-fetch body if it wasn't lead
            const body = $(element).find('.body-zh').text().trim();
            if (body) {
                slide.addText(body, { x: 0.5, y: currentY, w: 4.5, h: 2.5, fontSize: 18, color: textMuted, valign: 'top' });
            }

            if (imgSrc && !imgSrc.startsWith('http')) {
                const localImgPath = path.join(__dirname, imgSrc);
                if (fs.existsSync(localImgPath)) {
                    slide.addImage({ path: localImgPath, x: 5.2, y: 1.2, w: 4.3, h: 2.4 });
                }
            }
        }

        // Big Quote
        if (hasCallout && !hasImg) {
            const quote = $(element).find('.q-big').text().trim();
            const cite = $(element).find('.cite').text().trim();
            if (quote) {
                slide.addText(`"${quote}"`, {
                    x: 1.0, y: currentY + 0.5, w: 8, h: 1.5,
                    fontSize: 28, color: textMain, italic: true, valign: 'middle'
                });
            }
            if (cite) {
                slide.addText(`— ${cite}`, { x: 1.0, y: currentY + 2.2, w: 8, h: 0.4, fontSize: 16, color: textMuted });
            }
        }

        // Footer
        const footText = $(element).find('.foot > div').first().text().trim();
        if (footText && !isHero) {
            slide.addText(footText, { x: 0.5, y: 5.1, w: 4, h: 0.3, fontSize: 10, color: textMuted });
        }
    });

    const outPath = 'SOLO_0418_直播.pptx';
    await pres.writeFile({ fileName: outPath });
    console.log(`Generated ${outPath}`);
}

createPPTX().catch(console.error);
