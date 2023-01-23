from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link = "http://suninjuly.github.io/registration2.html"


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CLASS_NAME, "form-control first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "form-control second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control third")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "form-control first")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "/html/body/div/form/button")
        button.click()
        #self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "/html/body/div/form/button")
        button.click()
        #self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

# не забываем оставить пустую строку в конце файла
