import re
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        url = 'https://airbnb.com/experiences/272085'
        page.goto(url)
        page.wait_for_selector('h1')
        print(page.content())
        return url, page.content()


if __name__ == '__main__':
    url, content = run()