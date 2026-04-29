import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class ProstorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://prostor.ua/uk/")
        time.sleep(3)
        self._close_popups()

    def _close_popups(self):
        try:
            close_buttons = self.driver.find_elements(*MainPageLocators.CLOSE_BANNER)
            for btn in close_buttons:
                if btn.is_displayed():
                    btn.click()
        except:
            pass

    def search_for(self, text):
        self._close_popups()
        search_field = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SEARCH_INPUT))
        search_field.send_keys(text + Keys.ENTER)

    def get_logo(self):
        return self.wait.until(EC.presence_of_element_located(MainPageLocators.LOGO))

    def get_cart_element(self):
        return self.wait.until(EC.presence_of_element_located(MainPageLocators.CART_ICON))

    def get_catalog_button(self):
        return self.wait.until(EC.presence_of_element_located(MainPageLocators.CATALOG_BTN))