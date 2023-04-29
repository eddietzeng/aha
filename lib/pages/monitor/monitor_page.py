from ..basepage import BasePage
from .locators import MonitorLocator


class MonitorPage(BasePage):
    """
    This is Monitor Page class which inherits from BasePage
    MonitorPage implementations are defined here
    """
    locator = MonitorLocator

    def expand(self):
        try:
            ele = self.get_element(self.locator.txaMonitor)
            if ele.get_attribute("aria-expanded") == "false":
                self.click_element(self.locator.txaMonitor)
        except Exception:
            raise RuntimeError("Failed to expand Monitor")

    def collapse(self):
        try:
            ele = self.get_element(self.locator.txaMonitor)
            if ele.get_attribute("aria-expanded") == "true":
                self.click_element(self.locator.txaMonitor)
        except Exception:
            raise RuntimeError("Failed to expand Monitor")

    def choose_flowiq(self):
        try:
            self.click_element(self.locator.btnFlowIQ)
        except RuntimeError as e:
            raise Exception("Failed to click Network Graph tab: %s" % e)
