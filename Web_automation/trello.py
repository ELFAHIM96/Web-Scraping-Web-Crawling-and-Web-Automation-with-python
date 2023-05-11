from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
import json
from datetime import date

import os

CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver')
OP = webdriver.ChromeOptions()
OP.add_argument('--headless')
DRIVER = webdriver.Chrome(CHROME_DRIVER_PATH)



def login():
    with open("config.json") as configFile:
        credentials = json.load(configFile)
        time.sleep(2)
        DRIVER.find_element(By.XPATH,value ="//a[@href='/login']").click()
        time.sleep(2)
        username = DRIVER.find_element(
            By.CSS_SELECTOR, value = "input[name = 'user']")
        password = DRIVER.find_element(
            By.CSS_SELECTOR, value = "input[name = 'password']")
        username.clear()
        password.clear()

        username.send_keys(credentials["USERNAME"])
        password.Send_keys(credentials["PASSWORD"])

   
def main():
    try: 
        DRIVER.get("https://trello.com")
        login
        input('Bot Operation Completed. press any key..')
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()

if __name__ == "__main__":

    main()
    print("hi")