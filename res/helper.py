import time
import undetected_chromedriver as uc

from selenium.webdriver.chrome.options import Options

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from pages.login.login_page import LoginPage
from pages.profile.settings_page import SettingsPage
uc.install()

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


def get_driver_path(browser):
    driver_path = ""
    if browser == "chrome":
        driver_path = ChromeDriverManager().install()
    elif browser == "firefox":
        driver_path = GeckoDriverManager().install()
    else:
        print("Incorrect Browser")
    return driver_path


def open_chrome_to_page(page, driver_path):
    from selenium import webdriver
    chrome_options = Options()
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get(page)
    driver.implicitly_wait(20)

    return driver


def open_uc_chrome_to_page(page):
    from selenium import webdriver
    driver = webdriver.Chrome()

    driver.set_window_size(1920, 1080)
    driver.get(page)
    driver.implicitly_wait(20)

    return driver


def sign_in_with_google_oauth(driver, user, password):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.click_continue_with_google()
    login_page.input_google_username("eddiefree27@gmail.com")
    login_page.click_next_button()
    login_page.input_googlepassword("Ddong6lolcarousell")
    login_page.click_next_button()
    time.sleep(20)
    return (login_page.check_if_login_to_dashboard())


# if __name__ == "__main__":
#     driver_path = get_driver_path("chrome")
#     driver = open_uc_chrome_to_page("https://www.earnaha.com/")

#     settings_page = SettingsPage(driver)
#     settings_page.click_main_page()
#     settings_page. click_tab()
#     settings_page. click_logout()
#     print(settings_page.check_is_logout())
#     time.sleep(10)
