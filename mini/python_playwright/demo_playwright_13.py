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

    newspaper_name = ["name", "host", "form", "city", "download", "citation", "link"]
    newspaper_list = list()

    try:
        page.locator('[title="中央级"]').click()
        page.wait_for_timeout(500)
        page.locator('[title="列表模式"]').click()
        page.wait_for_timeout(500)

        for i in range(9):
            rows = page.query_selector_all('[class="list_tab"] > li')
            for row in rows[1:]:
                row_data = [item.inner_text() for item in row.query_selector_all('span')]
                print(row_data)
                content = page.locator(f'[title="{row_data[0]}"]')
                href = content.get_attribute('href')
                link = f"https://navi.cnki.net/knavi/newspapers/{re.split('=',href)[-1]}/detail?uniplatform=NZKPT"
                row_data.append(link)
                print(row_data)
                newspaper_list.append(dict(zip(newspaper_name, row_data)))
            if i < 8:
                page.locator('[class="next"]').click()
                page.wait_for_timeout(1500)

        print(newspaper_list)
    except:
        print("Hello")

    page.wait_for_timeout(2000)
    browser.close()

    pdata = pd.DataFrame(newspaper_list)
    pdata.to_excel(Path(__file__).parent.joinpath("newspaper/central_newspaper.xlsx"), index=False)