import time

from selenium import webdriver
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
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        while True:
            try:
                self.driver.find_element(By.XPATH, '//button[text()="Decline optional cookies"]').click()
                break
            except Exception:
                pass

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

    def find_following(self):
        self.driver.get(f"https://www.instagram.com/{self.__instagram_account}/")
        while True:
            try:
                number_of_followers = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/"
                    "section/ul/li[3]/a/span/span"
                ).text
                break
            except Exception:
                pass

        self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/"
            "section/ul/li[3]/a"
        ).click()

        while True:
            try:
                list_of_following = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]"
                )
                time.sleep(1)
                break
            except Exception:
                pass

        # for i in range(number_of_followers // 7):
        loading = 0
        length = len(self.driver.find_elements(
            By.XPATH,
            '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div'
        ))
        while loading < 3:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", list_of_following)
            new_length = len(self.driver.find_elements(
                By.XPATH,
                '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div'
            ))
            if length == new_length:
                loading += 1
            else:
                length = new_length
                loading = 0
            time.sleep(1.5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.__instagram_account}/")

        while True:
            try:
                number_of_followers = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/"
                    "section/ul/li[2]/a/span/span"
                ).text
                break
            except Exception:
                pass

        self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/"
            "section/ul/li[2]/a"
        ).click()

        while True:
            try:
                list_of_followers = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
                )
                time.sleep(1)
                break
            except Exception:
                pass

        # for i in range(number_of_followers // 7):
        loading = 0
        length = len(self.driver.find_elements(
            By.XPATH,
            '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div'
        ))
        while loading < 3:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", list_of_followers)
            new_length = len(self.driver.find_elements(
                By.XPATH,
                '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div'
            ))
            if length == new_length:
                loading += 1
            else:
                length = new_length
                loading = 0
            time.sleep(1.5)

    def save_following(self):
        list_of_following = self.driver.find_elements(
            By.XPATH,
            '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div/div/div/div/div/'
            'div/div[2]/div/div/div/span/div/a/div/div/span'
        )
        # print(len(list_of_following))

        with open("following.txt", "w") as file:
            for following in list_of_following:
                file.write(following.text + "\n")

        self.driver.quit()

    def save_followers(self):
        list_of_followers = self.driver.find_elements(
            By.XPATH,
            '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/'
            'div/div[2]/div/div/div/span/div/a/div/div/span'
        )
        # print(len(list_of_followers))

        with open("followers.txt", "w") as file:
            for followers in list_of_followers:
                file.write(followers.text + "\n")

        self.driver.quit()
