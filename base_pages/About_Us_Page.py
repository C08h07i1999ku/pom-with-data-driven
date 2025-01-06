import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class About_Us_Page:

    # locators of this page
    read_more_xpath = "//span[@class='readmoreBtn']"

    # declaring the constructor
    def __init__(self,driver):
        self.driver = driver

     # all the actions those will have to be performed
    def scroll_into_read_more_button(self):
        read_more = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.read_more_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",read_more)

    def click_on_read_more_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.read_more_xpath))).click()


