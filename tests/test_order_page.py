import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.base_page import BasePage

class TestOrderPage:
    
    @allure.title("Оформление заказа и проверка переходов по логотипам")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment, button_type, logo_type", [
        ("Иван", "Иванов", "ул. Ленина 1", "Сокольники", "79991112233", "25.11.2024", "сутки", "black", "Жду", "top", "scooter"),
        ("Анна", "Петрова", "Пресненская наб. 10", "Лубянка", "89005554422", "26.11.2024", "двое суток", "grey", "Тест", "bottom", "yandex")
    ])
    def test_order_and_logo_navigation(self, driver, name, surname, address, metro, phone, date, period, color, comment, button_type, logo_type):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        
        # 1. Выбор кнопки заказа
        main_page.click_order_button(button_type)    
        # 2. Заполнение форм 
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.fill_second_form(date, period, color, comment)
        # 3. Проверка подтверждения
        assert order_page.check_order_is_finished(), "Сообщение об успешном заказе не появилось"
        # 4. Проверка логотипов
        assert base_page.click_logo_and_check_navigation(logo_type), f"Переход по лого {logo_type} не удался"