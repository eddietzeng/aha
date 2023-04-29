from selenium.webdriver.common.by import By


class ProgramIntentLocator():
    """
    Locators related to ThreatIQ page are defined here
    """
    btnThreatIQ = (By.XPATH, "//a[@data-testid='fsnavtab-ThreatIQ']")
    btnSecurity = (By.XPATH, "//span[text()='Security']")

    dlgError = (By.CLASS_NAME, "MuiSnackbarContent-message")

    btnApply = (By.XPATH, "//span[text()='Apply']")

    txtTableValue = (By.XPATH, "./following-sibling::h2[1]")

    txtUniqueThreatIP = (
        By.XPATH, "//p[text()='Unique Threat IPs']/following-sibling::h2[1]")
    txtThreatCount = (
        By.XPATH, "//p[text()='Threat Count']/following-sibling::h2[1]")
    txtAllThreats = (
        By.XPATH, "//p[text()='All Threats (Total)']/following-sibling::h2[1]")

    dgdRows = (By.CSS_SELECTOR, "div[class*='MuiDataGrid-virtualScrollerRenderZone']>*")
    dgdRowCounts = (By.XPATH, "//*[contains(@class, 'MuiDataGrid-root')]")

    @staticmethod
    def threats_row_locators(num):
        rows_loc = {}
        src_addr_loc = f"div[data-rowindex='{num}'] [data-field='src_addr']"
        dst_addr_loc = f"div[data-rowindex='{num}'] [data-field='dst_addr']"
        host_loc = f"div[data-rowindex='{num}'] [data-field='host']"
        view_button_loc = f"div[data-rowindex='{num}'] [data-field=' '] button"

        rows_loc["src_addr"] = (By.CSS_SELECTOR, src_addr_loc)
        rows_loc["dst_addr"] = (By.CSS_SELECTOR, dst_addr_loc)
        rows_loc["host"] = (By.CSS_SELECTOR, host_loc)
        rows_loc["view_button"] = (By.CSS_SELECTOR, view_button_loc)
        return rows_loc

    # Threat Details
    tabTopology = (By.XPATH, "//span[text()='Topology']/parent::button")

    tabFlowdata = (By.XPATH, "//span[text()='Flow Data']/parent::button")
    tabGeneral = (By.XPATH, "//span[text()='general']/parent::button")
    tabGeoipdst = (By.XPATH, "//span[text()='geoip_dst']/parent::button")
    tabGeoipsrc = (By.XPATH, "//span[text()='geoip_src']/parent::button")
    tabNetflow = (By.XPATH, "//span[text()='netflow']/parent::button")

    tabSummary = (By.XPATH, "//span[text()='Threat Summary']/parent::button")

    btnProgramIntent = (
        By.XPATH,
        "//*[name()='svg' and @data-testid='DynamicFormOutlinedIcon']/ancestor::div[@role='button']"
    )
