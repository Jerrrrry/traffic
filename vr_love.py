import random
import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
import sys
import os
import json
from fake_useragent import UserAgent


def get_token():
    with open('cred.json') as json_file:
        data = json.load(json_file)
        return data['token']

 
def get_proxy():
    try:
        token=get_token()
        url = 'https://api.getproxylist.com/proxy?country[]=US&lastTested=600&maxConnectTime=1&protocol[]=socks4&protocol[]=socks5&apiKey='+token
        response = requests.get(url)
        response.close()
        protocol=str(response.json()['protocol'])
        ip = response.json()['ip']
        port=str(response.json()['port'])
        result=protocol+'://'+ip+':'+port
        print(result)
        return result
    except:
        return ''
    finally:
        pass
 
 
if __name__ == '__main__':
    while 1:
        url = "https://loveplanet.today/post/best-vr-gaming-in-los-angeles"
        # 无限循环
        # 调用函数获取浏览器标识, 字符串
        #headers = get_UA()
        # 调用函数获取IP代理地址,这里获取是字符串，而不是像前两个教程获得的是数组
        proxy = get_proxy()
        # 使用chrome自定义
        options = webdriver.ChromeOptions()
        # 设置代理
        ua = UserAgent()
        a = ua.random
        user_agent = ua.random
        print(user_agent)
        options.add_argument("--headless")
        if proxy!='':
            options.add_argument('--proxy-server='+proxy) 
        options.add_argument('--user-agent="'+user_agent+'"')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
        try:
            # 访问超时30秒
            driver.set_page_load_timeout(30)
            # 访问网页
            driver.get(url)
            time.sleep(random.randint(1, 5))
            driver.find_element_by_link_text("website").click()
            time.sleep(random.randint(1, 5))

            driver.find_element_by_link_text("BOOK NOW").click()
            time.sleep(5)
            # 退出当前浏览器
            driver.quit()
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
        
