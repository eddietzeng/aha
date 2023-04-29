from ..basepage import BasePage
from .locators import SecurityLocator


class SecurityPage(BasePage):
    """
    This is SecurityServices Page class which inherits from BasePage
    SecurityServicesPage implementations are defined here
    """
    locator = SecurityLocator

    def expand(self):
        try:
            ele = self.get_element(self.locator.btnSecurity)
            if ele.get_attribute("aria-expanded") == "false":
                self.click_element(self.locator.btnSecurity)

        except Exception:
            raise RuntimeError("Failed to expand Security")

    def collapse(self):
        try:
            ele = self.get_element(self.locator.btnSecurity)
            if ele.get_attribute("aria-expanded") == "true":
                self.click_element(self.locator.btnSecurity)

        except Exception:
            raise RuntimeError("Failed to collapse Security")

    def choose_threatiq(self):
        try:
            self.click_element(self.locator.btnThreatIQ)
        except RuntimeError as e:
            raise Exception("Failed to click Network Graph tab: %s" % e)

    def choose_anomaly(self):
        # to-do
        pass

    def choose_geoblocking(self):
        # to-do
        pass
