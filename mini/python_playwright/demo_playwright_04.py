from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()
    page.goto("https://www.amazon.com/Hitchhikers-Guide-Galaxy-Douglas-Adams-ebook/dp/B000XUBC2C")

	# Create a dictionary with the scraped data
    book = {
        "book_title": page.query_selector('#productTitle').inner_text().strip(),
        "author": page.query_selector('span.author a').inner_text().strip(),
        "edition": page.query_selector('#productSubtitle').inner_text().strip(),
        "price": page.query_selector('.a-size-base.a-color-price.a-color-price').inner_text().strip(),
    }

    print(book)
    page.screenshot(path="book.png")
    
    browser.close()