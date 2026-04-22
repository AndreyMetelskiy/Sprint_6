from selenium.webdriver.common.by import By

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    TOP_ORDER_BUTTON = (By.XPATH,"//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH,"//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH,"//img[@alt='Yandex']")
    
    
    def __init__(self, driver):
        self.driver = driver 
        
    def click_top_order_button(self):
        self.driver.find_element(*self.TOP_ORDER_BUTTON).click()
        
    
    