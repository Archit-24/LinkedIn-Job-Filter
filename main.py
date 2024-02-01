from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get()







