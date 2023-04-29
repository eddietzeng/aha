from selenium.webdriver.common.by import By


class TroubleshootLocator():
    """
    Locators related to Troubleshoot pages are defined here
    """
    btnAppIQ = (By.XPATH, "//a[@data-testid='/appiq']")
    txaSrc = (By.XPATH, "//input[@name='srcInstance']")

    txaDest = (By.XPATH, "//input[@name='dstInstance']")
    btnSubmit = (By.XPATH, "//button[text()='Run AppIQ']")

    imgCanvas = (By.CSS_SELECTOR, "canvas")
    txtResult = (By.CSS_SELECTOR, "h5")

    btnClose = (By.XPATH, "//img[@alt='avx logo']/following-sibling::div/button[1]")

    txaProtocol = (By.ID, "demo-simple-select-outlined")
    txaIcmp = (By.XPATH, "//li[@data-value='icmp']")
    txaTcp = (By.XPATH, "//li[@data-value='tcp']")
    txaUdp = (By.XPATH, "//li[@data-value='udp']")

    btnTroubleshoot = (
        By.XPATH,
        "//*[name()='svg' and @data-testid='InsightsOutlinedIcon']/ancestor::div[@role='button']"
    )

    btnMessageBoxClose = (By.XPATH, "//button[text()='Close']")
    txaPort = (By.XPATH, "//input[@name='port']")