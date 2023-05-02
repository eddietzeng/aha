import time
import re

from pathlib import Path
from playwright.sync_api import sync_playwright
from datetime import date

# from pages.login.locators import LoginLocator
# from pages.profile.locators import ProfileLocator


def month_converter(month):
    months = ['January', 'February', 'March',
              'April', 'May', 'June', 'July',
              'August', 'September', 'October',
              'November', 'December'
              ]
    return months.index(month) + 1


def open_firefox_to_page():
    try:
        p = sync_playwright().start()
        browser = p.firefox.launch(headless=True)
        return browser
    except Exception as err:
        print(f"Failed to create browser: {err}")
        return


def sign_in_with_google_oauth(browser, test_page, user, password):
    login_result = False
    try:
        page = browser.new_page()
        # goto aha page
        page.goto(test_page)
        page.wait_for_load_state("domcontentloaded")

        # login to google oauth
        page.click("text=Log In")
        page.click("text=Continue with Google")
        page.locator("input[name='identifier']").fill("eddiefree27@gmail.com")
        page.click("#identifierNext")
        # page.locator("//span[text()='Next' or text()='繼續' or text()='下一步']").click()
        time.sleep(2)
        if not page.locator("input[name='password'], input[name='Passwd']").is_visible():
            page.keyboard.press("Escape")
            page.click("#identifierNext")

        page.locator("input[name='password'], input[name='Passwd']").fill("Ddong6lolcarousell")
        page.click("#passwordNext")

        # wait for loading
        time.sleep(15)

        # skip free trial and tutorial pages
        if page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
            page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()

        if page.locator("//button[text()='Skip']").is_visible():
            page.locator("//button[text()='Skip']").click()

        # check if entering main dashboard
        login_result = page.locator("//a[@href='/sat/profile/account']").is_visible()
        page.screenshot(path=os.path.join()"login.png")
    except Exception as err:
        print(f"err: {err}")
        page.screenshot(path="error.png")
    finally:
        browser.close()
        return login_result


def sign_out(browser, test_page, user, password):
    logout_result = False
    try:
        page = browser.new_page()
        # goto aha page
        page.goto(test_page)
        page.wait_for_load_state("domcontentloaded")

        # login to google oauth
        page.click("text=Log In")
        page.click("text=Continue with Google")
        page.locator("input[name='identifier']").fill("eddiefree27@gmail.com")
        page.click("#identifierNext")
        # page.locator("//span[text()='Next' or text()='繼續' or text()='下一步']").click()
        time.sleep(2)
        if not page.locator("input[name='password'], input[name='Passwd']").is_visible():
            page.keyboard.press("Escape")
            page.click("#identifierNext")

        page.locator("input[name='password'], input[name='Passwd']").fill("Ddong6lolcarousell")
        page.click("#passwordNext")

        # wait for loading
        time.sleep(15)

        # skip free trial and tutorial pages
        if page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
            page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()

        if page.locator("//button[text()='Skip']").is_visible():
            page.locator("//button[text()='Skip']").click()

        page.locator("//a[@href='/sat/profile/account']").is_visible()

        # log out
        page.locator("//a[@href='/sat/profile/account']").nth(0).click()
        page.locator("//a[@href='/sat/profile/settings']").click()
        page.locator("//button[text()='LOG OUT']").click()
        page.locator("//button[text()='Yes']").click()
        time.sleep(3)

        logout_result = page.locator("//body[@class='login-lock']").is_visible()
        page.screenshot(path="logout.png")
    except Exception as err:
        print(f"err: {err}")
        page.screenshot(path="error.png")
    finally:
        browser.close()
        return logout_result


