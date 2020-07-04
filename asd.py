#https://www.asdscuba.com/zh/home
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

 
# 获取代理IP
def get_ip():
    try:
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
    except:
        print('no ip available')
        return ''
    finally:
        pass
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
        print(e)
        return ''
    finally:
        pass
 
 
if __name__ == '__main__':
    while 1:
        url = "https://www.asdscuba.com/zh/home"
        # 无限循环
        # 调用函数获取浏览器标识, 字符串
        #headers = get_UA()
        # 调用函数获取IP代理地址,这里获取是字符串，而不是像前两个教程获得的是数组
        proxy = get_ip()
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
        # 设置UA
        options.add_argument('--user-agent="'+user_agent+'"')
        #options.add_argument('--user-agent="'+headers+'"')
        #options.add_argument("--headless")
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
            time.sleep(60)
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
        
