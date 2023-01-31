from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def test_guest_should_see_login_link(browser, language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

