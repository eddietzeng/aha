import time

from selenium.webdriver.common.keys import Keys

from ..basepage import BasePage
from .locators import LoginLocator


class LoginPage(BasePage):
    """
    This is Login Page class which inherits from BasePage
    Login implementations are defined here
    """
    locator = LoginLocator

    def test(self):
        print("XXXXX")

    def click_login_button(self):
        """
        This method is to click login button
        """
        try:
            self.click_element(self.locator.btnLogin)
        except RuntimeError as e:
            raise Exception("Failed to click login button: %s" % e)

    def click_continue_with_google(self):
        """
        This method is to click login button
        """
        try:
            self.click_element(self.locator.btnContGoogle)
        except RuntimeError as e:
            raise Exception("Failed to click login button: %s" % e)

    def click_google_account(self):
        """
        This method is to click login button
        """
        try:
            self.click_element(self.locator.txaGoogleAccount)
        except RuntimeError as e:
            raise Exception("Failed to click login button: %s" % e)

    def click_next_button(self):
        """
        This method is to click login button
        """
        try:
            self.click_element(self.locator.btnNext)
        except RuntimeError as e:
            raise Exception("Failed to click login button: %s" % e)

    def input_google_username(self, user):
        """
        This method is to input username
        @param user: user name for Copilot
        """
        try:
            self.input_text(self.locator.txaGoogleUsername, user)
        except RuntimeError as e:
            raise Exception("Failed to input username: %s" % e)

    def input_googlepassword(self, pwd):
        """
        This method is to input password
        @param pwd: password for Copilot
        """
        try:
            self.input_text(self.locator.txaGooglePassword, pwd)
        except RuntimeError as e:
            raise Exception("Failed to input password: %s" % e)

    def check_if_login_to_dashboard(self):
        self.skip_to_free_trial()
        return self.is_element_visible(self.locator.btnMyProfile)
