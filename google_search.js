const puppeteer = require('puppeteer');
const axios=require('axios');
const jsonData = require('./cred.json');
const iPhone = puppeteer.devices['iPhone 6'];
const sleep=time=>{
  return new Promise(resolve=>{
    setTimeout(resolve,time)
  })
}


 //start one ip and one brwoser
 const oneRun = async _ => {
    console.log('Start')
    //start one ip and one brwoser
    await axios.get('https://api.getproxylist.com/proxy?country[]=US&lastTested=600&maxConnectTime=1&protocol[]=socks4&apiKey='+jsonData.token)
    .then(response => {
      const proxy=response.data
      console.log(response.data);
      //
  
      (async () => {
       
          const url='socks4://'+proxy.ip+':'+proxy.port
  
          let launchOptions = {
            headless:false,
            args: [
              '--no-sandbox',
              '--disable-setuid-sandbox',
              '--start-maximized',
              '--proxy-server='+url
            ] // this is where we set the proxy    socks4://67.204.1.222:64312
          };
          const browser = await puppeteer.launch(launchOptions)
          try{
            const page = await browser.newPage()
            //await page.emulate(iPhone);
            await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36');
            
            await page.goto('https://www.google.com/', {
                          waitUntil: 'networkidle2',
                          timeout: 0
            })    
            const title = await page.title()
            await page.type('input.gLFyf.gsfi', '洛杉矶潜水课程');
			page.keyboard.press('Enter');
           
            await sleep(20000)
            const userAgent = await page.evaluate(() => navigator.userAgent );
            // If everything correct then no 'HeadlessChrome' sub string on userAgent
            console.log(userAgent);
            await browser.close()
          }catch(error){
            console.log(error)
          }finally{
            await browser.close()
          }
        
  
  
      })()
  
    })
    .catch(error => {
        const proxy=''
    });
    console.log('End')
  }
  
  oneRun()