import os
from dotenv import load_dotenv
from utils.driver_setup import init_driver
from tests.test_login import test_login
from tests.test_search import test_search
from tests.test_cart import test_cart

if __name__ == "__main__":
    load_dotenv()
    driver = init_driver()
    driver.get("https://tiki.vn/")
    test_login(driver)
    test_search(driver)
    test_cart(driver)
    input("/n Press enter to finish...")
    driver.quit()