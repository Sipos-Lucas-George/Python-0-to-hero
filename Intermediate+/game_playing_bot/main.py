"""
    Game Playing Bot Using Selenium Webdriver Browser
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

OFFSET = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
buy_panel = driver.find_elements(By.CSS_SELECTOR, "#store div b")[::-1]
timeout = time.time() + OFFSET
last_time = 0
while True:
    cookie.click()
    if time.time() > timeout:
        if OFFSET == 30:
            OFFSET = 10
        if buy_panel[0].is_displayed():
            for i in range(9):
                if int(buy_panel[i].text.split(" - ")[1].replace(",", "")) < int(
                        driver.find_element(By.ID, "money").text.replace(",", "")):
                    buy_panel[i].click()
                    time.sleep(0.1)
                    buy_panel = driver.find_elements(By.CSS_SELECTOR, "#store div b")[::-1]
        else:
            buy_items = 0
            for i in range(8):
                if int(buy_panel[i + 1].text.split(" - ")[1].replace(",", "")) < int(
                        driver.find_element(By.ID, "money").text.replace(",", "")):
                    buy_items += 1
                    buy_panel[i + 1].click()
                    time.sleep(0.1)
                    buy_panel = driver.find_elements(By.CSS_SELECTOR, "#store div b")[::-1]
            if last_time == buy_items:
                OFFSET += 1
            last_time = buy_items
        timeout = time.time() + OFFSET
