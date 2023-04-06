from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()
    page.goto("https://s.ecust.edu.cn/")
    page.get_by_text("统一身份验证登录").hover()
    page.get_by_role("link", name="本科教育").click()
    page.get_by_role("button", name="继续").click()

    page.wait_for_selector('#username')
    page.locator('#username').fill("07995")
    page.locator("#password").fill("z1Yh290000")
    page.get_by_role("button", name="登录").click()

    page.locator('.hd_login_after_name').hover()
    page.get_by_role("link", name="个人中心").click()

    items = page.query_selector_all('[iswzykc="0"]')
    for item in items:
        print(item.inner_html())

    page.wait_for_timeout(10000)
    browser.close()