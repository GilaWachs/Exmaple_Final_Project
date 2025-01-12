import time

from selenium.webdriver.common.by import By
from utilities.common_ops import (get_data, wait, By)
from utilities.common_ops import read_csv

import Page_object.web_objects.server_admin_page as ser
import Page_object.web_objects.mainPage as main
from extensions.ui_actions import Ui_Actions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For


class Web_Flows:

    @staticmethod
    def login_flow(user_name, password):
        Ui_Actions.update_text(page.web_login.get_user_name(),"admin")
        Ui_Actions.update_text(page.web_login.get_password(),"admin")
        Ui_Actions.click(page.web_login.get_submit())
        Ui_Actions.click(page.web_login.get_skip())


    @staticmethod
    def verify_grafana_title(expected):
        wait(For.ELEMENT_EXISTS, main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    def verify_menu_buttons():
        elems = [page.web_upper_menu.get_add_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view_mode()
                 ]
        Verifications.soft_displayed(elems)
        #smart assertions function
        #Verifications.soft_assert(elems)
    @staticmethod
    def verify_menu_buttons_smart_assertions():
        elems = [page.web_upper_menu.get_add_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view_mode()
                 ]
        Verifications.soft_assert(elems)

    @staticmethod
    def open_users():
        elem1 = page.web_left_menu.get_server_admin()
        elem2 = page.web_server_admin_menu.get_users()
        Ui_Actions.mouse_hover(elem1, elem2)
    @staticmethod
    def create_user(name, email, user, password):
        Ui_Actions.click(page.web_server_admin.get_new_user())
        Ui_Actions.update_text(page.web_server_admin_new_user.get_name(), name)
        Ui_Actions.update_text(page.web_server_admin_new_user.get_email(), email)
        Ui_Actions.update_text(page.web_server_admin_new_user.get_user_name(), user)
        Ui_Actions.update_text(page.web_server_admin_new_user.get_password(), password)
        Ui_Actions.click(page.web_server_admin_new_user.get_create_user())


    @staticmethod
    def verify_number_of_users(number):
        if number > 0:
            wait(For.ELEMENT_DISPLAYED, ser.users_list)
            Verifications.verify_number_of_elements(page.web_server_admin.get_users_list(),number)

    @staticmethod
    def delete_user_index(index):
        Ui_Actions.click(page.web_server_admin.get_users_by_index(index))
        Ui_Actions.click(page.web_server_admin.get_users_delete())
        Ui_Actions.click(page.web_server_admin.get_users_confirm_delete())


    @staticmethod
    def delete_user(by, value):
        if by == By.INDEX:
            Ui_Actions.click(page.web_server_admin.get_users_by_index(value))
        elif by == By.USER:
            Ui_Actions.click(page.web_server_admin.get_user_by_user_name(value))
        Ui_Actions.click(page.web_server_admin.get_users_delete())
        #page.web_server_admin.driver.execute_script("arguments[0].style.display = 'none';", page.web_server_admin.driver.find_element(By.CLASS_NAME, "css-fxllif"))
        Ui_Actions.click(page.web_server_admin.get_users_confirm_delete())

    @staticmethod
    def grafana_home(self):
        self.driver.get(get_data('URL'))


    @staticmethod
    def search_user(search_value):
        Ui_Actions.clear(page.web_server_admin.get_search())
        Ui_Actions.update_text(page.web_server_admin.get_search(), search_value)
data = read_csv(get_data('CSV_Location'))
test_data= [
     (data[0][0],data[0][1]),
     (data[1][0],data[1][1]),
     (data[2][0],data[2][1]),
 ]


