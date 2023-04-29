from .topology_page import TopologyPage


class LatencyMonitorPage(TopologyPage):
    """
    Topology -> LatencyMonitor
    This is LatencyMonitor Page class which inherits from TopologyPage
    LatencyMonitor implementations are defined here
    """

    def click_tab(self):
        """
        This method is to click Latency Monitor tab
        """
        try:
            self.click_element(self.locator.tabLatencyMonitor)
        except RuntimeError as e:
            raise Exception("Failed to click Latency Monitor tab: %s" % e)
