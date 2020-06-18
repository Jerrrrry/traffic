install python3

pip3 install selenuim

pip3 install webdriver_manager

from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install()) 

pip3 install fake_useragent

ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)

