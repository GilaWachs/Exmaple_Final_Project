import selenium
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


main_title = (By.CLASS_NAME, "css-1aanzv4")
class MainPage:

    def __init__(self, n_driver):
        self.driver = n_driver

    def get_main_title(self):
        return self.driver.find_element(main_title[0],main_title[1])
