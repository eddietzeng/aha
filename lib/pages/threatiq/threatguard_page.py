from .threatiq_page import ThreatiqPage


class ThreatGuardPage(ThreatiqPage):
    """
    ThreatIQ -> ThreatGuard
    This is ThreatGuard Page class which inherits from ThreatiqPage
    ThreatGuard implementations are defined here
    """

    def click_tab(self):
        """
        This method is to click ThreatGuard tab
        """
        try:
            self.click_element(self.locator.tabThreatGuard)
        except RuntimeError as e:
            raise Exception("Failed to click ThreatGuard tab: %s" % e)
