from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip



driver = webdriver.Chrome(executable_path="C:\\Users\\Fahid\\Downloads\\chromedriver\\chromedriver.exe")

driver.maximize_window()



driver.get("https://www.foodpanda.com.bd/login/new")


email="bappa9673@gmail.com"
first_name="Al Amin "
last_name= "Siddique"
password="bappaandarica"



driver.find_element(By.XPATH,"//*[@id='login-page-react-root']/main/div/div/div[4]/button").send_keys(Keys.ENTER)


email_xpath = '//*[@id="email"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH,email_xpath))
)
time.sleep(1)

pyperclip.copy(email)

search_box.send_keys(Keys.CONTROL + "v")

time.sleep(1)


driver.find_element(By.XPATH,"//*[@id='login-page-react-root']/main/div/form/div[3]/button").send_keys(Keys.ENTER)


pass_xpath = '//*[@id="_password"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH,pass_xpath))
)
time.sleep(1)

pyperclip.copy(password)

search_box.send_keys(Keys.CONTROL + "v")

time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='login-page-react-root']/main/div/form/div[4]/button").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/div").click()
driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/div/div/div/ul/li[3]/a").click()

















