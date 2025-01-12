from selenium.webdriver.support.events import AbstractEventListener


class EventListener(AbstractEventListener):

    class EventListener:

        def __init__(self):
            self.button_text = None
            print("EventListener initialized.")

        def before_navigate_to(self, url, driver):
            print(f"Before navigating to: {url}")

        def after_navigate_to(self, url, driver):
            print(f"After navigating to: {url}")

        def before_navigate_back(self, driver):
            print("Before navigating back", driver.current_url)

        def after_navigate_back(self, driver):
            print("After navigating back", driver.current_url)

        def before_navigate_forward(self, driver):
            print("Before navigating forward", driver.current_url)

        def after_navigate_forward(self, driver):
            print("After navigating forward", driver.current_url)

        def before_find(self, by, value, driver):
            print(f"Before finding element by: {by} with value: {value}")

        def after_find(self, by, value, driver):
            print(f"After finding element by: {by} with value: {value}")

        def before_click(self, element, driver):
            EventListener.button_text = element.get_attribute("value")
            print(f"Before clicking on element: {EventListener.button_text}")


        def after_click(self, element, driver):
            print(f"After clicking on element: {EventListener.button_text}")

        def before_change_value_of(self, element, driver):
            if element.tag_name == 'input':
                print(f"Before changing value of element: {element.get_attribute('value')}")
            else:
                print(f"Before changing value of element: {element.text}")

        def after_change_value_of(self, element, driver):
            if element.tag_name == 'input':
                print(f"After changing value of element: {element.get_attribute('value')}")
            else:
                print(f"After changing value of element: {element.text}")


        def before_execute_script(self, script, driver):
            print(f"Before executing script: {script}")

        def after_execute_script(self, script, driver):
            print(f"After executing script: {script}")

        def before_close(self, driver):
            print("Before closing the browser")

        def after_close(self, driver):
            print("After closing the browser")

        def before_quit(self, driver):
            print("Before quitting the browser")

        def after_quit(self, driver):
            print("After quitting the browser")

        def on_exception(self, exception, driver):
            print(f"Exception occurred: {str(exception)}")
