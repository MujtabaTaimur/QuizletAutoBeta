from playwright.sync_api import sync_playwright

def launch_browser(headless=True):
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()
    return pw, browser, context, page
