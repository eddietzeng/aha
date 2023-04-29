from selenium.webdriver.common.by import By


class AdministrationLocator():
    """
    Locators related to Administration page are defined here
    """
    btnAdmin = (
        By.XPATH,
        "//*[name()='svg' and @data-testid='PeopleOutlinedIcon']/ancestor::div[@role='button']"
    )

    btnReports = (By.XPATH, "//a[@data-testid='/reports']")
    btnAudit = (By.XPATH, "//a[@data-testid='/audit']")
