import os
from pages.search_page import SearchPage

def test_search(driver):
    keyword=os.getenv("KEYWORD")
    
    login_page = SearchPage(driver)
    login_page.search(keyword)