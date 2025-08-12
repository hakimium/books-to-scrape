# In pages/home_page.py
from playwright.sync_api import expect
from page_selectors.home_selectors import HomeSelectors
from pages.base_page import BasePage

class HomePage(BasePage):
    def get_all_titles(self):
        return self.page.locator(HomeSelectors.BOOK_TITLES).all_inner_texts()
    
    def go_to_next_page(self):
        next_btn = self.page.locator(HomeSelectors.NEXT_BTN)
        if next_btn.count() > 0:
            next_btn.click()
            self.page.wait_for_load_state("networkidle")
            return True
        return False
    
    def get_current_page_number(self):
        return self.page.locator(HomeSelectors.CURRENT_PAGE).inner_text()