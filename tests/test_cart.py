import os
from pages.cart_page import CartPage

def test_cart(driver):
    
    cartpage = CartPage(driver)
    cartpage.cart()