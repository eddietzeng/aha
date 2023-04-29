from ..basepage import BasePage
from .locators import ProfileLocator


class ProfilePage(BasePage):
    """
    This is Settings Page class which inherits from BasePage
    Settings implementations are defined here
    """
    locator = ProfileLocator

    def click_main_page(self):
        """
        This method is to click and check Profile page
        """
        try:
            self.click_element(self.locator.btnMyProfile)
            self.skip_to_free_trial()
        except RuntimeError as e:
            raise Exception("Failed to click Settings page: %s" % e)
