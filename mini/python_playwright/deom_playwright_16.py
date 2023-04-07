import re
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, expect

central_df = pd.read_excel(Path(__file__).parent.joinpath("newspaper/central_newspaper.xlsx"))
local_df1 = pd.read_excel(Path(__file__).parent.joinpath("newspaper/loval_newspaper_v1.xlsx"))
local_df2 = pd.read_excel(Path(__file__).parent.joinpath("newspaper/loval_newspaper_v2.xlsx"))

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()

    central_set = set()
    for row in central_df.itertuples(index=False):
        row_dict = row._asdict()

        if row_dict["name"] not in central_set:
            central_set.add(row_dict["name"])

            page.goto(row_dict["link"])
            page.wait_for_timeout(500)

            page.locator("#J_sumBtn-stretch").click()
            page.wait_for_timeout(200)
            content = page.query_selector_all('[class="more"] > [class="hostUnit"] > span')
            print([item.inner_text() for item in content])

        break

    browser.close()

