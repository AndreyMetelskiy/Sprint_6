import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrderPage:
    
    @allure.title("Оформление заказа и проверка переходов по логотипам")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment, button_type, logo_type", [
        ("Иван", "Иванов", "ул. Ленина 1", "Сокольники", "79991112233", "25.11.2024", "сутки", "black", "Жду", "top", "scooter"),
        ("Анна", "Петрова", "Пресненская наб. 10", "Лубянка", "89005554422", "26.11.2024", "двое суток", "grey", "Тест", "bottom", "yandex")
    ])
    def test_order_and_logo_navigation(self, driver, scroll_to, name, surname, address, metro, phone, date, period, color, comment, button_type, logo_type):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # 1. Оформление заказа
        if button_type == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button(scroll_to)
            
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.fill_second_form(date, period, color, comment)
        assert order_page.check_order_is_finished(), "Заказ не оформился"
        
        # 2. Проверка логотипов
        if logo_type == "scooter":
            main_page.click_scooter_logo()
            main_page.wait_for_scooter_page()
            assert main_page.SCOOTER_URL in driver.current_url
            
        elif logo_type == "yandex":
            main_page.click_yandex_logo()
            main_page.switch_to_dzen_and_wait()
            assert main_page.DZEN_URL in driver.current_url