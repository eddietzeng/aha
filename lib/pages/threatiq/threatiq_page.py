from ..basepage import BasePage
from .locators import ThreatiqLocator


class ThreatiqPage(BasePage):
    """
    This is ThreatIQ Page class which inherits from BasePage
    ThreatIQ implementations are defined here
    """
    locator = ThreatiqLocator

    def click_main_page(self):
        """
        This method is to click ThreatIQ page
        """
        try:
            self.click_element(self.locator.btnThreatIQ)
        except RuntimeError as e:
            raise Exception("Failed to click ThreatIQ page: %s" % e)
