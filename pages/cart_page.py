from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver : WebDriver):
        self.driver =driver
        self.wait = WebDriverWait(self.driver,10) #chờ tối đa 10s
    def cart(self):
        # self._select_quanlity_product(number)
        self._add_product_into_cart()
        self._view_cart()
        self._click_delete_button()
        self._click_confirm_delete_product()
        
    # thêm vào giỏ hàng
    def _add_product_into_cart(self):
        add_product_button = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, "(//button[contains(@class,'sc-9e5b140a-1') and @data-view-id='pdp_add_to_cart_button'])"
            ))
        )
        add_product_button.click()
    #xem giỏ hàng
    def _view_cart(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, "(//img[contains(@class, 'cart-icon') and @alt = 'header_header_img_Cart'])"
            ))
        ) 
        cart_button.click()
    # nhấn nút xóa
    def _click_delete_button(self):
        delete_button  = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, "(//img[contains(@alt,'deleted')])[1]" 
            ))
        )
        delete_button.click()
    # nhấn nút confirm
    def _click_confirm_delete_product(self):
        # Chờ popup xác nhận hiển thị
        self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME,
                "ReactModal__Content"
            ))
            
        )
        print ("đã hiển thị pôpup")
        confirm_button = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, "(//div[contains(@class,'dialog-control__button')])"
                ))
        )
        print("đã tìn thấy buttoton")
        
        confirm_button.click()
    