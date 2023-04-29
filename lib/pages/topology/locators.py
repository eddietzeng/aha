from selenium.webdriver.common.by import By


class TopologyLocator():
    """
    Locators related to Topology page are defined here
    """
    btnTopology = (By.XPATH, "//a[@href='/topology']")

    tabNetworkGraph = (By.XPATH, "//span[text()='Network Graph']")
    tabNetwork = (By.XPATH, "//span[text()='Network']")
    tabTransit = (By.XPATH, "//span[text()='Transit']")
    tabMcna = (By.XPATH, "//span[text()='MCNA']")
    tabLatencyMonitor = (By.XPATH, "//span[text()='Latency Monitor']")
    tabTopologyReplay = (By.XPATH, "//span[text()='Topology Replay']")

    btnRefreshGraph = (
        By.XPATH, "//div[@style='overflow: hidden; max-height: 85vh;']/div[1]/div[1]/button[1]")

    imgCanvas = (By.CSS_SELECTOR, "canvas")
    imgIcon = (By.CSS_SELECTOR, "div[class='vis-tooltip']")

    btnReload = (By.XPATH, "//div[@class='MuiAlert-message']/button[1]")

    txaTruncate = (By.XPATH, "//span[text()='Truncate Node Labels']")
