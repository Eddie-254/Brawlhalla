import undetected_chromedriver as uc

driver = uc.Chrome(use_subprocess=True)
#open the webpage
driver.get("https://www.twitch.tv/brawlhalla")

