from playwright.sync_api import sync_playwright
 
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
                
        # go to url
        page.goto("https://google.com/")

        page.type('input[name="q"]', "python")
        page.click('input[name="btnK"]')
        page.wait_for_timeout(10000)
        browser.close()
 
if __name__ == '__main__':
    main()