import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1440, 900) 
    driver.get("https://qa-scooter.praktikum-services.ru/")
    # Пытаемся закрыть куки, если они есть
    try:
        cookie_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        cookie_button.click()
    except:
        # Если кнопки нет или она не успела прогрузиться — не страшно
        pass
    yield driver
    driver.quit()
    
@pytest.fixture
def scroll_to(driver):
    def _scroll(element):
        # block: "center" поможет избежать перекрытия краями экрана
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    return _scroll