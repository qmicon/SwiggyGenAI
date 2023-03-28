from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, devtools=True)
    page = browser.new_page()

    page.goto('https://www.swiggy.com/')
    login_link = page.wait_for_selector('a:has-text("Login")')
    login_link.click()
    mobile_input = page.wait_for_selector('#mobile')
    print("Type your Mobile Number")
    mobile_number = str(input())
    mobile_input.type(mobile_number)
    form = page.wait_for_selector('form')
    login_link = form.wait_for_selector('a:has-text("Login")')
    login_link.click()
    otp_input = page.wait_for_selector('#otp')
    print("Type your OTP Number")
    otp_num = str(input())
    otp_input.type(otp_num)
    form = page.wait_for_selector('form')
    verify_otp = form.wait_for_selector('a:has-text("VERIFY OTP")')
    verify_otp.click()
    page.goto('https://www.swiggy.com/city/bangalore')
    page.wait_for_timeout(500000)