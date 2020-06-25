import random
import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import sys
import os
import json
import pickle


def get_token():
    with open('cred.json') as json_file:
        data = json.load(json_file)
        return data['token']
# 随机获取浏览器标识

 
# 获取代理IP
def get_ip():
    # 这里填写大象代理api地址，num参数必须为1，每次只请求一个IP地址
    token=get_token()
    url = 'https://api.getproxylist.com/proxy?country[]=US&lastTested=600&maxConnectTime=1&protocol[]=socks4&apiKey='+token
    response = requests.get(url)
    response.close()
    
    ip = response.json()['ip']
    port=str(response.json()['port'])
    result='socks4://'+ip+':'+port
    print(result)
    return result
 
 
if __name__ == '__main__':
    url = "https://www.google.com/search?q=洛杉矶潜水&oq=洛杉矶潜水"
    # 无限循环，每次都要打开一个浏览器窗口，不是标签
    # 调用函数获取浏览器标识, 字符串
    proxy = get_ip()
        # 使用chrome自定义
    options = webdriver.ChromeOptions()
        # 设置代理
    ua = UserAgent()
    a = ua.random
    user_agent = ua.random
    print(user_agent)
    #options.add_argument("--headless")
    if proxy!='':
        options.add_argument('--proxy-server='+proxy) 
    # 设置UA
    options.add_argument('--user-agent="'+user_agent+'"') 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    #options.add_argument("--profile-directory=Default");
        # 使用设置初始化webdriver
    #driver=webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
    #driver=webdriver.Opera(executable_path=OperaDriverManager().install(), options=chrome_options)
    

    
    
 
    try:
            # 访问超时30秒
        driver.set_page_load_timeout(30)
        
            # 访问网页
        
        driver.get('https://www.google.com/')
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(url)
        
       
        time.sleep(5)
            
            # 退出当前浏览器
        driver.close()
            # 延迟1~3秒继续
        time_delay = random.randint(1, 3)
        while time_delay > 0:
            print(str(time_delay) + " seconds left!!")
            time.sleep(1)
            time_delay = time_delay - 1
            pass
    except:
        print("timeout")
            # 退出浏览器
        driver.quit()
        time.sleep(1)
            # 重启脚本, 之所以选择重启脚本是因为，长时间运行该脚本会出现一些莫名其妙的问题，不如重启解决
        python = sys.executable
        os.execl(python, python, *sys.argv)
    finally:
        pass
        