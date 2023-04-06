import re
from playwright.sync_api import sync_playwright, expect

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
        page.wait_for_timeout(500)

        result_text = page.query_selector_all('.pagerTitleCell')[0].inner_text()
        record_number = int(re.search("\d+", result_text).group())

        page.locator('[data-val="50"]').click()
        page.locator('#selectCheckAll1').check()

        page.locator('#PageNext').click()

        page.get_by_role('link', name="导出/参考文献").click()
        page.goto('https://kns.cnki.net/dm/manage/export.html')
        page.wait_for_timeout(1000)

        #page.locator('[displaymode="elearning"]').click()
        #page.get_by_role('link', name="MLA格式引文").click()
        #print(page.query_selector_all('.formatlist li')[1].inner_html())
        #page.query_selector_all('.formatlist li')[1].dblclick()
        with page.expect_download() as download_info:
            # Perform the action that initiates download
            page.locator('[title="导出题录文件"]').click()
            # Wait for the download to start
            download = download_info.value
            # Wait for the download process to complete
            print(download.path())
            # Save downloaded file somewhere
            download.save_as("D:/Download/at.txt")
    except:
        print("Hello")
    #page.frame_locator('[name="majorSearch"]')
    #page.locator('[name="majorSearch"]').click()
    #page.get_by_role("listitem", name="专业检索").click()
    #page.get_by_text("专业检索").hover()
    #page.locator('textarea.textarea-major.ac_input').fill('SU%=万科 AND (CN="11-0207")')

    page.wait_for_timeout(10000)
    browser.close()