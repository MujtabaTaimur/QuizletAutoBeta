import time
from playwright.sync_api import Page

def login(page: Page, username, password):
    page.goto("https://quizlet.com/login")
    page.wait_for_selector('input[name="username"]', timeout=15000)
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.press('input[name="password"]', 'Enter')
    page.wait_for_timeout(5000)
    if "login" in page.url.lower():
        raise RuntimeError("Login failed or requires manual intervention.")
