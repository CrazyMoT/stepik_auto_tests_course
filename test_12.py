import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir=C:\\Users\\Crazy_MoT\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link1', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_1(browser, link1):
    link = f"https://stepik.org/lesson/{link1}/step/1/"
    browser.get(link)
    try:
        bot1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav/a[2]")))
        bot1.click()
        in1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/input[1]")))
        in1.send_keys(log)
        in2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/input[2]")))
        in2.send_keys(pss)
        bot2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/button")))
        bot2.click()
    except:
        pass
    input1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    input1.send_keys(str(math.log(int(time.time()))))
    button1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[4]/button")))
    button1.click()
    output1 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "smart-hints__hint"))).text
    if output1 != "Correct!":
        print(output1)
