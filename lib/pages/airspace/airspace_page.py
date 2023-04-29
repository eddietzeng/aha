from ..basepage import BasePage
from .locators import AirSpaceLocator


class AirSpacePage(BasePage):
    """
    This is Networking Page class which inherits from BasePage
    NetworkingPage implementations are defined here
    """
    locator = AirSpaceLocator

    def expand(self):
        try:
            ele = self.get_element(self.locator.btnAirSpace)
            if ele.get_attribute("aria-expanded") == "false":
                self.click_element(self.locator.btnAirSpace)
        except Exception:
            raise RuntimeError("Failed to expand Networking")

    def collapse(self):
        try:
            ele = self.get_element(self.locator.btnAirSpace)
            if ele.get_attribute("aria-expanded") == "true":
                self.click_element(self.locator.btnAirSpace)
        except Exception:
            raise RuntimeError("Failed to collapse Networking")

    def choose_topology(self):
        try:
            self.click_element(self.locator.btnTopology)
            if self.is_element_present(self.locator.btnClose):
                self.click_element(self.locator.btnClose)
        except RuntimeError as e:
            raise Exception("Failed to click Topology: %s" % e)
