import time
from selenium.webdriver.common.keys import Keys
from .airspace_page import AirSpacePage


class TopologyPage(AirSpacePage):
    """
    Networking -> Topology
    This is Topology Page class which inherits from Networking
    Topology implementations are defined here
    """

    def click_tab_network(self):
        """
        This method is to click Network tab
        """
        try:
            self.click_element(self.locator.tabNetwork)
        except RuntimeError as e:
            raise Exception("Failed to click Network tab: %s" % e)

    def switch_to_new_topo(self):
        """
        This method is to switch to new topo page
        """
        try:
            element = self.get_element(self.locator.btnSwitch)
            self.execute_script("arguments[0].click();", element)
            if self.is_element_present(self.locator.btnClose):
                self.click_element(self.locator.btnClose)
        except RuntimeError as e:
            raise Exception("Failed to switch to new topo: %s" % e)

    def click_tab_transit(self):
        """
        This method is to click Transit tab
        """
        try:
            self.click_element(self.locator.tabTransit)
        except RuntimeError as e:
            raise Exception("Failed to click Transit tab: %s" % e)

    def click_tab_mcna(self):
        """
        This method is to click MCNA tab
        """
        try:
            self.click_element(self.locator.tabMcna)
        except RuntimeError as e:
            raise Exception("Failed to click MCNA tab: %s" % e)

    def refresh_topology(self):
        """
        This mehtod is to refresh Topology graph
        """
        try:
            self.click_element(self.locator.btnRefreshGraph)
        except RuntimeError as e:
            raise Exception("Failed to click refresh graph button: %s" % e)

    def reload_if_needed(self):
        """
        This method is to reload topology if not displayed
        """
        start_time = time.time()
        while time.time() - start_time < int(60):
            # Return if the img is visible
            if self.is_element_visible(self.locator.imgCanvas):
                return
            # Click reload button to refresh
            self.driver.refresh()
            # elif self.is_element_visible(self.locator.btnReload):
            #     self.click_element(self.locator.btnReload)
            time.sleep(10)
        raise RuntimeError("Failed to reload topology")

    def click_truncate_node_labels(self):
        """
        This method is to click Truncate Node Labels
        """
        try:
            self.click_element(self.locator.txaTruncate)
        except RuntimeError as e:
            raise Exception("Failed to click Truncate Node Labels: %s" % e)

    def click_add_condtion_button(self):
        """
        This method is to click Condition button
        """
        try:
            self.click_element(self.locator.btnAddCondition)
        except RuntimeError as e:
            raise Exception("Failed to click Condtion button: %s" % e)

    def input_filter_key(self, filter_key, tag_name):
        """
        This method is to input filter key
        @param filter_key: Filter key
        """
        try:
            self.input_text(self.locator.txaFilterKey, filter_key)
            self.actionchains().send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
            self.actionchains().send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(
                Keys.TAB).send_keys(tag_name).send_keys(Keys.ENTER).perform()
        except RuntimeError as e:
            raise Exception("Failed to input filter key: %s" % e)
