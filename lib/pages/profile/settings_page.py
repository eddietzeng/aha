from .profile_page import ProfilePage


class SettingsPage(ProfilePage):
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
            self.click_element(self.locator.btnSettings)
            self.skip_to_free_trial()
        except RuntimeError as e:
            raise Exception("Failed to click Licensing tab: %s" % e)

    def click_logout(self):
        """
        This method is to click RESET button
        """
        try:
            self.click_element(self.locator.btnLogOut)
            self.click_element(self.locator.btnYes)
        except RuntimeError as e:
            raise Exception("Failed to click Licensing tab: %s" % e)

    def check_is_logout(self):
        return self.is_element_visible(self.locator.txaLoginToPractice)
