import time

import pytest

from utilities.common_ops import get_data, wait, By
from workflows import web_flows
from workflows.web_flows import Web_Flows


@pytest.mark.usefixtures("init_web_driver")
class Test_Web:

    def test_verify_login(self):
        Web_Flows.login_flow(get_data('UserName'),get_data('Password'))
        Web_Flows.verify_grafana_title("Welcome to Grafana")

    def test_verify_upper_menu(self):
        #Web_Flows.verify_menu_buttons()
        Web_Flows.verify_menu_buttons_smart_assertions()

    def test_verify_new_user(self):
        Web_Flows.open_users()
        Web_Flows.create_user("Gila", "gilaw@gmail.com", "gilaw", "1234")
        time.sleep(1)
        Web_Flows.create_user("David", "Davvidd@gmail.com", "Davidd", "6423")
        Web_Flows.verify_number_of_users(3)
        time.sleep(1)

    @pytest.mark.parametrize('search_value, expected_users',web_flows.test_data)
    def test_csv(self, search_value , expected_users):
        Web_Flows.open_users()
        Web_Flows.search_user(search_value)
        time.sleep(2)
        Web_Flows.verify_number_of_users(int(expected_users))


    def test_verify_deleted_user(self):
        Web_Flows.open_users()
        Web_Flows.delete_user(By.USER,'gilaw')
        Web_Flows.delete_user(By.USER,'Davidd')
        time.sleep(3)
        Web_Flows.verify_number_of_users(1)
        time.sleep(2)


    def teardown_method(self):
        Web_Flows.grafana_home(self)
