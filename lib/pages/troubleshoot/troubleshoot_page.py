from ..basepage import BasePage
from .locators import TroubleshootLocator


class TroubleshootPage(BasePage):
    """
    This is Troubleshoot Page class which inherits from BasePage
    TroubleshootPage implementations are defined here
    """
    locator = TroubleshootLocator

    def expand(self):
        try:
            ele = self.get_element(self.locator.btnTroubleshoot)
            if ele.get_attribute("aria-expanded") == "false":
                self.click_element(self.locator.btnTroubleshoot)

        except Exception:
            raise RuntimeError("Failed to expand Troubleshoot")

    def collapse(self):
        try:
            ele = self.get_element(self.locator.btnTroubleshoot)
            if ele.get_attribute("aria-expanded") == "true":
                self.click_element(self.locator.btnTroubleshoot)
        except Exception:
            raise RuntimeError("Failed to collapse Troubleshoot")

    def choose_appiq(self):
        try:
            self.click_element(self.locator.btnAppIQ)
        except RuntimeError as e:
            raise Exception("Failed to choose AppIQ: %s" % e)

    def choose_cloud_routes(self):
        # to-do
        pass

    def choose_dignostic_tool(self):
        # to-do
        pass
