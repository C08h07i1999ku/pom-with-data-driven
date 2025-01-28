from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_Objects.Home_page import Home_page
from Page_Objects.About_Us_Page import About_Us_Page
import time
from utilities.read_testdata import Read_testdata
from utilities.custom_logger import Log_Maker
from utilities.read_config import Configurations
from selenium.webdriver.support.ui import WebDriverWait

class Test_About_us_page:
    Home_page_url = Configurations.get_url()
    logger = Log_Maker.log_gen()

    def test_click_on_read_more(self,setup):
        self.logger.info("*************************Test Case 8 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of the Home page class
        self.hp = Home_page(self.driver)
        # creating the object of the About us page class
        self.aup = About_Us_Page(self.driver)
        self.hp.click_on_about_us()
        self.aup.scroll_into_read_more_button()
        self.aup.click_on_read_more_button()
        self.driver.close()


    def test2_click_on_read_more(self,setup):
        self.logger.info("*************************Test Case 8 passed*************************")
        self.driver = setup
        self.driver.get(self.Home_page_url)
        # creating the object of the Home page class
        self.hp = Home_page(self.driver)
        # creating the object of the About us page class
        self.aup=self.hp.navigate_to_about_us_page()
        self.aup.scroll_into_read_more_button()
        self.aup.click_on_read_more_button2()
        self.driver.close()
