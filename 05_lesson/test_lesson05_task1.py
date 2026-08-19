from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # https://httpbin.qa-territory.online/forms/post

    driver.quit()
