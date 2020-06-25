import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
try:

    driver.get("http://www.google.com")
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

except:
    driver.close()
finally:
    pass