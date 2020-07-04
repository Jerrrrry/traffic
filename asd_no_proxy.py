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

if __name__ == '__main__':
    while 1:
        url = 'https://www.asdscuba.com/zh/home'
        # 无限循环
        # 使用chrome自定义
        options = webdriver.ChromeOptions()
        # 设置代理
        ua = UserAgent()
        a = ua.random
        user_agent = ua.random
        print(user_agent)
        options.add_argument("--headless")
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
        