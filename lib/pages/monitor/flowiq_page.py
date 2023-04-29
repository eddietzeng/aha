import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from .monitor_page import MonitorPage


class FlowiqPage(MonitorPage):
    """
    Monitor -> FlowIQ
    This is FlowIQ Page class which inherits from MonitorPage
    FlowIQ implementations are defined here
    """

    def click_records_tab(self):
        """
        This method is to click Network tab
        """
        try:
            self.click_element(self.locator.tabRecords)
        except RuntimeError as e:
            raise Exception("Failed to click Records tab: %s" % e)

    def toggle_resolve_hostnames(self):
        """
        This method is to toggle option "Resolve Hostnames"
        """
        self.log.info("Toggle resolve hostnames")
        try:
            self.click_element(self.locator.btnGear)
            self.click_element(self.locator.chkResolveHostname)
            self.actionchains().send_keys(
                Keys.ESCAPE).perform()
            self.wait_element_visible(self.locator.btnApply, timeout=300)
        except Exception as e:
            raise Exception("Failed to toggle Resolve Hostnames: %s" % e)

    def click_date_range_by_last(self, date_range):
        """
        This method is to click last date range for traffic data refreshing
        """
        try:
            if date_range == "hour":
                self.click_element(self.locator.tabLasthour)
            elif date_range == "day":
                self.click_element(self.locator.tabLastday)
            elif date_range == "week":
                self.click_element(self.locator.tabLastweek)
            elif date_range == "month":
                self.click_element(self.locator.tabLastmonth)
            else:
                raise ValueError(f"{date_range} is not supported")
        except Exception as e:
            raise Exception("Failed to click date range tab: %s" % e)

    def filter_by_source_address(self, ip_addr):
        """
        This method is to add Source Address into filter condition
        """
        self.log.info(f"Source Address: {ip_addr}")
        try:
            self.click_element(self.locator.btnAddrule)
            ele_rule = self.get_element(self.locator.txaSelectfield)
            ele_rule.send_keys(Keys.CONTROL + "a")
            ele_rule.send_keys(Keys.DELETE)
            time.sleep(2)
            ele_rule.send_keys("Source Address")
            self.actionchains().send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
            self.actionchains().send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
            self.actionchains().send_keys(ip_addr).send_keys(
                Keys.DOWN).send_keys(Keys.ENTER).send_keys(Keys.ESCAPE).perform()

        except Exception as e:
            raise Exception("Failed to choose filter source_address: %s" % e)

    def filter_by_source_csp_tag(self, tag_name, instance):
        """
        This method is to add Source Address into filter condition
        """
        self.log.info(f"Tag Name: {tag_name}\nInstance: {instance}")
        try:
            self.click_element(self.locator.btnAddrule)
            ele_rule = self.get_element(self.locator.txaSelectfield)
            ele_rule.send_keys(Keys.CONTROL + "a")
            ele_rule.send_keys(Keys.DELETE)
            time.sleep(2)
            ele_rule.send_keys("Source CSP Tag")
            self.actionchains().send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
            self.actionchains().send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
            self.actionchains().send_keys(tag_name).send_keys(
                Keys.DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            self.actionchains().send_keys(Keys.TAB).send_keys(instance).send_keys(
                Keys.DOWN).send_keys(Keys.ENTER).send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()

        except Exception as e:
            raise Exception("Failed to choose filter source_address: %s" % e)

    def click_apply(self):
        """
        This method is to click Apply button
        """
        try:
            self.click_element(self.locator.btnApply)
            self.wait_element_visible(self.locator.btnApply, timeout=300)
        except Exception as e:
            raise Exception("Failed to click Apply button: %s" % e)

    def refresh_data(self):
        """
        This method is to click Refresh Data button
        """
        try:
            self.click_element(self.locator.btnRefreshData)
        except Exception as e:
            raise Exception("Failed to click Refresh Data button: %s" % e)

    def clear_all_filter(self):
        """
        This method is to click Clear All
        """
        try:
            # self.get_element(self.locator.btnClearAll, focus=True)
            self.click_element(self.locator.btnClearAll)
            self.wait_element_visible(self.locator.btnApply, timeout=300)
        except Exception as e:
            raise Exception("Failed to clear all: %s" % e)

    def check_dstip_existence(self):
        """
        this method is to check if destination ips traffic exists or not
        """
        try:
            destip_eles = self.get_elements(self.locator.txaDestIP)
            destip = [ele.text for ele in destip_eles if "B" not in ele.text]

            if len(destip) >= 2:
                return True
            else:
                return False
        except Exception:
            return False

    def get_source_ip(self):
        sourceip_lst = []
        try:
            time.sleep(1)
            self.wait_element_visible(self.locator.txaSourceIP, timeout=20)
            sourceip_eles = self.get_elements(self.locator.txaSourceIP)
            sourceip_lst = [ele.text for ele in sourceip_eles if "B" not in ele.text]
        except StaleElementReferenceException:
            self.log.info("stale element reference: element is not attached to the page document")
        except Exception:
            self.log.error("Failed to find source ip", exc_info=True)
        finally:
            return sourceip_lst

    def get_destination_ip(self):
        destip_lst = []
        try:
            destip_eles = self.get_elements(self.locator.txaDestIP)
            destip_lst = [ele.text for ele in destip_eles if "B" not in ele.text]
        except StaleElementReferenceException:
            self.log.info("stale element reference: element is not attached to the page document")
        except Exception:
            self.log.error("Failed to find destination ip", exc_info=True)
        finally:
            return destip_lst

    def get_traffic_data(self):
        """
        This method is to get traffic data shown in the page
        """
        self.log.info("Collecting traffic data...")
        traffic = {}
        # Source IPs
        sourceip_eles = self.get_elements(self.locator.txaSourceIP)
        sourceip = [ele.text for ele in sourceip_eles]
        traffic["Source IP (bytes"] = sourceip

        # Destination IPs
        destip_eles = self.get_elements(self.locator.txaDestIP)
        destip = [ele.text for ele in destip_eles]
        traffic["Destination IP (bytes)"] = destip

        return traffic

    def switch_format(self):
        try:
            self.click_element(self.locator.taxSwitch)
            self.wait_element_visible(self.locator.btnApply, timeout=300)
        except Exception:
            raise RuntimeError("Failed to switch format")

    def get_record_data(self):
        """
        This method is to get recrod data
        """
        records = set()
        try:
            time.sleep(3)
            self.wait_element_visible(self.locator.tblDstCell, timeout=20)
            cells = self.get_elements(self.locator.tblDstCell)
            for cell in cells:
                if cell.text:
                    records.add(cell.text)
        except StaleElementReferenceException:
            self.log.info("stale element reference: element is not attached to the page document")
        except Exception:
            self.log.error("Failed to find flows records", exc_info=True)
        finally:
            return records
