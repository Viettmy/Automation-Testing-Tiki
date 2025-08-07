from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, phone, password):
        self._close_popup_if_present()
        self._click_account_button()
        self._input_phone(phone)
        self._click_continue_button()

        if password:
            if self._is_password_input_present():
                self._input_password(password)
                self._click_login_button()

    # Đóng popup nếu có
    def _close_popup_if_present(self):
        try:
            close_popup = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//img[contains(@class,'sc-900210d0-0')]"))
            )
            close_popup.click()
        except:
            pass

    # Nhấn nút "Tài khoản"
    def _click_account_button(self):
        account_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Tài khoản']"))
        )
        account_btn.click()

    # Nhập số điện thoại
    def _input_phone(self, phone):
        phone_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "tel"))
        )
        phone_input.clear()
        phone_input.send_keys(phone)

    # Nhấn "Tiếp tục"
    def _click_continue_button(self):
        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Tiếp Tục')]"))
        )
        continue_btn.click()

    # Kiểm tra có hiện ô nhập mật khẩu không
    def _is_password_input_present(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
            )
            return True
        except TimeoutException:
            return False

    # Nhập mật khẩu
    def _input_password(self, password):
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.clear()
        password_input.send_keys(password)

    # Nhấn nút "Đăng nhập"
    def _click_login_button(self):
        login_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Đăng Nhập')]")
        login_btn.click()

    # Kiểm tra đã đăng nhập chưa
    def is_logged_in(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[contains(text(), 'Tài khoản')]").is_displayed()
        except:
            return False

    # Lấy thông báo lỗi
    def get_error_message(self):
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='error-mess']"))
            )
            return error_element.text.strip()
        except TimeoutException:
            return ""
