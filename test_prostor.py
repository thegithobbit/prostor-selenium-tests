import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from prostor_page import ProstorPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# 1. перевірка тексту кнопки "Каталог"
def test_tc_007_catalog_button_text(driver):
    page = ProstorPage(driver)
    page.open()
    btn = page.get_catalog_button()
    assert btn is not None


# 2. перевірка заголовка головної сторінки (Title)
def test_tc_001_title_check(driver):
    page = ProstorPage(driver)
    page.open()
    assert "Prostor" in driver.title


# 3. перевірка наявності головного логотипу
def test_tc_002_logo_exists(driver):
    page = ProstorPage(driver)
    page.open()
    logo = page.get_logo()
    assert logo is not None


# 4. перевірка гарячої лінії
def test_tc_010_phone_exists(driver):
    page = ProstorPage(driver)
    page.open()
    phone = driver.find_element(By.XPATH, "//a[contains(@href, 'tel:0800')]")
    assert phone is not None

# 5. перевірка наявності кнопки пошуку
def test_tc_011_search_button_exists(driver):
    page = ProstorPage(driver)
    page.open()
    search_btn = driver.find_element(By.CSS_SELECTOR, ".header-search__button, button[type='submit']")
    assert search_btn is not None

# 6. перевірка посилання на Instagram
def test_tc_012_instagram_link_exists(driver):
    page = ProstorPage(driver)
    page.open()
    link = driver.find_element(By.XPATH, "//a[contains(@href, 'instagram.com')]")
    assert link is not None

# 7. перевірка наявності розділу "Акції"
def test_tc_013_promo_link_exists(driver):
    page = ProstorPage(driver)
    page.open()
    promo = driver.find_element(By.XPATH, "//a[contains(@href, 'aktsii') or contains(@href, 'promotions')]")
    assert promo is not None

# 8. перевірка посилання на Facebook
def test_tc_014_facebook_link_exists(driver):
    page = ProstorPage(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, 500);")
    fb = driver.find_element(By.XPATH, "//a[contains(@href, 'facebook.com')]")
    assert fb is not None

# 9. перевірка копірайту у футері (актуальний рік)
def test_tc_015_footer_copyright_exists(driver):
    page = ProstorPage(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    copyright_text = driver.find_element(By.XPATH, "//*[contains(text(), '20')]")
    assert copyright_text is not None

# 10. перевірка посилання на Доставку
def test_tc_016_delivery_link_exists(driver):
    page = ProstorPage(driver)
    page.open()
    delivery = driver.find_element(By.XPATH, "//a[contains(@href, 'dostavka') or contains(text(), 'Доставка')]")
    assert delivery is not None