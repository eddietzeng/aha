import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .profile_page import ProfilePage


def month_converter(month):
    months = ['January', 'February', 'March',
              'April', 'May', 'June', 'July',
              'August', 'September', 'October',
              'November', 'December'
              ]
    return months.index(month) + 1


class MyProfilePage(ProfilePage):
    """
    Settings -> Licensing
    This is Licensing Page class which inherits from SettingsPage
    Licensing implementations are defined here
    """

    def click_tab(self):
        """
        This method is to click Licensing tab
        """
        try:
            self.click_element(self.locator.btnMyProfile)
            self.skip_to_free_trial()
        except RuntimeError as e:
            raise Exception("Failed to click MyProfile tab: %s" % e)

    def choose_birthday_date(self, year, month, day):
        """
        This method is to click RESET button
        """
        try:
            self.click_element(self.locator.txaBirthday)
            time.sleep(1)
            self.click_element(self.locator.btnPickyear)
            self.get_element(self.locator.btnYear(year), focus=True)
            self.click_element(self.locator.btnYear(year))
            year_month_string = self.get_element(self.locator.txtYearMonth).text
            cur_month = month_converter(year_month_string.split(" ")[0])
            while cur_month != month:
                if cur_month > month:
                    self.click_element(self.locator.btnPrevMonth)
                elif cur_month < month:
                    self.click_element(self.locator.btnNextMonth)
                else:
                    break
                year_month_string = self.get_element(self.locator.txtYearMonth).text
                cur_month = month_converter(year_month_string.split(" ")[0])
                time.sleep(1)
            self.click_element(self.locator.btnDay(day))
            self.click_element(self.locator.btnOK)
            time.sleep(1)
        except RuntimeError as e:
            raise Exception("Failed to click Licensing tab: %s" % e)

    def click_save(self):
        try:
            self.click_element(self.locator.txtSave)
            self.skip_to_free_trial()
        except RuntimeError as e:
            raise Exception("Failed to click MyProfile tab: %s" % e)

    def get_birthday_date(self):
        try:
            ele = self.get_element(self.locator.txaBirthday)
            return ele.get_attribute("value")
        except RuntimeError as e:
            return ""

    def clear_highschool_graduation(self):
        try:
            self.input_text(self.locator.txaHighSchool, "")
            self.actionchains().send_keys(Keys.TAB).send_keys(
                Keys.DELETE).perform()
            # ele.send_keys(Keys.CONTROL + "a")
            # ele.send_keys(Keys.DELETE)
        except RuntimeError as e:
            raise Exception("Failed to click MyProfile tab: %s" % e)
