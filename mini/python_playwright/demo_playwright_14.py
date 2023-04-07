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
        page.locator('[title="地方级"]').hover()
        page.wait_for_timeout(500)

        province_content = page.query_selector_all('[class="resecondlayer"] > dd')
        province_list = [re.split("\(", re.sub("\s+", "", item.inner_text()))[0] for item in province_content]
        
        print(province_list)

        for province in province_list:
            print(province)
            page.locator('[title="地方级"]').hover()
            page.wait_for_timeout(500)
            page.locator(f'[title="{province}"]').click()
            page.wait_for_timeout(500)
            page.locator('[title="列表模式"]').click()
            page.wait_for_timeout(1000)

            sign = True
            while sign:
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

                try:
                    page.locator('[class="next"]').click()
                    page.wait_for_timeout(200)
                    sign = True
                except:
                    sign = False

        print(newspaper_list)
    except:
        print("Hello")

    page.wait_for_timeout(2000)
    browser.close()

    pdata = pd.DataFrame(newspaper_list)
    pdata.to_excel(Path(__file__).parent.joinpath("newspaper/loval_newspaper_v1.xlsx"), index=False)