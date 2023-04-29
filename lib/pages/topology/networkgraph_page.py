import time
from .topology_page import TopologyPage


class NetworkGraphPage(TopologyPage):
    """
    Topology -> NetworkGraph
    This is NetworkGraph Page class which inherits from TopologyPage
    NetworkGraph implementations are defined here
    """

    def click_tab(self):
        """
        This method is to click Network Graph tab
        """
        try:
            self.click_element(self.locator.tabNetworkGraph)
        except RuntimeError as e:
            raise Exception("Failed to click Network Graph tab: %s" % e)

    def click_tab_network(self):
        """
        This method is to click Network tab
        """
        try:
            self.click_element(self.locator.tabNetwork)
        except RuntimeError as e:
            raise Exception("Failed to click Network tab: %s" % e)

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
        while time.time() - start_time < int(90):
            # Return if the img is visible
            if self.is_element_visible(self.locator.imgCanvas):
                return
            # Click reload button to refresh
            elif self.is_element_visible(self.locator.btnReload):
                self.click_element(self.locator.btnReload)
            time.sleep(5)
        raise RuntimeError("Failed to reload topology")

    def click_truncate_node_labels(self):
        """
        This method is to click Truncate Node Labels
        """
        try:
            self.click_element(self.locator.txaTruncate)
        except RuntimeError as e:
            raise Exception("Failed to click Truncate Node Labels: %s" % e)
