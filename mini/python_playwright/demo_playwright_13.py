import re
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()
    page.goto("https://navi.cnki.net/knavi/newspapers/index?uniplatform=NZKPT")
    page.wait_for_timeout(500)
    try:
        page.locator('[title="中央级"]').click()
        page.wait_for_timeout(500)
        page.locator('[title="列表模式"]').click()
        page.wait_for_timeout(500)
        rows = page.query_selector_all('[class="list_tab"] > li')

        for row in rows[1:]:
            row_data = [item.inner_text() for item in row.query_selector_all('span')]
            print(row_data[0])
            content = page.locator(f'[title="{row_data[0]}"]')
            href = content.get_attribute('href')
            link = f"https://navi.cnki.net/knavi/newspapers/{re.split('=',href)[-1]}/detail?uniplatform=NZKPT"
            print(link)


    except:
        print("Hello")

    page.wait_for_timeout(2000)
    browser.close()