import test_cases.conftest as conf
from Page_object.web_objects.loginPage import LoginPage
from Page_object.web_objects.mainPage import MainPage
from Page_object.web_objects.left_menu_page import Left_Menu_Page
from Page_object.web_objects.server_admin_menu_page import Server_Admin_Menu_Page
from Page_object.web_objects.server_admin_new_user_page import Server_Admin_New_User_Page
from Page_object.web_objects.server_admin_page import Server_Admin_Page
from Page_object.web_objects.upper_menu_page import Upper_Menu_Page

#Web Objects
web_login = None
web_main = None
web_upper_menu = None
web_left_menu = None
web_server_admin_menu = None
web_server_admin = None
web_server_admin_new_user = None


class Manage_Pages:

    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['web_upper_menu'] = Upper_Menu_Page(conf.driver)
        globals()['web_left_menu'] = Left_Menu_Page(conf.driver)
        globals()['web_server_admin_menu'] = Server_Admin_Menu_Page(conf.driver)
        globals()['web_server_admin'] = Server_Admin_Page(conf.driver)
        globals()['web_server_admin_new_user'] = Server_Admin_New_User_Page(conf.driver)
