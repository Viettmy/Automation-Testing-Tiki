import os
import pytest
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@allure.feature("Login Functionality")
@allure.story("Test login with valid and invalid credentials")
@pytest.mark.parametrize("phone, password, expected_result", [
    (os.getenv("PHONE"), os.getenv("PASSWORD"), "success"),           # Đúng
    (os.getenv("PHONE"), "sai_mat_khau", "wrong_password"),           # Sai mật khẩu
    ("0123456789", os.getenv("PASSWORD"), "wrong_phone"),             # Sai số điện thoại
    ("", "", "empty"),                                                # Trống
])
def test_login(driver, phone, password, expected_result):
    login_page = LoginPage(driver)
    
    with allure.step(f"Attempting login with phone: {phone}, password: {password}"):
        login_page.login(phone, password)

    if expected_result == "success":
        with allure.step("Verify successful login"):
            assert login_page.is_logged_in(), "❌ Không đăng nhập được với tài khoản đúng"
            allure.attach("Login successful", name="Login Result", attachment_type=allure.attachment_type.TEXT)

    elif expected_result == "wrong_password":
        with allure.step("Verify error message for wrong password"):
            error = login_page.get_error_message()
            assert "Thông tin đăng nhập không đúng" in error, f"❌ Không bắt đúng lỗi mật khẩu: {error}"
            allure.attach(error, name="Error Message", attachment_type=allure.attachment_type.TEXT)

    elif expected_result == "wrong_phone":
        with allure.step("Verify error message for wrong phone number"):
            error = login_page.get_error_message()
            assert "Số điện thoại không đúng định dạng" in error or "không tồn tại" in error, f"❌ Không bắt được lỗi sai số điện thoại: {error}"
            allure.attach(error, name="Error Message", attachment_type=allure.attachment_type.TEXT)

    elif expected_result == "empty":
        with allure.step("Verify error message for empty input"):
            error = login_page.get_error_message()
            assert "Số điện thoại không được để trống" in error, f"❌ Không bắt được lỗi bỏ trống: {error}"
            allure.attach(error, name="Error Message", attachment_type=allure.attachment_type.TEXT)