from selenium.webdriver.remote.webelement import WebElement

import test_cases.conftest as conf


class Ui_Actions:

    @staticmethod
    def click(elem: WebElement):
        elem.click()


    @staticmethod
    def update_text(elem: WebElement, value):
        elem.send_keys(value)


    @staticmethod
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem1).click().perform()

    @staticmethod
    def right_click(elem: WebElement):
        conf.action.context_click(elem).perform()

    @staticmethod
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        conf.action.drag_and_drop().perform()

    @staticmethod
    def clear(elem: WebElement):
        elem.clear()
