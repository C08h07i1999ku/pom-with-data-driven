import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Base_Page import BasePage

class About_Us_Page(BasePage):

    # locators of this page
    read_more_xpath = "//span[@class='readmoreBtn']"

    # declaring the constructor
    def __init__(self,driver):
        super().__init__(driver)

     # all the actions those will have to be performed
    def scroll_into_read_more_button(self):
        read_more = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.read_more_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",read_more)

    def click_on_read_more_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.read_more_xpath))).click()


    # def scroll_into_read_more_button2(self):
    #     self.scroll_into_view(self.read_more_class)

    def click_on_read_more_button2(self):
        self.element_click(self.read_more_xpath)
