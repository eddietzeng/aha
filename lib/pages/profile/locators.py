from selenium.webdriver.common.by import By


class ProfileLocator():
    """
    Locators related to Settings page are defined here
    """
    btnMyProfile = (By.XPATH, "//a[@href='/sat/profile/account']")
    btnSettings = (By.XPATH, "//a[@href='/sat/profile/settings']")
    btnMyProfile = (By.XPATH, "//a[@href='/sat/profile/account']")
    btnLogOut = (By.XPATH, "//button[text()='LOG OUT']")
    btnYes = (By.XPATH, "//button[text()='Yes']")
    txaLoginToPractice = (By.XPATH, "//h2[text()='Login to practice']")
    txaBirthday = (By.XPATH, "//input[@name='birthday']")
    btnPickyear = (By.XPATH, "//button[@title='Pick year']")
    txtYearMonth = (By.XPATH, "//button[@title='Pick year']/p[1]")
    btnNextMonth = (By.XPATH, "//button[@title='Next month']")
    btnPrevMonth = (By.XPATH, "//button[@title='Previous month']")
    btnOK = (By.XPATH, "//button[text()='OK']")
    txtSave = (By.XPATH, "//div[text()='Save']")
    txaGraduation = (By.XPATH, "//input[@name='highSchoolGraduation']")
    txaHighSchool = (By.XPATH, "//input[@name='highSchool']")

    @staticmethod
    def btnYear(year):
        loc = f"//button[@data-year='{year}']"
        return (By.XPATH, loc)

    @staticmethod
    def btnDay(day):
        loc = f"//button[text()='{day}']"
        return (By.XPATH, loc)
