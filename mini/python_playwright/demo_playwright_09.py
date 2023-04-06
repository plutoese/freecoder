import re
import random
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright



def run(try_count=100):
    run_sign = True
    while(run_sign):
        run_sign = False
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False
            )
            page = browser.new_page()
            page.goto("https://kns.cnki.net/kns/advsearch?dbcode=CCND")
            page.wait_for_timeout(500)
            try:
                page.get_by_text('专业检索').click()
                page.get_by_placeholder('请输入专业检索表达式').fill('SU%=万科 AND (CN="11-0207")')

                page.locator('.search2').click()
                page.wait_for_timeout(1000)

                result_text = page.query_selector_all('.pagerTitleCell')[0].inner_text()
                record_number = int(re.search("\d+", result_text).group())

                page.locator('.icon-detail').click()
                page.locator('[data-val="50"]').click()
                page.wait_for_timeout(2000)
                result_table = page.query_selector_all('.result-detail-list dd')
                
                records = list()
                for row in result_table:
                    record = dict() 
                    soup = BeautifulSoup(row.inner_html(), 'lxml')
                    record["title"] = soup.h6.a.text
                    record["author"] = re.sub("\s+", "", soup.select(".authorinfo > p")[0].text)
                    record_info = [re.sub("\s+", "", item.text) for item in soup.select('.baseinfo > span')]
                    record["source"], record["date"], record["download"] = record_info[0], record_info[1], re.search("\d+", record_info[2]).group()
                    record["abstract"] = soup.select(".abstract > span")[1].text
                    record["link"] = soup.h6.a["href"]

                    records.append(record)
                
                pdata = pd.DataFrame(records)
                print(pdata)
                pdata.to_excel(Path(__file__).parent.joinpath("output/data.xls"), index=False)
                #page.locator('#selectCheckAll1').check()

                #page.locator('#PageNext').click()

            except:
                print("Hello")
                run_sign = True

            page.wait_for_timeout(2000)
            browser.close()

if __name__ == '__main__':
    run()