from .programintent_page import ProgramIntentPage
from selenium.webdriver.common.keys import Keys


class ThreatiqPage(ProgramIntentPage):
    """
    SecurityServices -> ThreatIQ
    This is Threats Page class which inherits from ProgramIntentPage
    Threats implementations are defined here
    """

    def click_threatiq_tag(self):
        try:
            self.click_element(self.locator.btnThreatIQ)
            self.wait_element_visible(self.locator.btnApply, timeout=300)
        except RuntimeError as e:
            raise Exception("Failed to click Network Graph tab: %s" % e)

    def get_threats_row_data(self, rows_num):
        """
        This method is to get threats data in the table
        """
        data = {}
        for i in range(rows_num):
            rows_loc = self.locator.threats_row_locators(i)
            # # v1.8.x
            # src_addr = self.get_element(
            #     rows_loc["src_addr"], focus=True).get_attribute("data-value")
            # dst_addr = self.get_element(
            #     rows_loc["dst_addr"]).get_attribute("data-value")
            # v1.9.0
            src_addr = self.get_element(rows_loc["src_addr"], focus=True).text
            dst_addr = self.get_element(rows_loc["dst_addr"]).text
            host = self.get_element(
                rows_loc["host"]).text
            self.click_element(rows_loc["view_button"])
            self.click_element(self.locator.tabTopology)
            self.click_element(self.locator.tabFlowdata)
            self.click_element(self.locator.tabGeneral)
            self.click_element(self.locator.tabGeoipdst)
            self.click_element(self.locator.tabGeoipsrc)
            self.click_element(self.locator.tabNetflow)
            self.click_element(self.locator.tabSummary)

            self.actionchains().send_keys(Keys.ESCAPE).perform()

            index = f"row_index_{i}"
            data[index] = [src_addr, dst_addr, host]
        return data

    def get_unique_threat_ips(self):
        """
        This method is to get Unique Threat Ips
        """
        return self.get_element(self.locator.txtUniqueThreatIP).text

    def get_threat_count(self):
        """
        This method is to get Threat Count
        """
        return self.get_element(self.locator.txtThreatCount).text

    def get_all_threats(self):
        """
        This method is to get All Threats(Total)
        """
        return self.get_element(self.locator.txtAllThreats).text
