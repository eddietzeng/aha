from selenium.webdriver.common.by import By


class LoginLocator():
    """
    Locators related to login are defined here
    """
    btnLogin = (By.XPATH, "//a[@href='https://app.earnaha.com/api/auth/login']")
    btnContGoogle = (By.XPATH, "//span[text()='Continue with Google']")
    txaGoogleAccount = (By.XPATH, "//div[text()='Eddie Tzeng']")

    txaGoogleUsername = (By.NAME, "identifier")
    # txaGooglePassword = (By.NAME, "password")
    txaGooglePassword = (By.XPATH, "//input[@name='password' or @name='Passwd']")

    btnNext = (By.XPATH, "//span[text()='Next' or text()='繼續' or text()='下一步']")

    btnMyProfile = (By.XPATH, "//a[@href='/sat/profile/account']")

    # btnKeepFree = (By.XPATH, "//div[text()='Skip, Keep Free Trial']")
    btnKeepFree = (By.XPATH, "//*[@id='__next']/div[1]/div/div[1]/button/svg")
    btnSkip = (By.XPATH, "//button[text()='Skip']")
