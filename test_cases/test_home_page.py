import pytest
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Home_page import Home_page
import time
from utilities.read_testdata import Read_testdata
from utilities.custom_logger import Log_Maker
from utilities.read_config import Configurations


class Test_Home_Page:
    Home_page_url = Configurations.get_url()
    logger = Log_Maker.log_gen()

    def test_scroll_down(self,setup):
        self.logger.info("*************************Test Case 1 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.hp.scroll_down_to_the_elements()
        self.driver.close()

    def test_click_on_who_we_are(self,setup):
        self.logger.info("*************************Test Case 2 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.hp.scroll_down_to_the_elements()
        self.hp.click_on_who_we_are()
        self.driver.close()

    def test_click_on_our_vision(self,setup):
        self.logger.info("*************************Test Case 3 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.hp.scroll_down_to_the_elements()
        self.hp.click_on_our_vision()
        self.driver.close()

    def test_click_on_our_values(self,setup):
        self.logger.info("*************************Test Case 4 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.hp.scroll_down_to_the_elements()
        self.hp.click_on_our_values()
        self.driver.save_screenshot("C:/PythonProject2/screenshots/screenshot2.png")
        self.driver.close()

    def test_click_on_about_us(self,setup):
        self.logger.info("*************************Test Case 5 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.hp.click_on_about_us()
        self.driver.close()

    def test_logo(self,setup):
        self.logger.info("*************************Test Case 6 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.hp.logo_verify()
        self.driver.close()

    @pytest.mark.parametrize(
        "name,emailid,contact_number,message",
        [
            (
                    Read_testdata.get_value("my_name"),
                    Read_testdata.get_value("my_email"),
                    Read_testdata.get_value("my_number"),
                    Read_testdata.get_value("message"),
            ),
            (
                    Read_testdata.get_value("invalid_name"),
                    Read_testdata.get_value("invalid_email"),
                    Read_testdata.get_value("invalid_number"),
                    Read_testdata.get_value("message"),
            ),
        ],
    )
    def test_first(self, setup, name, emailid, contact_number, message):
        self.logger.info("********** Test Case Execution **********")
        self.driver = setup
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.driver.get(self.Home_page_url)
        self.hp.scroll_down_to_contact_number()
        self.hp.entering_first_name(name)
        self.hp.entering_email(emailid)
        self.hp.entering_contact_number(contact_number)
        self.hp.entering_message(message)
        self.driver.save_screenshot("C:/PythonProject2/screenshots/screenshot3.png")
        self.driver.close()
        



















