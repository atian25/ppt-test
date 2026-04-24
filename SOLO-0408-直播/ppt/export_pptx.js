const puppeteer = require('puppeteer');
const pptxgen = require('pptxgenjs');
const path = require('path');
const fs = require('fs');

async function exportPptx() {
    const url = 'http://localhost:8000/index.html';
    const tempDir = path.join(__dirname, 'temp_slides');
    
    if (!fs.existsSync(tempDir)){
        fs.mkdirSync(tempDir);
    }

    console.log('Launching browser...');
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    
    // Set viewport to a standard 16:9 presentation size
    await page.setViewport({ width: 1920, height: 1080 });
    
    console.log('Navigating to PPT...');
    await page.goto(url, { waitUntil: 'networkidle0' });
    
    // Wait a bit for fonts and WebGL to fully render
    await new Promise(r => setTimeout(r, 2000));
    
    // Get total number of slides
    const totalSlides = await page.evaluate(() => {
        return document.querySelectorAll('.slide').length;
    });
    
    console.log(`Found ${totalSlides} slides. Capturing screenshots...`);
    
    const slideImages = [];
    
    for (let i = 0; i < totalSlides; i++) {
        console.log(`Capturing slide ${i + 1}/${totalSlides}...`);
        
        // Use the 'go(n)' function defined in the HTML to switch slides
        await page.evaluate((index) => {
            window.go(index);
        }, i);
        
        // Wait for transition animation (transition is 0.9s, so wait 1.2s to be safe)
        await new Promise(r => setTimeout(r, 1200));
        
        const imagePath = path.join(tempDir, `slide_${i}.png`);
        await page.screenshot({ path: imagePath });
        slideImages.push(imagePath);
    }
    
    await browser.close();
    
    console.log('Generating PPTX...');
    let pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9';
    
    for (let i = 0; i < slideImages.length; i++) {
        let slide = pptx.addSlide();
        slide.addImage({ 
            path: slideImages[i], 
            x: 0, 
            y: 0, 
            w: '100%', 
            h: '100%' 
        });
    }
    
    const outputPath = path.join(__dirname, 'SOLO_0418_直播.pptx');
    await pptx.writeFile({ fileName: outputPath });
    
    console.log(`PPTX generated successfully at ${outputPath}`);
    
    // Clean up temp images
    for (const img of slideImages) {
        fs.unlinkSync(img);
    }
    fs.rmdirSync(tempDir);
}

exportPptx().catch(console.error);
