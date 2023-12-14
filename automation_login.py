import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By

def login(url, user_class, pass_class, btn_class, time, username, password):
    driver = webdriver.Firefox()
    driver.get(url)
    t.sleep(time)
    driver.find_element(By.ID, user_class).send_keys(username)
    t.sleep(time)
    driver.find_element(By.ID, pass_class).send_keys(password)
    t.sleep(time)
    driver.find_element(By.ID, btn_class).click()

login("https://www.example.com", "userid-or-name", "passid-or-name", "btnid-or-name", 1, "username", "password")
