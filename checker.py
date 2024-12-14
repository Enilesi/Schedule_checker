from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url1="https://docs.google.com/spreadsheets/d/e/2PACX-1vRXLWDLpnv-108LNY1vMSst-yvrWKqGlytCjlt2Qauid7gv7x2MLzKsO0fPWJ9Cfxj3AfevBvc9gGC0/pubhtml#"
url2="https://docs.google.com/spreadsheets/d/e/2PACX-1vQEyqy8X0hPQ4LL5yf3NRS0vrw-KMOS0c5E0onO-BU3lakCuANqvd3jWH_l_x8xtNUeiEq9VOjWU4Kv/pubhtml"


driver=webdriver.Chrome()
driver.get(url1)
navigate=driver.find_element(by=By.ID,value="sheet-menu")
list_of_tables=navigate.find_elements(By.TAG_NAME,"li")

for table in list_of_tables:
    table.click()
    sleep(3)

