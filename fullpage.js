/**
 * @name get title
 *
 * @desc Get the title of a page and print it to the console.
 *
 * @see {@link https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#pagetitle}
 */
const puppeteer = require('puppeteer');
const axios = require('axios');
let jsonData = require('./cred.json');

const sleep=time=>{
  return new Promise(resolve=>{
    setTimeout(resolve,time)
  })
}

axios.get('https://api.getproxylist.com/proxy?country[]=US&protocol[]=socks4&apiKey='+jsonData.token)
  .then(response => {
    const proxy=response.data
    console.log(response.data);
    //

    (async () => {
      try{
        const url='socks4://'+proxy.ip+':'+proxy.port

        let launchOptions = {
          args: [
            '--start-maximized',
            '--proxy-server='+url,
            '--no-sandbox',
            '--headless',
            '--disable-gpu',
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

        for (let i=0;i<hrefs.length;i++)
        {
          let rs=hrefs[i]
          await page.goto(rs, {
                      waitUntil: 'networkidle2',
                      timeout: 0
                  })
          console.log(await page.title())
          await sleep(3000)
          await page.goBack();
        }


        // get the User Agent on the context of Puppeteer
        const userAgent = await page.evaluate(() => navigator.userAgent );

        // If everything correct then no 'HeadlessChrome' sub string on userAgent
        console.log(userAgent);
        await browser.close()
      }catch(error){
        console.log(error)

      }


    })()

  })
  .catch(error => {
    const proxy=''
  });
