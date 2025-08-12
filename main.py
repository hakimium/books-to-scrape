from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from utils.helpers import save_to_csv

# In main.py
def scrape_books():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        home_page = HomePage(page)
        
        home_page.page.goto("http://books.toscrape.com/")
        books = []
        page_count = 1
        
        while True:
            print(f"Scraping page {page_count}...")
            titles = home_page.get_all_titles()
            books.extend([{"title": title} for title in titles])
            
            if not home_page.go_to_next_page():
                break
                
            page_count += 1
            if page_count > 3:  # Safety limit - remove for full scrape
                break
        
        save_to_csv(books, "books.csv")
        print(f"Scraped {len(books)} books from {page_count} pages")
        browser.close()

if __name__ == "__main__":
    scrape_books()