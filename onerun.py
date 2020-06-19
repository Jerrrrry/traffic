
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
# 随机获取浏览器标识
def get_UA():
    UA_list = [
        "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
        #"Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        #"Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    ]
    randnum = random.randint(0, len(UA_list)-1)
    h_list = UA_list[randnum]
    return h_list

def get_URL():
    URL_list=[
        'https://www.cannabiszealot.com/marijuana-strains/dark-star',
        'https://www.cannabiszealot.com/',
        'https://www.cannabiszealot.com/marijuana-strains/buddhas-sister',
        'https://www.cannabiszealot.com/marijuana-strains/ak-47',
        'https://www.cannabiszealot.com/marijuana-strains/ak-48',
        'https://www.cannabiszealot.com/marijuana-strains/americano',
        'https://www.cannabiszealot.com/marijuana-strains/bc-blueberry',
        'https://www.cannabiszealot.com/marijuana-strains/blueberry-northern-lights',
        'https://www.cannabiszealot.com/marijuana-strains/amnesia',
        'https://www.cannabiszealot.com/marijuana-strains/angel-heart',
        'https://www.cannabiszealot.com/marijuana-strains/aurora-indica',
        'https://www.cannabiszealot.com/marijuana-strains/blue-cheese'
    ]

    randnum = random.randint(0, len(URL_list)-1)
    h_list = URL_list[randnum]
    return h_list
 
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
 
 
if __name__ == '__main__':
    url = get_URL()
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
    options.add_argument(f'user-agent={user_agent}')
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
        time.sleep(45)
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
        
        