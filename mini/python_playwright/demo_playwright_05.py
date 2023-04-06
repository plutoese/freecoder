from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()
    page.goto("https://scrapeme.live/shop/")

	# Create a dictionary with the scraped data
    items = page.query_selector_all("li.post*") 

    for i in items: 
        scraped_element = {} 
    
        # Product name 
        el_title = i.query_selector("h2") 
        scraped_element["product"] = el_title.inner_text() 
        
        # Product price 
        el_price = i.query_selector("span.woocommerce-Price-amount") 
        scraped_element["price"] = el_price.text_content()

        print(scraped_element)
    
    browser.close()