def aha_e2e_test_login_with_googleoauth(browser, test_page, login_user, login_pwd, change_date):
    try:
        page = browser.new_page()
        # goto aha page
        page.goto(test_page)
        page.wait_for_load_state("domcontentloaded")

        target_date = list(map(int, change_date.split("/")))
        year, month, day = target_date[0], target_date[1], target_date[2]

        # login to google oauth
        page.click("text=Log In")
        page.click("text=Continue with Google")
        page.locator("input[name='identifier']").fill("eddiefree27@gmail.com")
        page.click("#identifierNext")
        # page.locator("//span[text()='Next' or text()='繼續' or text()='下一步']").click()
        time.sleep(2)
        if not page.locator("input[name='password'], input[name='Passwd']").is_visible():
            page.keyboard.press("Escape")
            page.click("#identifierNext")

        page.locator("input[name='password'], input[name='Passwd']").fill("Ddong6lolcarousell")
        page.click("#passwordNext")

        # wait for loading
        time.sleep(15)

        # skip free trial and tutorial pages
        if page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
            page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()

        if page.locator("//button[text()='Skip']").is_visible():
            page.locator("//button[text()='Skip']").click()

        # check if entering main dashboard
        login_result = page.locator("//a[@href='/sat/profile/account']").is_visible()
        page.screenshot(path="login.png")
        print(f"login_result: {login_result}")

        # edit birthday date
        page.locator("//a[@href='/sat/profile/account']").click()
        curdate = page.locator("//input[@name='birthday']").get_attribute("value")
        curbir = list(map(int, curdate.split("/")))
        bir_year, bir_month, bir_day = curbir[2], curbir[0], curbir[1]
        if not (date(year, month, day) == date(bir_year, bir_month, bir_day)):
            page.locator("//input[@name='birthday']").click()
            page.locator("//button[@title='Pick year']").click()
            page.locator(f"//button[@data-year='{year}']").click()
            year_month_string = page.locator("//button[@title='Pick year']/p[1]").text_content()
            cur_month = month_converter(year_month_string.split(" ")[0])
            while cur_month != month:
                if cur_month > month:
                    page.locator("//button[@title='Previous month']").click()
                elif cur_month < month:
                    page.locator("//button[@title='Next month']").click()
                else:
                    break
                year_month_string = year_month_string = page.locator("//button[@title='Pick year']/p[1]").text_content()
                cur_month = month_converter(year_month_string.split(" ")[0])
                time.sleep(1)
            page.locator(f"//button[text()='{day}']").nth(0).click()
            page.locator("//button[text()='OK']").click()
            time.sleep(1)

            # clear hightschool graduation
            page.locator("//input[@name='highSchool']").fill("")
            page.keyboard.press("Tab")
            page.keyboard.press("Backspace")
            page.locator(f"//div[text()='Save']").click()
            if page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
                page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()
            page.screenshot(path="change_date.png")
            time.sleep(1)

        # log out
        # page.locator("//a[@href='/sat/profile/account']").nth(0).click()
        page.locator("//a[@href='/sat/profile/settings']").click()
        page.locator("//button[text()='LOG OUT']").click()
        page.locator("//button[text()='Yes']").click()
        time.sleep(3)

        logout_result = page.locator("//body[@class='login-lock']").is_visible()
        page.screenshot(path="logout.png")
        print(f"logout_result: {logout_result}")
        browser.close()
    except Exception as err:
        print(f"err: {err}")
        page.screenshot(path="error.png")


def aha_e2e_test(web_page, login_user, login_pwd, change_date):

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        # goto aha page
        page.goto("https://www.earnaha.com/")

        # login to google oauth
        page.click("text=Log In")
        page.click("text=Continue with Google")
        page.locator("input[name='identifier']").fill("eddiefree27@gmail.com")
        page.click("#identifierNext")
        time.sleep(2)
        try:
            page.keyboard.press("Escape")
            page.click("#identifierNext")
        except Exception as err:
            pass
        page.locator("input[name='password'], input[name='Passwd']").fill("Ddong6lolcarousell")
        page.click("#passwordNext")

        # wait for loading
        time.sleep(15)

        # skip free trial and tutorial pages
        if page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
            page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()

        if page.locator("//button[text()='Skip']").is_visible():
            page.locator("//button[text()='Skip']").click()

        # check if entering main dashboard
        result = page.locator("//a[@href='/sat/profile/account']").is_visible()
        browser.close()
        return result


if __name__ == "__main__":
    # driver_path = get_driver_path("firefox")
    browser, page = open_firefox_to_page()
    aha_e2e_test_login_with_googleoauth(
        browser,
        "https://www.earnaha.com/",
        "eddiefree27@gmail.com",
        "Ddong6lolcarousell",
        "1992/10/11"
    )
