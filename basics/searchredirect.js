// https://www.google.com/search?q=cannabis+zealot&rlz=1C1CHBF_enUS819US819&oq=cannabis+zealot+&aqs=chrome.0.69i59l2j69i60l3.4816j0j7&sourceid=chrome&ie=UTF-8

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
  //const iPhone = puppeteer.devices['iPhone 6'];
  await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36');
  //await page.emulate(iPhone)
  await page.goto('https://www.google.com/search?rlz=1C1CHBF_enUS819US819&ei=_MG9Xt28JOy-0PEP9viOyAo&q=cannabis+zealot+durga&oq=cannabis+zealot+durga&gs_lcp=CgZwc3ktYWIQAzoECAAQRzoFCCEQoAE6BQghEKsCULyRggFYm62CAWDDr4IBaABwAXgAgAF1iAG-BJIBAzUuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjdqoLKr7TpAhVsHzQIHXa8A6kQ4dUDCAw&uact=5')
  const title = await page.title()
  console.log(title)

  // get the User Agent on the context of Puppeteer
  const userAgent = await page.evaluate(() => navigator.userAgent );
//  const stories = await page.$$eval('.r.a', anchors => { return anchors.map(anchor => anchor.textContent).slice(0, 10) })

  //const ah = await page.$eval('.r.a', el => el.innerHTML)

  const hrefs = await page.evaluate(() => {
    const anchors = document.querySelectorAll('a');
    return [].map.call(anchors, a => a.href);
  });

  // If everything correct then no 'HeadlessChrome' sub string on userAgent

  const results=[]

  hrefs.forEach(function(item){
    if(item.startsWith('https://www.cannabiszealot.com/')){
       results.push(item)
    }
  });

  if(results.length>0)
  {
    console.log(results[0])
    await page.goto(results[0])
  }

  await browser.close()
})()
