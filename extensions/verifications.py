from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:


    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, \
            'Verify equal failed, actual:' + str(actual) + 'is not equals to: ' + str(expected)

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'Verify is display failed' + elem.text + ' is not displayed'


    #verify menu button flow using my implementation
    @staticmethod
    def soft_displayed(elements):
        failed_elems = []
        for i in range(len(elements)):
            if not elements[i].is_displayed():
                failed_elems.insert(len(elements), elements[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print("\nSoft display failed for " + str(failed_elem))
            raise AssertionError
    #verify menu button flow using smart assertion
    @staticmethod
    def soft_assert(elems):
        for i in range(len(elems)) :
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, ('number of elemntst in list: '
                                    + str(len(elems)) + 'does not match expected: ' + str(size))


