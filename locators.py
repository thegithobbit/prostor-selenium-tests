from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOG_BTN = (By.XPATH, "//*[contains(text(), 'Каталог')]")
    SEARCH_INPUT = (By.NAME, "q")
    LOGO = (By.XPATH, "//a[contains(@class, 'logo')] | //a[@href='/uk/']")
    CLOSE_BANNER = (By.CSS_SELECTOR, ".popup-close")
    PHONE_NUMBER = (By.XPATH, "//a[contains(@href, 'tel:0800')]")
    SEARCH_ICON = (By.CSS_SELECTOR, ".search-icon, .header-search__button, button[type='submit']")
    INSTAGRAM_LINK = (By.XPATH, "//a[contains(@href, 'instagram.com')]")
    PROMO_SECTION = (By.XPATH, "//a[contains(@text, 'Акції') or contains(@href, 'aktsii')]")
    FACEBOOK_LINK = (By.XPATH, "//a[contains(@href, 'facebook.com')]")
    DELIVERY_LINK = (By.XPATH, "//a[contains(@href, 'dostavka') or contains(text(), 'Доставка')]")
    FOOTER_COPYRIGHT = (By.XPATH,
                        "//*[contains(text(), '2024') or contains(text(), '2025') or contains(text(), '2026')]")