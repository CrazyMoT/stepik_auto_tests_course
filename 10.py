from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element(By.CSS_SELECTOR, "#book")
    button1.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

finally:
    confirm = browser.switch_to.alert
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()