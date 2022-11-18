from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random 
from twitch import driver

def account():
    page = driver.get("https://www.twitch.tv/brawlhalla")
    signup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".dDxrgX"))).click()
    use_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.dWdTjI:nth-child(2)"))).click()
    enter_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#email-input")))
    enter_email.clear()
    enter_email.send_keys()
    next_step = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ScCoreButtonPrimary-sc-1qn4ixc-1:nth-child(2) > div:nth-child(1) > div:nth-child(1)"))).click()
    user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#signup-username")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password-input")))

    user_name.clear()
    user_name.sendkeys()
    password.clear()
    password.sendkeys()

    next_step1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ScCoreButtonPrimary-sc-1qn4ixc-1:nth-child(2) > div:nth-child(1) > div:nth-child(1)"))).click()
    month = Select(driver.find_element_by_css_selector("select.ScInputBase-sc-1wz0osy-0"))
    month.select_by_visible_text(random.choice(month))
    day = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.birthday-picker__input:nth-child(2) > div:nth-child(1) > input:nth-child(1)")))
    year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.birthday-picker__input:nth-child(3) > div:nth-child(1) > input:nth-child(1)")))

    day.clear()
    day.sendkeys()
    year.clear()
    year.sendkeys()

    signup_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ScCoreButtonPrimary-sc-1qn4ixc-1:nth-child(2)"))).click()
    
