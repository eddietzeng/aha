from selenium.webdriver.common.by import By


class NetworkingLocator():
    """
    Locators related to Topology page are defined here
    """
    btnTopology = (By.XPATH, "//a[@data-testid='/topology']")

    tabNetworkGraph = (By.XPATH, "//a[@data-testid='fsnavtab-Network']")
    tabNetwork = (By.XPATH, "//a[@data-testid='fsnavtab-Network']")
    tabTransit = (By.XPATH, "//a[@data-testid='fsnavtab-Transit']")
    tabMcna = (By.XPATH, "//a[@data-testid='fsnavtab-MCNA']")
    tabLatencyMonitor = (By.XPATH, "//span[text()='Latency Monitor']")
    tabTopologyReplay = (By.XPATH, "//span[text()='Topology Replay']")

    btnRefreshGraph = (
        By.XPATH, "//div[@style='overflow: hidden; max-height: 85vh;']/div[1]/div[1]/button[1]")

    imgCanvas = (By.CSS_SELECTOR, "canvas")
    imgIcon = (By.CSS_SELECTOR, "div[class='vis-tooltip']")

    btnReload = (By.XPATH, "//div[@class='MuiAlert-message']/button[1]")

    txaTruncate = (By.XPATH, "//span[text()='Truncate Node Labels']")

    btnNetworking = (
        By.XPATH,
        "//*[name()='svg' and @data-testid='AccountTreeOutlinedIcon']/ancestor::div[@role='button']"
    )
