from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

#import wget
os.environ['PATH'] += r"C:/geckodriver-v0.32.0-win32"

options = webdriver.FirefoxOptions()
options.add_argument("-profile")
options.add_argument("C:\\Users\\user\\AppData\\Local\\\Mozilla\\Firefox\Profiles\\j9qm8nmx.default-release")
driver = webdriver.Firefox(options=options)
driver.set_window_size(1024, 600)
driver.maximize_window()


#open the webpage
driver.get("https://www.twitch.tv/brawlhalla")

#target username
login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div.Layout-sc-nxg1ff-0.bSuLAT > nav > div > div.Layout-sc-nxg1ff-0.hWJFll > div.Layout-sc-nxg1ff-0.jwASrz > div > div.Layout-sc-nxg1ff-0.iLhppl.anon-user > div:nth-child(1) > button > div > div"))).click()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-username")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password-input")))

#enter username and password
username.clear()
username.send_keys("3ddi6")
password.clear()
password.send_keys("vC%=xA!i&Z7bgUT")

#target the login button and click it
button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-nxg1ff-0.gmqBFP > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(3) > button > div > div"))).click()

