from ..basepage import BasePage
from .locators import TopologyLocator


class TopologyPage(BasePage):
    """
    This is Topology Page class which inherits from BasePage
    Topology implementations are defined here
    """
    locator = TopologyLocator

    def click_main_page(self):
        """
        This method is to click and check Topology page
        """
        try:
            self.click_element(self.locator.btnTopology)
        except RuntimeError as e:
            raise Exception("Failed to click Topology page: %s" % e)
