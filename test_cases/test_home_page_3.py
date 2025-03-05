import pytest
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_Objects.Home_page import Home_page
import time
from utilities.read_config import Configurations
from utilities.custom_logger import Log_Maker
from utilities.excel_utils_2 import ExcelUtils

@pytest.mark.usefixtures("setup")
class Test_home_page_3:
    logger = Log_Maker.log_gen()
    name = "Chinmaya"
    emailid="xyz@gmail.com"
    contact_number = 8249117340
    message = "hii"

    def test_data_driven_demo(self):
        self.hp = Home_page(self.driver)
        self.hp.scroll_down_to_contact_number()
        self.hp.entering_first_name(self.name)
        self.hp.entering_email(self.emailid)
        self.hp.entering_contact_number(self.contact_number)
        self.hp.entering_message(self.message)
        time.sleep(5)
        self.driver.close()


    def test_data_driven_demo_2(self):
        self.hp = Home_page(self.driver)
        self.hp.scroll_down_to_contact_number()
        self.hp.entering_first_name(self.name)
        self.hp.entering_email(self.emailid)
        self.hp.entering_contact_number(self.contact_number)
        self.hp.entering_message(self.message)
        time.sleep(5)
        self.driver.close()

