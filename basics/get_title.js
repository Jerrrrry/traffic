/**
 * @name get title
 *
 * @desc Get the title of a page and print it to the console.
 *
 * @see {@link https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#pagetitle}
 */
const puppeteer = require('puppeteer');

(async () => {
  
    const args = process.argv.slice(2)
    let proxy=args[0]
    let launchOptions = {
      args: [
        '--start-maximized',
        '--proxy-server='+proxy
      ] // this is where we set the proxy    socks4://67.204.1.222:64312
    };
    const browser = await puppeteer.launch(launchOptions)
    const page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36');
    await page.goto('https://www.cannabiszealot.com/', {
                waitUntil: 'networkidle2',
                timeout: 0
            })
    const title = await page.title()

    const hrefs = await page.evaluate(() => {
      const anchors = document.querySelectorAll('.post-thumb>a');
      return [].map.call(anchors, a => a.href);
    });


    console.log(title)

    rs= hrefs[Math.floor(Math.random() *hrefs.length)];

    await page.goto(rs, {
                waitUntil: 'networkidle2',
                timeout: 0
            })
    console.log(await page.title())
    await page.goBack();

    rs= hrefs[Math.floor(Math.random() *hrefs.length)];
    await page.goto(rs, {
                waitUntil: 'networkidle2',
                timeout: 0
            })
    console.log(await page.title())
    await page.goBack();



    // get the User Agent on the context of Puppeteer
    const userAgent = await page.evaluate(() => navigator.userAgent );

    // If everything correct then no 'HeadlessChrome' sub string on userAgent
    console.log(userAgent);
    await browser.close()
})().catch(error=>{
    console.log("bad is "+error)
  }).then(()=>{
    console.log('in the end')
    await process.exit(1)
  })
