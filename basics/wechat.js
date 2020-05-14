/**
 * @name get title
 *
 * @desc Get the title of a page and print it to the console.
 *
 * @see {@link https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#pagetitle}
 */
const puppeteer = require('puppeteer');

(async () => {
  // let launchOptions = {
  //                        args: ['--start-maximized',
  //                               '--proxy-server=198.255.114.82'] // this is where we set the proxy
  // };
  const browser = await puppeteer.launch()
  const page = await browser.newPage()
  await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36');
  await page.goto('https://mp.weixin.qq.com/s/N3PglI5mC-zuG9Ic-mEjpw')
  const title = await page.title()
  const ah = await page.$eval('.rich_media_content', el => el.innerText)
  console.log(title)

  console.log(ah)


  await browser.close()
})()
