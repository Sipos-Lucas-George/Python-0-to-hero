import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self, login_details, promised_speed, paid_speed):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.__login_details = login_details
        self.__promised_speed = promised_speed
        self.__paid_speed = paid_speed
        self.__actual_speed = (0, 0)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(0.7)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.XPATH, '//span[text()="Go"]').click()

        time.sleep(40)
        while True:
            try:
                self.driver.find_element(By.XPATH, '//a[text()="Back to test results"]').click()
                break
            except ElementNotInteractableException:
                continue

        download = float(self.driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/"
            "div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span"
        ).text)
        upload = float(self.driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/"
            "div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span"
        ).text)
        self.__actual_speed = (download, upload)

    def tweet_at_provider(self):
        if self.__promised_speed[0] >= self.__actual_speed[0] or self.__promised_speed[1] >= self.__actual_speed[1]:
            print(f"All good, you internet speed is {self.__actual_speed[0]} down and {self.__actual_speed[1]} up")
            return
        self.driver.get("https://twitter.com/login")
        time.sleep(0.7)

        email = self.driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/"
            "div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
        )
        email.send_keys(self.__login_details[0])
        email.send_keys(Keys.ENTER)
        time.sleep(0.5)
        try:
            if self.driver.find_element(By.XPATH,
                                        '//span[text()="Enter your phone number or username"]').is_displayed():
                username = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/"
                    "div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
                )
                username.send_keys(self.__login_details[2])
                username.send_keys(Keys.ENTER)
        except InvalidSelectorException:
            pass
        time.sleep(0.5)
        password = self.driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/"
            "div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
        )
        password.send_keys(self.__login_details[1])
        time.sleep(0.5)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        self.driver.find_element(By.XPATH, '//span[text()="Refuse non-essential cookies"]').click()

        complaint_text = (f"Hi Digi, why is my internet speed {self.__actual_speed[0]} down/{self.__actual_speed[1]} up"
                          f" when I pay for {self.__paid_speed[0]} down/{self.__paid_speed[1]} up?")
        time.sleep(1)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/"
            "div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]"
        ).click()
        time.sleep(0.5)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/"
            "div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/"
            "div/div/div/div/span"
        ).send_keys(complaint_text)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/"
            "div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/span/span"
        ).click()
        time.sleep(2)
        self.driver.quit()
