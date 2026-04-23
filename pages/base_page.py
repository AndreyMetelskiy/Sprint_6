from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "https://dzen.ru/?yredirect=true"
    
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), 
        )

    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
        )
        element.click()

    def click_via_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.send_keys(text)

    def get_text(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_window(self, expected_url_part, time=15):
        WebDriverWait(self.driver, time).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, time).until(EC.url_contains(expected_url_part))
        
    @allure.step("Нажать на логотип Самоката и дождаться перехода")
    def click_scooter_logo(self):
        # Используем click_via_js, чтобы избежать ElementClickInterceptedException
        self.click_via_js(self.SCOOTER_LOGO)
        return WebDriverWait(self.driver, 10).until(EC.url_contains(self.SCOOTER_URL))

    @allure.step("Нажать на логотип Яндекса и перейти в Дзен")
    def click_yandex_logo_and_switch(self):
        self.click_via_js(self.YANDEX_LOGO)
        self.switch_to_new_window(self.DZEN_URL)
        return True
    
    def click_logo_and_check_navigation(self, logo_type):
        if logo_type == "scooter":
            return self.click_scooter_logo() 
        elif logo_type == "yandex":
            return self.click_yandex_logo_and_switch()