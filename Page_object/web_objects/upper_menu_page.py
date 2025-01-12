from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

general = (By.LINK_TEXT, "General")
home = (By.LINK_TEXT, "Home")
add_panel = (By.CSS_SELECTOR, "button[aria-label='Add panel']")
save_dashboard = (By.CSS_SELECTOR, "button[aria-label='Save dashboard']")
dashboard_settings = (By.CSS_SELECTOR, "button[aria-label='Dashboard settings']")
cycle_view_mode = (By.CSS_SELECTOR, "button[aria-label='Cycle view mode']")




class Upper_Menu_Page:

    def __init__(self, driver: WebElement):
        self.driver = driver

    def get_general(self):
        return self.driver.find_element(general[0],general[1])

    def get_home(self):
        return self.driver.find_element(home[0],home[1])

    def get_add_panel(self):
        return self.driver.find_element(add_panel[0],add_panel[1])

    def get_save_dashboard(self):
        return self.driver.find_element(save_dashboard[0],save_dashboard[1])

    def get_dashboard_settings(self):
        return self.driver.find_element(dashboard_settings[0],dashboard_settings[1])

    def get_cycle_view_mode(self):
        return self.driver.find_element(cycle_view_mode[0],cycle_view_mode[1])