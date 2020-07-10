from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


with open('config.txt', 'r') as f:
    nickname = f.readline() 
    passwd = f.readline() 

path_to_webdriver = 'chromedriver.exe'
driver = webdriver.Chrome(path_to_webdriver)
driver.get("https://uchebnik.mos.ru/catalogue")
assert "Библиотека" in driver.title
elem = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/div[1]/div/button/span[2]/div/div/span')
elem.click()
name = driver.find_element_by_id("login-field")
name.send_keys(nickname)
password = driver.find_element_by_id("password-field")
password.send_keys(passwd, Keys.RETURN)
try:
    my_materials = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/a[1]'))
    )
finally:
    my_materials.click()
scen = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/div[1]/div/div/div[3]/div/div[1]')
scen.click()
try:
    lesson = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div[1]/div[2]/div/div[4]/div[1]/div/a/div/div[1]/div[1]/span'))
    )
except Exception as e:
    print(e.args[0])
else:
    lesson.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
driver.close()
