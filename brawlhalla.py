from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from twitch import driver


def brawlhalla():
    tab = driver.switch_to.new_window('tab')
    page = driver.get('https://www.brawlhalla.com/')
    accept_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#wt-cli-accept-btn'))).click()
    
    while(True):
        pass
brawlhalla()

    