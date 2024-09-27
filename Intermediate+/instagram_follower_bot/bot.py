import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstagramFollowerBot:
    def __init__(self, login_details, instagram_account):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.__login_details = login_details
        self.__instagram_account = instagram_account

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[text()="Decline optional cookies"]').click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/"
            "form/div/div[1]/div/label/input"
        ).send_keys(self.__login_details[0])
        password = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/"
            "form/div/div[2]/div/label/input"
        )
        password.send_keys(self.__login_details[1])
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.__instagram_account}/")
        time.sleep(2)

        number_of_followers = int(self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/"
            "section/ul/li[2]/a/span/span"
        ).text)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/"
            "section/ul/li[2]/a"
        ).click()
        time.sleep(0.5)
        list_of_followers = self.driver.find_element(
            By.XPATH,
            "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        )
        for i in range(number_of_followers // 7):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", list_of_followers)
            time.sleep(2)
        time.sleep(1)

    def follow(self):
        list_to_follow = self.driver.find_elements(By.XPATH, '//div[text()="Follow"]')
        print(len(list_to_follow))
        # for follow in list_to_follow:
        #     follow.click()
        self.driver.quit()
