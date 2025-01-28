from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.About_Us_Page import About_Us_Page

class Home_page:

    # locators of this page
    who_we_are_xpath = "//button[normalize-space()='Who we are?']"
    our_vision_mission_xpath = "//button[normalize-space()='Our Vision & Mission']"
    our_values_xpath = "//button[normalize-space()='Our Values']"
    about_us_xpath = "//a[contains(@class,'drop-down')][normalize-space()='About Us']"
    company_logo_xpath = "//img[@alt='Company Logo']"
    your_full_name_xpath = "//input[@placeholder='Your Full Name']"
    your_email_xpath = "//input[@placeholder='Your Email']"
    your_contact_number_xpath = "//input[@placeholder='Your Contact Number']"
    write_your_meassage_xpath = "//textarea[@id='msg-text']"

# declaring the constructor
    def __init__(self,driver):
        self.driver = driver

# all the actions those will have to be performed
    def scroll_down_to_the_elements(self):
        vision_mission = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.our_vision_mission_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",vision_mission)

    def click_on_who_we_are(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.who_we_are_xpath))).click()

    def click_on_our_vision(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.our_vision_mission_xpath))).click()

    def click_on_our_values(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.our_values_xpath))).click()

    def click_on_about_us(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.about_us_xpath))).click()


    def logo_verify(self):
        logo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.company_logo_xpath)))
        assert logo.is_displayed(), "Logo is not visible"  # Message when the logo is not visible
        print("Logo is visible")  # Message when the logo is visible

    def scroll_down_to_contact_number(self):
        number = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.your_contact_number_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",number)

    def entering_first_name(self,my_name):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.your_full_name_xpath))).send_keys(my_name)

    def entering_email(self,my_email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.your_email_xpath))).send_keys(my_email)

    def entering_contact_number(self,my_number):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.your_contact_number_xpath))).send_keys(my_number)

    def entering_message(self,my_message):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.write_your_meassage_xpath))).send_keys(my_message)


    def navigate_to_about_us_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.about_us_xpath))).click()
        return About_Us_Page(self.driver)







































