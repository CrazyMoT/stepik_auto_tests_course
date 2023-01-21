from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)


    xy = browser.find_element(By.CSS_SELECTOR, "#num1")
    yy = browser.find_element(By.CSS_SELECTOR, "#num2")
    x = xy.text
    y = yy.text
    z = int(x) + int(y)
    print(z)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(z))  # ищем элемент с текстом, который задали


    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
