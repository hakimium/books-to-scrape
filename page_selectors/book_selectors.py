class BookSelectors:
    DESCRIPTION = "#product_description + p"
    UPC = "th:has-text('UPC') + td"
    PRICE = ".price_color"