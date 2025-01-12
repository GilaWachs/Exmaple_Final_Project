import csv

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import test_cases.conftest as conf
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse('C:/Automation/FinalProject/Configuration/data.xml').getroot()
    return root.find('.//' + node_name).text

def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data),row)
        return data

def wait(for_elem, elem):
    if for_elem == For.ELEMENT_EXISTS:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0],elem[1])))
    elif for_elem == For.ELEMENT_DISPLAYED:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))

        #Enum for selecting display element or exist element, my wait method uses this enum

class For:
    ELEMENT_EXISTS = 'element exists'
    ELEMENT_DISPLAYED = 'element displayed'

class By:
    USER = 'user'
    INDEX = 'index'