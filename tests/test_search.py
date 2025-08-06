import os
from pages.search_page import SearchPage

def test_search(driver):
    keyword=os.getenv("KEYWORD")
    
    search_page = SearchPage(driver)
    search_page.search(keyword)