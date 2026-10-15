// Check the generated website and actual responsive layout without opening a desktop window.
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require('playwright');

async function main() {
  const root = path.resolve(__dirname, '..', 'docs');
  const out = path.resolve(process.argv[2] || '.local/site-review');
  const only = process.argv[3] ? process.argv[3].split(',') : null;
  fs.mkdirSync(out, { recursive: true });
  const failures = [], records = [];
  const server = http.createServer((req, res) => {
    const name = path.resolve(root, '.' + decodeURIComponent(req.url.split('?')[0]));
    if (!name.startsWith(root + path.sep) || !fs.existsSync(name) || !fs.statSync(name).isFile()) {
      res.writeHead(404); return res.end();
    }
    const ext = path.extname(name);
    res.setHeader('Content-Type', ({'.html':'text/html; charset=utf-8','.css':'text/css','.js':'application/javascript','.webp':'image/webp','.png':'image/png','.svg':'image/svg+xml'})[ext] || 'application/octet-stream');
    fs.createReadStream(name).pipe(res);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = 'http://127.0.0.1:' + server.address().port;
  const browser = await chromium.launch({ headless: true, channel: 'msedge' });
  try {
    const page = await browser.newPage();
    const languages = ['ko', 'en', 'ja', 'zh'];
    for (const lang of languages) {
    const names = fs.readdirSync(path.join(root, lang)).filter(n => n.endsWith('.html') && (!only || only.includes(n)));
    for (const width of [1440, 900, 390]) {
      await page.setViewportSize({ width, height: 1000 });
      for (const name of names) {
        const errors = [];
        const onError = e => errors.push(e.message);
        page.on('pageerror', onError);
        await page.goto(base + '/' + lang + '/' + name, { waitUntil: 'load' });
        const result = await page.evaluate(async () => {
          const main = document.querySelector('main');
          const missing = [], images = [];
          for (const image of document.querySelectorAll('article img')) {
            image.loading = 'eager';
            try { await image.decode(); } catch (_) { missing.push(image.getAttribute('src')); }
            images.push({alt:image.alt, width:image.clientWidth, natural:image.naturalWidth});
          }
          const brokenLinks = [];
          for (const a of document.querySelectorAll('a[href^="#"]')) {
            const id = decodeURIComponent(a.getAttribute('href').slice(1));
            if (id && !document.getElementById(id)) brokenLinks.push(id);
          }
          const clippedLabels = [...document.querySelectorAll('.settings-table td:first-child')]
            .filter(cell => cell.scrollWidth > cell.clientWidth + 1).map(cell => cell.innerText);
          return {title:document.title, overflow:document.documentElement.scrollWidth > innerWidth + 1,
            rawMarkdown:!!main && main.innerText.includes('**'), missing, brokenLinks, clippedLabels, images};
        });
        page.off('pageerror', onError);
        const record = {lang, width, page:name, ...result, errors};
        records.push(record);
        if (result.overflow || result.rawMarkdown || result.missing.length || result.brokenLinks.length || result.clippedLabels.length || errors.length) failures.push(record);
        if (['01-getting-started.html','08-scene.html','08-camera-effects.html','09-session.html','13-license.html'].includes(name)) {
          await page.screenshot({path:path.join(out, lang+'-'+width+'-'+name.replace('.html','.png'))});
        }
        if (name === '08-camera-effects.html') {
          const anchor = page.locator('article img[src$="/guide-post-aa.webp"]').first();
          await anchor.scrollIntoViewIfNeeded();
          await page.screenshot({path:path.join(out,lang+'-'+width+'-antialiasing.png')});
          const rects = await page.locator('td').filter({hasText:/^안티에일리어싱$/}).count();
          if (rects) throw new Error('Expected effect-specific explanations, not the obsolete crowded table');
        }
      }
    }
    console.log('Checked ' + lang + ': ' + names.length + ' pages at 3 widths');
    }
    fs.writeFileSync(path.join(out,'layout-results.json'),JSON.stringify({failures, records},null,2));
    console.log(JSON.stringify({languages:languages.length,pages:records.length/3,viewports:3,checks:records.length,failures:failures.map(f=>({lang:f.lang,page:f.page,width:f.width,missing:f.missing,brokenLinks:f.brokenLinks,overflow:f.overflow,clippedLabels:f.clippedLabels,errors:f.errors}))},null,2));
    if (failures.length) process.exitCode=1;
  } finally {
    server.closeAllConnections();
    await browser.close();
    await new Promise(resolve=>server.close(resolve));
  }
}
main().catch(error => {console.error(error);process.exitCode=1;});
