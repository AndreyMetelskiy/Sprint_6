import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Локаторы
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text() ='Далее']")
    
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_LIST = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_COMPLETED_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")

    @allure.step("Заполнение первой формы")
    def fill_first_form(self, name, lastname, address, metro_station, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.LASTNAME_INPUT, lastname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.click_element(self.METRO_STATION_INPUT)
        # Динамический локатор для выбора метро
        metro_option = (By.XPATH, f".//div[text()='{metro_station}']")
        self.click_element(metro_option)
        self.send_keys(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Заполнение второй формы")
    def fill_second_form(self, date, period, color, comment):
        # Ввод даты
        self.send_keys(self.DATE_INPUT, date)
        # Клик по активному дню в календаре (берем только число из DD.MM.YYYY)
        day = str(int(date.split('.')[0])) 
        day_xpath = (By.XPATH, f".//div[contains(@class, 'react-datepicker__day') and not(contains(@class, '--outside-month')) and text()='{day}']")
        self.click_element(day_xpath)
        
        # Срок аренды
        self.click_element(self.RENTAL_PERIOD_LIST)
        period_xpath = (By.XPATH, f".//div[text()='{period}']")
        self.click_element(period_xpath)
        
        # Цвет
        if color == "black": self.click_element(self.COLOR_BLACK)
        else: self.click_element(self.COLOR_GREY)
        
        self.send_keys(self.COMMENT_INPUT, comment)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_YES_BUTTON)

    @allure.step("Проверка завершения заказа")
    def check_order_is_finished(self):
        return "Заказ оформлен" in self.get_text(self.ORDER_COMPLETED_HEADER)
    