import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
    
    # Локаторы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text() ='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_LIST = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    COMMENTS_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    MIDDLE_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Да']")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    @allure.step("Заполнение первой формы")
    def fill_first_form(self, name, lastname, address, metro_station, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(lastname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.METRO_STATION_INPUT).send_keys(metro_station)
        
        # Клик по выпавшему списку метро
        metro_option = (By.XPATH, f"//div[text()='{metro_station}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(metro_option)).click() 
        
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step("Заполнение второй формы")
    def fill_second_form(self, date, period, color, comment):
        # Дата
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DATE_INPUT)).send_keys(date, Keys.ENTER)
        # Срок
        self.driver.find_element(*self.RENTAL_PERIOD_LIST).click()
        rental_option = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(rental_option)).click()
        # Цвет (динамический ID: black или grey)
        self.driver.find_element(By.ID, color).click()
        # Комментарий
        self.driver.find_element(*self.COMMENTS_INPUT).send_keys(comment) 
        # Финальные кнопки
        self.driver.find_element(*self.MIDDLE_ORDER_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.YES_BUTTON)).click()

    @allure.step("Проверка модалки")
    def check_order_is_finished(self):
        modal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MODAL_WINDOW))
        return "Заказ оформлен" in modal.text