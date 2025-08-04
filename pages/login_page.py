from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
class LoginPage:
    def __init_(self, driver: WebDriver):
        self.driver = driver
        def login(self, phone, password):
            time.sleep(5)
            close_popup = self.driver.find_element(By.XPATH, "//img[contains (@class, 'sc-900210d0-0')]").click()
            time.sleep(1)
            account_button = self.driver.find_element(By.XPATH, "//span[text()='Tài khoản']").click()
            time.sleep(1)
            phone_input = self.driver.find_element(By.NAME, "tel").send_keys(phone)
            time.sleep(1)
            continue_button = self.driver.find_element(By.XPATH, "//button [contains (text(), 'Tiếp Tục')]").click()
            time.sleep(1)
            pass_input = self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
            time.sleep(1)
            login_button = self.driver.find_element(By.XPATH, "//button [contains (text(), 'Đăng Nhập')]").click()