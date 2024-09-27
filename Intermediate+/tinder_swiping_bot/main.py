"""
    Auto Tinder Swiping Bot Using Selenium Webdriver Browser
"""
import os
import time
import dotenv

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By

dotenv.load_dotenv()

PHONE = os.getenv("PHONE")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

driver.find_element(By.XPATH, '//div[text()="I accept"]').click()
driver.find_element(
    By.XPATH,
    '//div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]'
).click()
time.sleep(0.7)
driver.find_element(
    By.XPATH,
    '//main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'
).click()
time.sleep(3)
base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

driver.find_element(By.XPATH, '//button[@title="Decline optional cookies"]').click()

username = driver.find_element(By.ID, "email")
username.send_keys(PHONE)
password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)
driver.find_element(By.ID, "loginbutton").click()
time.sleep(6)

driver.switch_to.window(base_window)
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]").click()
time.sleep(8)

for _ in range(100):
    time.sleep(1)

    try:
        driver.find_element(
            By.XPATH,
            '//span[normalize-space()="Like"]'
        ).click()

    except ElementClickInterceptedException:
        try:
            time.sleep(1)
            driver.find_element(
                By.XPATH,
                '//button[contains(@title, "Back to Tinder")]'
            ).click()
        except NoSuchElementException:
            try:
                driver.find_element(
                    By.XPATH,
                    '//div[text()="Not interested"]'
                ).click()
            except NoSuchElementException:
                try:
                    driver.find_element(
                        By.XPATH,
                        '//div[text()="Maybe Later"]'
                    ).click()
                except NoSuchElementException:
                    try:
                        if driver.find_element(By.XPATH, '//h3[text()="Select a plan"]').is_displayed():
                            driver.quit()
                            exit(0)
                    except NoSuchElementException:
                        time.sleep(0.5)
    except NoSuchElementException:
        time.sleep(1)

driver.quit()
