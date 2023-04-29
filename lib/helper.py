import time
from undetected_chromedriver import Chrome, ChromeOptions

from datetime import date
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# from robot.api.deco import keyword


# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager

from pages.login.login_page import LoginPage
from pages.profile.settings_page import SettingsPage
from pages.profile.myprofile_page import MyProfilePage
# uc.install()

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


# def get_driver_path(browser):
#     driver_path = ""
#     if browser == "chrome":
#         driver_path = ChromeDriverManager().install()
#     elif browser == "firefox":
#         driver_path = GeckoDriverManager().install()
#     else:
#         print("Incorrect Browser")
#     return driver_path


# def open_chrome_to_page(page, driver_path):

#     chrome_options = Options()
#     chrome_options.add_argument("--disable-web-security")
#     chrome_options.add_argument("--allow-running-insecure-content")
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     chrome_options.add_experimental_option('useAutomationExtension', False)
#     chrome_options.add_argument('--disable-blink-features=AutomationControlled')

#     driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
#     driver.set_window_size(720, 640)
#     driver.get(page)
#     driver.implicitly_wait(20)

#     return driver

# def open_firefox_to_page(page, driver_path):

#     # chrome_options = Options()
#     # chrome_options.add_argument("--disable-web-security")
#     # chrome_options.add_argument("--allow-running-insecure-content")
#     # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
#     # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     # chrome_options.add_experimental_option('useAutomationExtension', False)
#     # chrome_options.add_argument('--disable-blink-features=AutomationControlled')

#     driver = webdriver.Firefox(executable_path=driver_path)
#     driver.set_window_size(1920, 1080)
#     driver.get(page)
#     driver.implicitly_wait(20)

#     return driver


# def open_uc_chrome_to_page(page):
#     options = uc.ChromeOptions()
#     # options.headless = True
#     options.add_argument('--headless=new')
#     driver = uc.Chrome(options=options)
#     # driver = uc.Chrome()
#     driver.set_window_size(1920, 1080)
#     # driver.set_window_size(1080, 720)
#     driver.get(page)
#     driver.implicitly_wait(20)

#     return driver

def open_uc_chrome_to_page(page):
    options = ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-audio-output')
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--no-first-run")
    # options.add_argument("--no-service-autorun")
    # options.add_argument("--no-default-browser-check")
    # options.add_argument("--disable-popup-blocking")
    # options.add_argument("--profile-directory=Default")
    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--disable-plugins-discovery")
    # options.add_argument("--incognito")
    # options.add_argument("--start-maximized")
    # options.add_argument("--start-maximized")
    # options.add_argument('--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"')
    # options.add_argument('--headless')
    driver = Chrome(options=options)
    driver.set_window_size(1366, 768)
    # driver.set_window_size(1080, 720)
    driver.get(page)
    driver.implicitly_wait(20)

    return driver


def sign_in_with_google_oauth(driver, user, password):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.click_continue_with_google()
    login_page.input_google_username("eddiefree27@gmail.com")
    time.sleep(3)
    login_page.click_next_button()
    time.sleep(3)
    driver.save_screenshot('datadome_undetected_webddriver.png')
    login_page.input_googlepassword("Ddong6lolcarousell")
    time.sleep(3)
    login_page.click_next_button()
    time.sleep(10)
    return login_page.check_if_login_to_dashboard()


def change_birthday_date(driver, year, month, day):
    myprofile_page = MyProfilePage(driver)
    myprofile_page.click_main_page()
    bir_date = myprofile_page.get_birthday_date()
    date_list = bir_date.split("/")
    bir_year = int(date_list[2])
    bir_month = int(date_list[0])
    bir_day = int(date_list[1])
    if not (date(year, month, day) == date(bir_year, bir_month, bir_day)):
        myprofile_page.choose_birthday_date(year, month, day)
        myprofile_page.clear_highschool_graduation()
        myprofile_page.click_save()


def validate_birthday_date(driver, year, month, day):
    myprofile_page = MyProfilePage(driver)
    myprofile_page.click_main_page()
    bir_date = myprofile_page.get_birthday_date()
    date_list = bir_date.split("/")
    bir_year = int(date_list[2])
    bir_month = int(date_list[0])
    bir_day = int(date_list[1])

    return date(year, month, day) == date(bir_year, bir_month, bir_day)


def sign_out(driver):
    settings_page = SettingsPage(driver)
    settings_page.click_main_page()
    settings_page. click_tab()
    settings_page. click_logout()
    return settings_page.check_is_logout()


if __name__ == "__main__":
    # driver_path = get_driver_path("firefox")
    # driver = open_firefox_to_page("https://www.earnaha.com/", driver_path)
    driver = open_uc_chrome_to_page("https://www.earnaha.com/")

    result = sign_in_with_google_oauth(driver, "eddiefree27@gmail.com", "Ddong6lolcarousell")
    print(result)

    # change_birthday_date(driver, 2002, 11, 1)
    # rv = validate_birthday_date(driver, 2002, 11, 1)
    # print(rv)

    # result = sign_out(driver)
    # print(result)
    # time.sleep(10)

    # time.sleep(10)
