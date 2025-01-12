from selenium.webdriver.common.by import By

from utilities.common_ops import wait, For

search = (By.CSS_SELECTOR, ".css-fcoerl-input-input")
new_user = (By.CSS_SELECTOR, ".css-sqvqs4-button")
users_list = (By.XPATH, "//table[@class='filter-table form-inline filter-table--hover']/tbody/tr")
user_by_user_name = (By.CSS_SELECTOR, "a[title='kuku']")
delete = (By.XPATH,"//div/button[@class='css-19vct9a-button']")
confirm_delete = (By.XPATH,"//button[@aria-label='Confirm Modal Danger Button']")


class Server_Admin_Page:

    def __init__(self, driver):
        self.driver = driver


    def get_search(self):
        return self.driver.find_element(search[0],search[1])

    def get_new_user(self):
        wait(For.ELEMENT_EXISTS,new_user)
        return self.driver.find_element(new_user[0], new_user[1])

    def get_users_list(self):
        return self.driver.find_elements(users_list[0],users_list[1])

    def get_users_delete(self):
        return self.driver.find_element(delete[0],delete[1])


    def get_users_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0],confirm_delete[1])

    def get_user_by_user_name(self,user):
        return self.driver.find_element(user_by_user_name[0], user_by_user_name[1].replace("kuku", str(user)))

    def get_users_by_index(self, index):
        return self.get_users_list()[index]
