from ..basepage import BasePage
from .locators import AdministrationLocator


class AdministrationPage(BasePage):
    """
    This is Administration Page class which inherits from BasePage
    AdministrationPage implementations are defined here
    """
    locator = AdministrationLocator

    def expand(self):
        try:
            ele = self.get_element(self.locator.btnAdmin)
            if ele.get_attribute("aria-expanded") == "false":
                self.click_element(self.locator.btnAdmin)
        except Exception:
            raise RuntimeError("Failed to expand Administration")

    def collapse(self):
        try:
            ele = self.get_element(self.locator.btnAdmin)
            if ele.get_attribute("aria-expanded") == "true":
                self.click_element(self.locator.btnAdmin)
        except Exception:
            raise RuntimeError("Failed to collapse Administration")

    def choose_reports(self):
        try:
            self.click_element(self.locator.btnReports)
        except RuntimeError as e:
            raise Exception("Failed to choose Reports: %s" % e)

    def choose_audit(self):
        try:
            self.click_element(self.locator.btnAudit)
        except RuntimeError as e:
            raise Exception("Failed to choose Audit: %s" % e)
