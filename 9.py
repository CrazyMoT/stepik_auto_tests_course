from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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