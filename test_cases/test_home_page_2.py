import pytest
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_Objects.Home_page import Home_page
import time
from utilities.read_config import Configurations
from utilities.custom_logger import Log_Maker
from utilities.excel_utils_2 import ExcelUtils

testdata2 = ExcelUtils.load_excel_data("C:/Users/chinmaya kumar nayak/Documents/testdata2.xlsx","Sheet1")

class Test_home_page_2:

    Home_url = Configurations.get_url()
    logger = Log_Maker.log_gen()

    @pytest.mark.parametrize("name, emailid, contact_number, message", testdata2)
    def test_data_driven(self, setup, name, emailid, contact_number, message):
        self.logger.info("************************* data driven testing ****************************")
        self.driver = setup
        self.driver.get(self.Home_url)
        # creating the object of home page class
        self.hp = Home_page(self.driver)
        self.hp.scroll_down_to_contact_number()
        self.hp.entering_first_name(name)
        self.hp.entering_email(emailid)
        self.hp.entering_contact_number(contact_number)
        self.hp.entering_message(message)
        self.driver.close()
        




