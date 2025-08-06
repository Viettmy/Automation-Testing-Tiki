from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10) #chờ 10s
    def search(self, keyword):
        self._close_popup_if_present()
        self._input_search_keyword(keyword)
        self._click_search_button()
        self._wait_for_search_results_to_load()
        self._select_product()
    # đóng popup nếu có
    def _close_popup_if_present(self):
        try:
            close_popup = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, "//img[contains(@class,'sc-900210d0-0') and @alt='close-icon']"
                ))
            )
            close_popup.click()
        except:
            pass
    # Thêm phương thức này vào class SearchPage
    def _wait_for_search_results_to_load(self):
        """
        Chờ cho đến khi container chứa danh sách sản phẩm tìm kiếm được hiển thị.
        Đây là dấu hiệu cho thấy trang kết quả đã tải xong.
        """
        self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                "[data-view-id='product_list_top_categories_container']" # Đây là container chứa các sản phẩm
            ))
        )
    # Nhập từ khóa
    def _input_search_keyword(self, keyword):
        search_input = self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "[data-view-id='main_search_form_input']"
            ))
        )  
        search_input.click()
        search_input.clear()
        search_input.send_keys(keyword)
    # Nhấn nút TÌM KIẾM
    def _click_search_button(self):
        search_button = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,"[data-view-id='main_search_form_button']"
            ))
        )
        search_button.click()
    # chọn sản phảm
    def _select_product(self):
        select_product = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "(//a[contains(@class,'product-item') and @data-view-id='product_list_item'])[1]"
            ))
        )
        select_product.click()