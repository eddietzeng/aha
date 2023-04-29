from selenium.webdriver.common.by import By


class MonitorLocator():
    """
    Locators related to FlowIQ page are defined here
    """
    btnFlowIQ = (By.XPATH, "//a[@data-testid='/netflow']")

    tabOverview = (By.XPATH, "//a[@data-testid='fsnavtab-Overview']")
    tabTrends = (By.XPATH, "//span[text()='Trends']")
    tabGeolocation = (By.XPATH, "//span[text()='Geolocation']")
    tabFlows = (By.XPATH, "//span[text()='Flows']")
    tabRecords = (By.XPATH, "//a[@data-testid='fsnavtab-Records']")

    tabLasthour = (By.XPATH, "//span[text()='Last hour']")
    tabLastday = (By.XPATH, "//span[text()='Last day']")
    tabLastweek = (By.XPATH, "//span[text()='Last week']")
    tabLastmonth = (By.XPATH, "//span[text()='Last month']")

    btnAddrule = (By.XPATH, "//label[text()='Filters']/following-sibling::button")
    cboFilter = (By.XPATH, "//div[@role='combobox']")
    txaSelectfield = (By.XPATH, "//input[@placeholder='Select a metric']")
    txaCondition = (By.XPATH, "//input[@autocomplete='list' and @value='']")
    btnAppyChanges = (By.XPATH, "//span[text()='Apply Changes']")
    btnClear = (
        By.XPATH,
        "//*[name()='svg' and @data-testid='DeleteOutlinedIcon']"
    )
    btnGear = (By.ID, "resolveHostnamePopover")
    chkResolveHostname = (By.XPATH, "//span[text()='Resolve Hostnames']")
    chkInput = (By.CSS_SELECTOR, "input")

    dgdTables = (By.XPATH, "//div[@id='dash-container']/div[2]/div")
    btnApply = (By.XPATH, "//span[text()='Apply']")
    btnRefreshData = (By.XPATH, "//button[text()='Refresh Data']")

    tblDstCell = (
        By.XPATH, "//div[@data-field='netflow.dst_addr' and @role='cell']/div[1]/div")

    tblFlows = (By.XPATH, "//div[@id='dash-container']/div[2]/descendant::div")

    txaSourceIP = (
        By.XPATH,
        "//div[@data-testid='data-container-test']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/descendant::label"
    )

    txaDestIP = (
        By.XPATH,
        "//div[@data-testid='data-container-test']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/descendant::label"
    )

    txaMonitor = (
        By.XPATH,
        "//*[name()='svg' and @data-testid='MonitorHeartOutlinedIcon']/ancestor::div[@role='button']"
    )

    taxSwitch = (By.XPATH, "//span[contains(@class, 'MuiSwitch-switchBase')]")
