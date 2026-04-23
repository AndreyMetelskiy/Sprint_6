import pytest
import allure
from pages.main_page import MainPage

@allure.feature("Главная страница")
@allure.story("Раздел 'Вопросы о важном'")
class TestMainPage:
    
    @allure.title("Проверка текста ответов в выпадающем списке")
    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_0, MainPage.DROPDOWN_BUTTON_0_TEXT, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_1, MainPage.DROPDOWN_BUTTON_1_TEXT, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_2, MainPage.DROPDOWN_BUTTON_2_TEXT, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_3, MainPage.DROPDOWN_BUTTON_3_TEXT, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_4, MainPage.DROPDOWN_BUTTON_4_TEXT, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_5, MainPage.DROPDOWN_BUTTON_5_TEXT, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_6, MainPage.DROPDOWN_BUTTON_6_TEXT, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (MainPage.DROPDOWN_LIST_ELEMENT_BUTTON_7, MainPage.DROPDOWN_BUTTON_7_TEXT, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
        ]
    )
    def test_check_faq_answers(self, driver, question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)
        result_text = main_page.get_answer_text(question_locator, answer_locator)
        assert result_text == expected_text