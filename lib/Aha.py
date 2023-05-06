import os
import time
import logging

from pathlib import Path
from playwright.sync_api import sync_playwright
from datetime import date

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)


def month_converter(month):
    months = ['January', 'February', 'March',
              'April', 'May', 'June', 'July',
              'August', 'September', 'October',
              'November', 'December'
              ]
    return months.index(month) + 1


class Aha():
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.browser = None
        self.page = None

    def open_firefox_to_page(self, test_page):
        logger.info(f"Open firefox to page: {test_page}")
        try:
            p = sync_playwright().start()
            self.browser = p.firefox.launch(headless=True)
            self.page = self.browser.new_page()
            self.page.goto(test_page)
            self.page.wait_for_load_state("domcontentloaded")
        except Exception as err:
            logger.error(f"Failed to create browser: {err}")
            self.close()

    def close(self):
        if self.page:
            self.page.close()
        if self.browser:
            self.browser.close()

    def sign_in_with_google_oauth(self, user, password):
        login_result = True
        try:
            # login to google oauth
            logger.info("Login to google oauth")
            self.page.click("text=Log In")
            self.page.click("text=Continue with Google")
            self.page.locator("input[name='identifier']").fill(user)
            self.page.click("//span[text()='Next' or text()='繼續' or text()='下一步']")
            time.sleep(2)
            if not self.page.locator("input[name='password'], input[name='Passwd']").is_visible():
                self.page.keyboard.press("Escape")
                self.page.click("//span[text()='Next' or text()='繼續' or text()='下一步']")

            self.page.locator("input[name='password'], input[name='Passwd']").fill(password)
            self.page.click("//span[text()='Next' or text()='繼續' or text()='下一步']")

            # wait for loading
            time.sleep(15)

            # skip free trial and tutorial pages
            if self.page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
                self.page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()

            if self.page.locator("//button[text()='Skip']").is_visible():
                self.page.locator("//button[text()='Skip']").click()

            # check if entering main dashboard
            login_result = self.page.locator("//a[@href='/sat/profile/account']").is_visible()
            self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "login.png"))
        except Exception as err:
            logger.error("[Exception] sign_in_with_google_oauth ", exc_info=True)
            login_result = False
            self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "login_error.png"))
            self.close()
        finally:
            return login_result

    def sign_out(self):
        logout_result = True
        try:
            # log out
            logger.info("Log out")
            self.page.locator("//a[@href='/sat/profile/account']").nth(0).click()
            time.sleep(1)
            self.page.locator("//a[@href='/sat/profile/settings']").click()
            time.sleep(1)
            self.page.locator("//button[text()='LOG OUT']").click()
            time.sleep(1)
            self.page.locator("//button[text()='Yes']").click()
            time.sleep(3)

            logout_result = self.page.locator("//body[@class='login-lock']").is_visible()
            self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "logout.png"))
        except Exception as err:
            logger.error("[Exception] sign_out ", exc_info=True)
            logout_result = False
            self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "logout_error.png"))
            self.close()
        finally:
            return logout_result

    def change_birthday(self, date_to_change):
        change_result = True
        try:
            target_date = list(map(int, date_to_change.split("/")))
            year, month, day = target_date[2], target_date[0], target_date[1]
            # edit birthday date
            logger.info("Edit birthday date")
            self.page.locator("//a[@href='/sat/profile/account']").click()
            curdate_txt = self.page.locator("//input[@name='birthday']").get_attribute("value")
            curdate = "1/1/1" if not curdate_txt else curdate_txt
            curbir = list(map(int, curdate.split("/")))
            bir_year, bir_month, bir_day = curbir[2], curbir[0], curbir[1]

            if date(year, month, day) != date(bir_year, bir_month, bir_day):
                self.page.locator("//input[@name='birthday']").click()
                self.page.locator("//button[@title='Pick year']").click()
                self.page.locator(f"//button[@data-year='{year}']").click()
                year_month_string = self.page.locator("//button[@title='Pick year']/p[1]").text_content()
                cur_month = month_converter(year_month_string.split(" ")[0])
                while cur_month != month:
                    if cur_month > month:
                        self.page.locator("//button[@title='Previous month']").click()
                    elif cur_month < month:
                        self.page.locator("//button[@title='Next month']").click()
                    else:
                        break
                    year_month_string = year_month_string = self.page.locator("//button[@title='Pick year']/p[1]").text_content()
                    cur_month = month_converter(year_month_string.split(" ")[0])
                    time.sleep(1)
                self.page.locator(f"//button[text()='{day}']").nth(0).click()
                self.page.locator("//button[text()='OK']").click()
                time.sleep(1)

                # clear hightschool graduation
                logger.debug("Clear high school graduation")
                self.page.locator("//input[@name='highSchool']").fill("")
                self.page.keyboard.press("Tab")
                self.page.keyboard.press("Backspace")
                self.page.locator(f"//div[text()='Save']").click()
                if self.page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
                    self.page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()
                time.sleep(1)
            else:
                logger.info(f"Current date is already {date_to_change}. Please input another date")
            self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "date.png"))
        except Exception as err:
            logger.error("[Exception] change_birthday ", exc_info=True)
            change_result = False
            self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "chagedate_error.png"))
            self.close()
        finally:
            return change_result


if __name__ == "__main__":
    obj = Aha()
    obj.open_firefox_to_page("https://www.earnaha.com/")
    loging_result = obj.sign_in_with_google_oauth(
        "eddiefree27@gmail.com",
        "Ddong6lolcarousell"
    )
    print(f"loging: {loging_result}")
    change_result = obj.change_birthday("11/30/1993")
    print(f"change_date: {change_result}")
    logout_result = obj.sign_out()
    print(f"logout: {logout_result}")
