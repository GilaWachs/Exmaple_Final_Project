import time

import pytest
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data
from utilities.event_listener import EventListener
from utilities.manage_pages import Manage_Pages

driver = None
action = None

@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('URL'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    Manage_Pages.init_web_pages()
    time.sleep(2)
    yield
    driver.quit()


def get_web_driver():
    webdriver_type = get_data('Browser')
    if webdriver_type.lower() == 'chrome':
        driver = get_chrome()
    elif webdriver_type.lower() == 'firefox':
        driver = get_firefox()
    elif webdriver_type.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception('Wrong input, Unrecognized browser')
    return driver

def get_chrome():
    service = Service(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(service=service)#selenium 4.x
    return chrome_driver
#Edge browser
def get_edge():
    service = Service(EdgeChromiumDriverManager().install())
    edge_driver = selenium.webdriver.Edge(service=service)#selenium 4.x
    return edge_driver

def get_firefox():
    service = Service(executable_path=GeckoDriverManager().install())
    ff_driver = selenium.webdriver.Firefox(service=service)  # selenium 4.x
    return ff_driver

