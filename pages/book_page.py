from page_selectors.book_selectors import BookSelectors
from pages.base_page import BasePage

class BookPage(BasePage):
    def get_description(self):
        return self.page.locator(BookSelectors.DESCRIPTION).inner_text()

    def get_upc(self):
        return self.page.locator(BookSelectors.UPC).inner_text()