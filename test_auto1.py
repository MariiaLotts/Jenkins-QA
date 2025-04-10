from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# def test_locked_out_user():
#     driver = webdriver.Chrome()
def test_success_log_in():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    time.sleep(3)

    driver.find_element(By.XPATH,"//*[@id='login-button']").click()
    driver.get(url="https://www.saucedemo.com/inventory.html")

    time.sleep(3)

    driver.quit()
