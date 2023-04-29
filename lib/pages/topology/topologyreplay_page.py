from .topology_page import TopologyPage


class TopologyReplayPage(TopologyPage):
    """
    Topology -> TopologyReplay
    This is TopologyReplay Page class which inherits from TopologyPage
    TopologyReplay implementations are defined here
    """

    def click_tab(self):
        """
        This method is to click Topology Replay tab
        """
        try:
            self.click_element(self.locator.tabTopologyReplay)
        except RuntimeError as e:
            raise Exception("Failed to click Topology Replay tab: %s" % e)
