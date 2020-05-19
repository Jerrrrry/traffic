const puppeteer = require('puppeteer');

(async () => {
  let launchOptions = {
    args: [
      '--start-maximized',
      '--proxy-server=socks4://67.204.1.222:64312'
    ] // this is where we set the proxy    socks4://67.204.1.222:64312
  };
  try{
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36');
    await page.goto('http://free-proxy.cz/en/proxylist/country/US/socks/ping/all')
    const title = await page.title()
    const anchors = document.querySelectorAll('tr');
    console.log(anchors.length)
    // const hrefs = await page.evaluate(() => {
    //   const anchors = document.querySelectorAll('tr');
    //   console.log(anchors.length)
    //   //return [].map.call(anchors, a => a.href);
    // });


    console.log(title)

    // rs= hrefs[Math.floor(Math.random() *hrefs.length)];
    //
    // await page.goto(rs)
    // console.log(await page.title())
    // await page.goBack();
    //
    // rs= hrefs[Math.floor(Math.random() *hrefs.length)];
    // await page.goto(rs)
    // console.log(await page.title())
    // await page.goBack();



    // get the User Agent on the context of Puppeteer
    const userAgent = await page.evaluate(() => navigator.userAgent );

    // If everything correct then no 'HeadlessChrome' sub string on userAgent
    console.log(userAgent);
    await browser.close()
  }catch(error){
    console.log(error)
    await browser.close()
  }
})()
