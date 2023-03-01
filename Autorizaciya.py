# а это типа дев ветка понял да?
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "https://youdo.com/"
driver.get(url)

Log_in = driver.find_element(By.XPATH, '//*[@id="ToolbarR"]/div[2]/div[3]/div/span/a[1]')
Log_in.click()

username_input = driver.find_element(By.XPATH, '//*[@id="ModalsPortal"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/div[1]/div/div/input')
username_input.clear()
username_input.send_keys("88005553535")

username_input.send_keys(Keys.ENTER)

while(True):
    pass
# понял
