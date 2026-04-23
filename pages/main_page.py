from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class MainPage(BasePage):
    
    TOP_ORDER_BUTTON = (By.XPATH,"//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH,"//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
        
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
    

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(self.BOTTOM_ORDER_BUTTON)
        self.click_element(self.BOTTOM_ORDER_BUTTON)
        
    def click_order_button(self, button_type):
        if button_type == "top":
            self.click_top_order_button()
        else:
            self.click_bottom_order_button()
        
            
    @allure.step("Клик по вопросу и получение ответа")
    def get_answer_text(self, question_locator, answer_locator):
        self.scroll_to_element(question_locator)
        self.click_element(question_locator) 
        return self.get_text(answer_locator)
