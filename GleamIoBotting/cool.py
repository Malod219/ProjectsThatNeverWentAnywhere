from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import random
name="yourname"
usr="yourname@gmail.com"
driver=webdriver.Firefox()
driver.get("https://gleam.io/TKwm3/ironside-imp-ultra")
for i in range(0,10):
    try:
        usr="perf3ctodst+"+str(i)+"@gmail.com"
        time.sleep(3)
        names = driver.find_elements_by_name("name")
        namebox = names[1]
        namebox.click()
        namebox.send_keys(name)
        emails = driver.find_elements_by_name("email")
        emailbox = emails[1]
        emailbox.click()
        emailbox.send_keys(usr)
        terms = driver.find_elements_by_name("i_have_read_and_agree_to_the_terms_and_conditions")
        termsbox=terms[0]
        termsbox.send_keys(Keys.SPACE)
        buttons = driver.find_elements_by_class_name("btn-primary")
        button=buttons[1]
        button.click()
        time.sleep(1)
        buttons2 = driver.find_elements_by_xpath("//*[contains(text(), 'Logout')]")
        for i in buttons2:
            print(i)
            try:
                i.click()
                print("success")
            except:
                print("fail")
        time.sleep(random.randint(10,30))
    except:
        driver.quit()
        driver=webdriver.Firefox()
        driver.get("https://gleam.io/TKwm3/ironside-imp-ultra")
