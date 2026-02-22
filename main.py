from playwright.sync_api import sync_playwright
import time
import random
def rand_sleep():
    seed=random.randint(1,3)
    time.sleep(seed)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    keyword="linkin park"
    page.goto("https://www.google.com/")
    # rand_sleep()
    page.fill('#APjFqb','123123')
    # rand_sleep()
    page.keyboard.press("Enter")
    page.click("recaptcha-checkbox-checkmark")
    print(page.title())
    time.sleep(100)
    browser.close()
