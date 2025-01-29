import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Declaring the constructor
    def __init__(self,driver):
        self.driver = driver

    #  Declaring a method for sending values to field
    def element_sendkeys(self,text,locator):
        element = self.get_element(locator)
        element.send_keys(text)

    #  Declaring a method for clicking on a web element
    def element_click(self,locator):
        element = self.get_element(locator)
        element.click()

    #  Declaring a method for checking the visibility of an element
    def visibility_of_element(self,locator):
        element = self.get_element(locator)
        return element.is_displayed()

    #  Declaring a method for getting the text of an web element
    def retrieve_text_of_element(self,locator):
        element = self.get_element(locator)
        return element.text

    #  Declaring a method for locating a web element
    def get_element(self,locator):
        element = None
        if locator.__contains__("_id"):
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,locator)))
        elif locator.__contains__("//"):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,locator)))
        return element



