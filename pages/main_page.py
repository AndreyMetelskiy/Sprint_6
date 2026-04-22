from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage:
    
    def __init__(self, driver):
        self.driver = driver 
        
    TOP_ORDER_BUTTON = (By.XPATH,"//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH,"//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    SCOOTER_LOGO = (By.XPATH,"//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH,"//img[@alt='Yandex']")
    
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "https://dzen.ru/?yredirect=true"
    
    

    DROPDOWN_LIST_ELEMENT_BUTTON_0 = (By.XPATH,"//div[@id = 'accordion__heading-0']")
    DROPDOWN_LIST_ELEMENT_BUTTON_1 = (By.XPATH,"//div[@id = 'accordion__heading-1']")
    DROPDOWN_LIST_ELEMENT_BUTTON_2 = (By.XPATH,"//div[@id = 'accordion__heading-2']")
    DROPDOWN_LIST_ELEMENT_BUTTON_3 = (By.XPATH,"//div[@id = 'accordion__heading-3']")
    DROPDOWN_LIST_ELEMENT_BUTTON_4 = (By.XPATH,"//div[@id = 'accordion__heading-4']")
    DROPDOWN_LIST_ELEMENT_BUTTON_5 = (By.XPATH,"//div[@id = 'accordion__heading-5']")
    DROPDOWN_LIST_ELEMENT_BUTTON_6 = (By.XPATH,"//div[@id = 'accordion__heading-6']")
    DROPDOWN_LIST_ELEMENT_BUTTON_7 = (By.XPATH,"//div[@id = 'accordion__heading-7']")
    
    DROPDOWN_BUTTON_0_TEXT = (By.ID, "accordion__panel-0")
    DROPDOWN_BUTTON_1_TEXT = (By.ID, "accordion__panel-1")
    DROPDOWN_BUTTON_2_TEXT = (By.ID, "accordion__panel-2")
    DROPDOWN_BUTTON_3_TEXT = (By.ID, "accordion__panel-3")
    DROPDOWN_BUTTON_4_TEXT = (By.ID, "accordion__panel-4")
    DROPDOWN_BUTTON_5_TEXT = (By.ID, "accordion__panel-5")
    DROPDOWN_BUTTON_6_TEXT = (By.ID, "accordion__panel-6")
    DROPDOWN_BUTTON_7_TEXT = (By.ID, "accordion__panel-7")
    
    
    @allure.step("Клик по кнопке вопроса и получение текста ответа")  
    def check_text_button(self, scroll_to, button, text):
        # 1. поиск элемента 
        target_button = self.driver.find_element(*button)
        # 2. Скролл
        scroll_to(target_button)
        # 3. Клик
        self.driver.execute_script("arguments[0].click();", target_button)
        # 4. текст ответа 
        answer = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(text)
        )
        return answer.text
    
    @allure.step("Клик по кнопке заказать сверху") 
    def click_top_order_button(self):
        self.driver.find_element(*self.TOP_ORDER_BUTTON).click()
        
    @allure.step("Клик по кнопке заказать снизу") 
    def click_bottom_order_button(self, scroll_to):
        # Находим кнопку 
        button = self.driver.find_element(*self.BOTTOM_ORDER_BUTTON)
        # Скроллим до неё
        scroll_to(button)
        button.click()
        
    @allure.step("Переключиться на новую вкладку и дождаться URL")
    def wait_for_new_window_and_url(self, expected_url_part):
        # Ждем открытия второго окна
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # Переключаемся на новую вкладку
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        # Ждем редиректа
        WebDriverWait(self.driver, 10).until(lambda d: expected_url_part in d.current_url)
        return self.driver.current_url
    
    @allure.step("Нажать на логотип «Самокат»")
    def click_scooter_logo(self):
        logo = self.driver.find_element(*self.SCOOTER_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)

    @allure.step("Дождаться перехода на главную страницу «Самоката»")
    def wait_for_scooter_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.url_contains(self.SCOOTER_URL)
        )

    @allure.step("Нажать на логотип «Яндекс»")
    def click_yandex_logo(self):
        # Сохраняем текущие окна, чтобы потом найти новую вкладку
        self.original_handles = self.driver.window_handles 
        logo = self.driver.find_element(*self.YANDEX_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)

    @allure.step("Переключиться на новую вкладку и дождаться загрузки Дзена")
    def switch_to_dzen_and_wait(self):
        # Ожидаем появление второго окна
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(len(self.original_handles) + 1)
        )
        # Находим ID новой вкладки (которой не было в списке до клика)
        new_window = [w for w in self.driver.window_handles if w not in self.original_handles][0]
        # Переключаем фокус драйвера на новую вкладку
        self.driver.switch_to.window(new_window)
        
        # Ждем появления dzen.ru в URL
        return WebDriverWait(self.driver, 15).until(
            EC.url_contains(self.DZEN_URL)
        )