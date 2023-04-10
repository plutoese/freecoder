import re
import pandas as pd
from pathlib import Path
from random import randrange
from playwright.sync_api import sync_playwright, expect

"""
central_df = pd.read_excel(Path(__file__).parent.joinpath("newspaper/central_newspaper.xlsx"))
central_df["level"] = "中央级"
local_df1 = pd.read_excel(Path(__file__).parent.joinpath("newspaper/loval_newspaper_v1.xlsx"))
local_df2 = pd.read_excel(Path(__file__).parent.joinpath("newspaper/loval_newspaper_v2.xlsx"))
local_df1["level"] = "地方级"
local_df2["level"] = "地方级"

ndf = pd.concat([central_df, local_df1, local_df2], ignore_index=True)
ndf = ndf.drop_duplicates()
print(ndf.shape)
ndf.to_excel(Path(__file__).parent.joinpath("newspaper/newspaper.xlsx"), index=False)"""

newspaper_df = pd.read_excel(Path(__file__).parent.joinpath("newspaper/newspaper.xlsx"))

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()

    i = 1
    newspaper_list = []
    for row in newspaper_df.itertuples(index=False):
        print(i)
        if i < 500:
            i += 1
            continue

        row_dict = row._asdict()
        print(row_dict["name"], row_dict["link"])
        record = {"报刊名称": row_dict["name"], "级别": row_dict['level']}

        page.goto(row_dict["link"])
        page.wait_for_timeout(500)

        page.locator("#J_sumBtn-stretch").click()
        page.wait_for_timeout(300)

        for query_id in ["NBaseInfo", "NContactInfo"]:
            labels = page.query_selector_all(f'[id="{query_id}"] > li > p > label')
            contents = page.query_selector_all(f'[id="{query_id}"] > li > p > span')
            record.update(dict(zip([item.inner_text() for item in labels], [item.inner_text() for item in contents])))

        record.update({"下载次数": row_dict["download"], "引用次数": row_dict["citation"]})
        print(record)
        newspaper_list.append(record)

        #if i > 600:
        #    break

        i += 1

        page.wait_for_timeout(randrange(500, 1000))

    browser.close()

    pdata = pd.DataFrame(newspaper_list)
    pdata.to_excel(Path(__file__).parent.joinpath("newspaper/newspaper_info_v3.xlsx"), index=False)

