from ..basepage import BasePage
from .locators import ProgramIntentLocator


class ProgramIntentPage(BasePage):
    """
    This is SecurityServices Page class which inherits from BasePage
    SecurityServicesPage implementations are defined here
    """
    locator = ProgramIntentLocator

    def expand(self):
        try:
            ele = self.get_element(self.locator.btnProgramIntent)
            if ele.get_attribute("aria-expanded") == "false":
                self.click_element(self.locator.btnProgramIntent)

        except Exception:
            raise RuntimeError("Failed to expand Security")

    def collapse(self):
        try:
            ele = self.get_element(self.locator.btnProgramIntent)
            if ele.get_attribute("aria-expanded") == "true":
                self.click_element(self.locator.btnProgramIntent)

        except Exception:
            raise RuntimeError("Failed to collapse Security")

    def choose_security(self):
        try:
            self.click_element(self.locator.btnSecurity)
        except RuntimeError as e:
            raise Exception("Failed to click Network Graph tab: %s" % e)

    def choose_anomaly(self):
        # to-do
        pass

    def choose_geoblocking(self):
        # to-do
        pass
