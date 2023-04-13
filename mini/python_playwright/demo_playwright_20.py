import re
import time
import random
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def get_report_table():
    companies_data = pd.read_excel(Path(__file__).parent.joinpath(f"input/companies.xlsx"))
    output_dir = Path(__file__).parent.joinpath("output")
    companies_done = {re.split("\_", file_path.name)[0] for file_path in output_dir.iterdir()}

    for company in companies_data["company"].values:
        if company not in companies_done:
            print(company)
            search_str = f'(SU%={company} OR KY={company} OR TI={company} OR CO={company}) AND (FT="{company} $ 2" AND FT="公司" $ 2) AND (CN="11-0207")'
            search(search_str=search_str, output_template=company)
            time.sleep(random.randrange(2, 10))


def search(try_times=10, search_str='SU%=万科 AND (CN="11-0207")', output_template="万科"):
    run_sign = True
    try_count = 1

    while(run_sign):
        print("starting...")
        run_sign = False

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False
            )
            page = browser.new_page()
            page.goto("https://kns.cnki.net/kns/advsearch?dbcode=CCND")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(random.randrange(500, 1000))

            try:
                page.get_by_text('专业检索').click()
                page.get_by_placeholder('请输入专业检索表达式').fill(search_str)

                page.locator('.search2').click()
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(random.randrange(1000, 2000))

                result_text = page.query_selector_all('.pagerTitleCell')[0].inner_text()
                record_number = int(re.search("\d+", result_text).group())
                
                page.locator('.icon-detail').click()
                page.locator('[data-val="50"]').wait_for()
                page.locator('[data-val="50"]').click()

                if record_number > 0:
                    for page_number in range(1, (record_number//50)+2):
                        print(page_number)
                        if page_number > 1:
                            page.locator('#PageNext').click()
                        page.wait_for_load_state("networkidle")
                        page.wait_for_timeout(random.randrange(1000, 2000))

                        result_table = page.query_selector_all('.result-detail-list dd')
                        
                        records = list()
                        for row in result_table:
                            record = dict() 
                            soup = BeautifulSoup(row.inner_html(), 'lxml')
                            record["title"] = soup.h6.a.text
                            if len(soup.select(".authorinfo > p")) > 0:
                                record["author"] = re.sub("\s+", "", soup.select(".authorinfo > p")[0].text)
                            else:
                                record["author"] = None
                            record_info = [re.sub("\s+", "", item.text) for item in soup.select('.baseinfo > span')]
                            record["source"], record["date"] = record_info[0], record_info[1]
                            record["year"] = int(record["date"][0:4])
                            record["abstract"] = re.sub("\s+", "", soup.select(".abstract > span")[1].text)
                            record["link"] = soup.h6.a["href"]
                            records.append(record)
                        
                        pdata = pd.DataFrame(records)
                        pdata.to_excel(Path(__file__).parent.joinpath(f"output/{output_template}_{page_number}.xlsx"), index=False)
                        
                else:
                    print("No record!")

            except Exception:
                print("Wrong!!!")
                try_count += 1
                if try_count < try_times:
                    run_sign = True
                    page.wait_for_timeout(random.randrange(500, 2000))
                    
            finally:
                page.wait_for_timeout(random.randrange(1000, 2000))
                browser.close()



if __name__ == '__main__':
    get_report_table()
    #search()