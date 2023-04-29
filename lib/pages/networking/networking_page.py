from ..basepage import BasePage
from .locators import NetworkingLocator


class NetworkingPage(BasePage):
    """
    This is Networking Page class which inherits from BasePage
    NetworkingPage implementations are defined here
    """
    locator = NetworkingLocator

    def expand(self):
        try:
            ele = self.get_element(self.locator.btnNetworking)
            if ele.get_attribute("aria-expanded") == "false":
                self.click_element(self.locator.btnNetworking)
        except Exception:
            raise RuntimeError("Failed to expand Networking")

    def collapse(self):
        try:
            ele = self.get_element(self.locator.btnNetworking)
            if ele.get_attribute("aria-expanded") == "true":
                self.click_element(self.locator.btnNetworking)
        except Exception:
            raise RuntimeError("Failed to collapse Networking")

    def choose_topology(self):
        try:
            self.click_element(self.locator.btnTopology)
        except RuntimeError as e:
            raise Exception("Failed to click Topology: %s" % e)
