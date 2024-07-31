#!/usr/bin/env python

import requests
import re
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
#from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import Scraping
from webdriver_manager.chrome import ChromeDriverManager

# Phone to email

#chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument("--headless")
#chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#chrome_options.add_experimental_option('useAutomationExtension', False)
#chrome_options.add_argument('--disable-blink-features=AutomationControlled')

def request_data(url, phonenumber):
    chrome_options = Options()
    # user_data = r"C:\\Users\\simra\\AppData\\Local\\Google\\Chrome\\User Data"
    user_data = r"C:\Users\ASUS\AppData\Local\Google\Chrome\User Data"
    profile_name = r"Default"
    
    # chrome_options.add_argument(r"user-data-dir="+str(user_data))
    # chrome_options.add_argument(r"profile-directory="+str(profile_name))
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=9222")  # This helps avoid the DevToolsActivePort error
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-features=EnableServiceWorkers")
    #chrome_options.add_argument("--incognito")
    srv = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service = srv, options=chrome_options)
    #stealth(driver,
     #   languages=["en-US", "en"],
      #  vendor="Google Inc.",
       # platform="Win32",
        #webgl_vendor="Intel Inc.",
        #renderer="Intel Iris OpenGL Engine",
        #fix_hairline=True,
        #)
    lst = []
    try:
        driver.get('https://' + url + phonenumber)
        WebDriverWait(driver, 30)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*/a[@class="field"][3]/div/div[@class="field__content"]')))
        #print(driver.page_source)
        tree = html.fromstring(driver.page_source)
        divs = tree.xpath('//*/a[@class="field"][3]/div/div[@class="field__content"]')#"//div[@data-v-702518d1 and contains(., 'simranmehta2014@gmail.com')]")#'//*[@id="__nuxt"]/div/main/div[2]/div/div[2]/div/div/div[2]')
        #soup = BeautifulSoup(page_source, 'lxml')
        #soup = BeautifulSoup(driver.page_source, 'lxml', from_encoding='utf-8')
        print(divs)
        for i in range(len(divs)):
            lst.append(divs[i].text)
        #for item in soup.find_all('a'):  # Example: extracting all paragraph tags
            #print(item.text)
        print(lst)
    except: #requests.exceptions.ConnectionError:
        print('simranmehta2014@gmail.com')
        # lst[0] = 'simranmehta2014@gmail.com'
        lst.append('simranmehta2014@gmail.com')
    finally:
        driver.quit()
        return lst[0]
    
# phonenumber="+916000982561"    
# T_url = "www.truecaller.com/search/in/"
# response = request_data(T_url, phonenumber)
# print(response)
#//*[@id="__nuxt"]/div/main/div[2]/div/div[2]/div/div/div[2]/div[2]/a[3]/div/div[2]
