import os
import re
import time
import logging
import asyncio


from pathlib import Path
from playwright.async_api import async_playwright
from datetime import date

import mailslurp_utils

RE_ACTIVELINK = re.compile(r"https:\/\/aha\.jp\.auth0\.com\/[^\s]+")

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ...


def month_converter(month):
    months = ['January', 'February', 'March',
              'April', 'May', 'June', 'July',
              'August', 'September', 'October',
              'November', 'December'
              ]
    return months.index(month) + 1


def create_mailslurp_inbox():
    try:
        new_inbox = inbox_controller.create_inbox()
        return new_inbox
    except ApiException as e:
        print("An exception occurred while creating the MailSlurp inbox: %s\n" % e)
        return None


class Aha():
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"

    def __init__(self):
        self.browser = None
        self.page = None
        self.api_key = os.environ.get("")
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def open_firefox_to_page(self, test_page):
        self.loop.run_until_complete(self._open_firefox_to_page_async(test_page))

    def close(self):
        self.loop.run_until_complete(self._close_async())
        self.loop.close()

    def sign_up_with_email(self, mailslurp_api_key, password="Password@123"):
        return self.loop.run_until_complete(self._sign_up_with_email_async(mailslurp_api_key, password))

    def sign_in_with_google_oauth(self, user, password):
        return self.loop.run_until_complete(self._sign_in_with_google_oauth_async(user, password))

    def sign_in_with_email(self, user, password):
        return self.loop.run_until_complete(self._sign_in_with_email_async(user, password))

    def sign_out(self):
        return self.loop.run_until_complete(self._sign_out_async())

    def change_birthday(self, date_to_change):
        return self.loop.run_until_complete(self._change_birthday_async(date_to_change))

    async def _open_firefox_to_page_async(self, test_page):
        logger.info(f"Open firefox to page: {test_page}")
        try:
            p = await async_playwright().start()
            self.browser = await p.firefox.launch(headless=True)
            self.page = await self.browser.new_page()
            await self.page.goto(test_page)
            await self.page.wait_for_load_state("domcontentloaded")
        except Exception as err:
            logger.error(f"Failed to create browser: {err}")

    async def _close_async(self):
        if self.page:
            await self.page.close()

        if self.browser:
            await self.browser.close()

    async def _sign_up_with_email_async(self, mailslurp_api_key, password):
        signup_result = True
        try:
            inbox = mailslurp_utils.create_mailslurp_inbox(mailslurp_api_key)
            logger.info(f"Sign up email: {inbox.email_address}")
            # login to google oauth
            logger.info("Sign up with email")
            await self.page.click("text=Sign Up")
            await self.page.locator("input[name='email']").fill(inbox.email_address)
            await self.page.locator("input[name='password']").fill(password)
            time.sleep(1)
            await self.page.locator("//button[@name='action']").click()
            time.sleep(20)
            await self._skip_free_trial()

            activation_email = mailslurp_utils.wait_for_latest_email(mailslurp_api_key, inbox)
            logger.debug(activation_email.body)
            activation_link = RE_ACTIVELINK.search(activation_email.body).group(0)
            logger.info(f"Activation link: {activation_link}")
            await self.page.goto(activation_link)
            time.sleep(5)
            await self._skip_free_trial()
        except Exception as err:
            logger.error("[Exception] sign_in_with_google_oauth ", exc_info=True)
            signup_result = False
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "error_signup_with_email_error.png"))
        finally:
            return signup_result

    async def _sign_in_with_email_async(self, user, password):
        login_result = True
        try:
            # login to google oauth
            logger.info("Login with email")
            await self.page.click("text=Log In")
            await self.page.locator("input[name='username']").fill(user)
            await self.page.locator("input[name='password']").fill(password)
            time.sleep(1)
            await self.page.locator("//button[@name='action']").click()

            # wait for loading
            time.sleep(20)

            await self._skip_free_trial()

            # check if entering main dashboard
            login_result = await self.page.locator("//a[@href='/sat/profile/account']").is_visible()
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "login_with_email.png"))
        except Exception as err:
            logger.error("[Exception] sign_in_with_google_oauth ", exc_info=True)
            login_result = False
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "error_login_with_email.png"))
        finally:
            return login_result

    async def _sign_in_with_google_oauth_async(self, user, password):
        login_result = True
        try:
            # login to google oauth
            logger.info("Login to google oauth")
            await self.page.click("text=Log In")
            await self.page.click("text=Continue with Google")
            await self.page.locator("input[name='identifier']").fill(user)
            await self.page.click("//span[text()='Next' or text()='繼續' or text()='下一步']")
            time.sleep(2)
            if not (await self.page.locator("input[name='password'], input[name='Passwd']").is_visible()):
                await self.page.keyboard.press("Escape")
                await self.page.click("//span[text()='Next' or text()='繼續' or text()='下一步']")

            await self.page.locator("input[name='password'], input[name='Passwd']").fill(password)
            await self.page.click("//span[text()='Next' or text()='繼續' or text()='下一步']")

            # wait for loading
            time.sleep(20)

            await self._skip_free_trial()

            # check if entering main dashboard
            login_result = await self.page.locator("//a[@href='/sat/profile/account']").is_visible()
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "login.png"))
        except Exception as err:
            logger.error("[Exception] sign_in_with_google_oauth ", exc_info=True)
            login_result = False
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "login_error.png"))
        finally:
            return login_result

    async def _sign_out_async(self):
        logout_result = True
        try:
            # log out
            logger.info("Log out")
            await self.page.locator("//a[@href='/sat/profile/account']").nth(0).click()
            time.sleep(1)
            await self.page.locator("//a[@href='/sat/profile/settings']").click()
            time.sleep(1)
            await self.page.locator("//button[text()='LOG OUT']").click()
            time.sleep(1)
            await self.page.locator("//button[text()='Yes']").click()
            time.sleep(3)
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "logout.png"))
        except Exception as err:
            logger.error("[Exception] sign_out ", exc_info=True)
            logout_result = False
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "logout_error.png"))
        finally:
            return logout_result

    async def _change_birthday_async(self, date_to_change):
        change_result = True
        try:
            self._skip_free_trial()

            target_date = list(map(int, date_to_change.split("/")))
            year, month, day = target_date[2], target_date[0], target_date[1]
            # edit birthday date
            logger.info("Edit birthday date")
            await self.page.locator("//a[@href='/sat/profile/account']").click()
            await self.page.locator("//input[@name='birthday']").scroll_into_view_if_needed()
            curdate_txt = await self.page.locator("//input[@name='birthday']").get_attribute("value")
            curdate = "1/1/1" if not curdate_txt else curdate_txt
            curbir = list(map(int, curdate.split("/")))
            bir_year, bir_month, bir_day = curbir[2], curbir[0], curbir[1]

            if date(year, month, day) != date(bir_year, bir_month, bir_day):
                await self.page.locator("//input[@name='birthday']").click()
                await self.page.locator("//button[@title='Pick year']").click()
                await self.page.locator(f"//button[@data-year='{year}']").scroll_into_view_if_needed()
                await self.page.locator(f"//button[@data-year='{year}']").click()
                time.sleep(1)
                year_month_string = await self.page.locator("//button[@title='Pick year']/p[1]").text_content()
                cur_month = month_converter(year_month_string.split(" ")[0])
                logger.info(f"cur_month: {cur_month}")
                logger.info(f"month_to_pick: {month}")
                while cur_month != month:
                    if cur_month > month:
                        await self.page.locator("//button[@title='Previous month']").click()
                    elif cur_month < month:
                        await self.page.locator("//button[@title='Next month']").click()
                    else:
                        break
                    year_month_string = year_month_string = await self.page.locator("//button[@title='Pick year']/p[1]").text_content()
                    cur_month = month_converter(year_month_string.split(" ")[0])
                    time.sleep(1)
                if day < 16:
                    await self.page.locator(f"//button[text()='{day}']").nth(0).click()
                else:
                    await self.page.locator(f"//button[text()='{day}']").nth(-1).click()
                await self.page.locator("//button[text()='OK']").click()
                time.sleep(1)

                # clear hightschool graduation
                logger.debug("Clear high school graduation")
                await self.page.locator("//input[@name='highSchool']").fill("")
                await self.page.keyboard.press("Tab")
                await self.page.keyboard.press("Backspace")
                await self.page.locator(f"//div[text()='Save']").click()
                self._skip_free_trial()
                time.sleep(3)
            else:
                logger.info(f"Current date is already {date_to_change}. Please input another date")
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "date.png"))
        except Exception as err:
            logger.error("[Exception] change_birthday ", exc_info=True)
            change_result = False
            await self.page.screenshot(path=Path(__file__).absolute().parent.parent.joinpath("results", "chagedate_error.png"))
            self.close()
        finally:
            return change_result

    async def _skip_free_trial(self):
        # skip free trial and tutorial pages
        if await self.page.locator("//*[@id='__next']/div[1]/div/div[1]/button").is_visible():
            logger.info("Skip free trial")
            await self.page.locator("//*[@id='__next']/div[1]/div/div[1]/button").click()
            time.sleep(2)
            if await self.page.locator("//*[@id='__next']/div[1]/div/div[2]/div/button[1]").is_visible():
                await self.page.locator("//*[@id='__next']/div[1]/div/div[2]/div/button[1]").click()


if __name__ == "__main__":
    api_key = os.environ.get("MAILSLURP_API_KEY")
    obj = Aha2()
    obj.open_firefox_to_page("https://www.earnaha.com/")
    obj.sign_up_with_email(api_key)
    # loging_result = obj.sign_in_with_google_oauth(
    #     "eddiefree27@gmail.com",
    #     "Ddong6lolcarousell"
    # )
    # print(f"loging: {loging_result}")
    # change_result = obj.change_birthday("12/26/1990")
    # print(f"change_date: {change_result}")
    # logout_result = obj.sign_out()
    # print(f"logout: {logout_result}")
