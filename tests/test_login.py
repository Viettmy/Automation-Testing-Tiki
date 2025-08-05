import os
from pages.login_page import LoginPage

def test_login(driver):
    phone=os.getenv("PHONE")
    password = os.getenv("PASSWORD")
    
    login_page = LoginPage(driver)
    login_page.login(phone, password)