# This is a sample Python script.

from selenium import webdriver
driver = webdriver.Chrome("/Users/omesh.bhat/PycharmProjects/pythonProject/Drivers/chromedriver")

driver.get("https://www.google.com/")

driver.maximize_window()

driver.close()



