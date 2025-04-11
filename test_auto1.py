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

def test_locked_out_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # find username field and input data
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")

    time.sleep(2)

    # find password field and input data
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    time.sleep(2)

    # click on button
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text == "Epic sadface: Sorry, this user has been locked out."

    driver.quit()

def test_empty_fields():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # find username field and input data
    driver.find_element(By.ID, "user-name").send_keys(" ")

    # find password field and input data
    driver.find_element(By.ID, "password").send_keys(" ")

    # click on button
    driver.find_element(By.ID, "login-button").click()

    assert driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    driver.quit()