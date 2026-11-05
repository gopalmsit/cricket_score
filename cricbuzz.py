from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/live-cricket-scores/173060/wi-vs-ban-2nd-test-west-indies-tour-of-bangladesh-2026")
    page.screenshot(path="cricbuzz_page.png")
    browser.close()