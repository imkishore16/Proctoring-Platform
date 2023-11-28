from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Specify the path to your webdriver (e.g., chromedriver)
webdriver_path = '/path/to/your/chromedriver'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get("https://skcet530.examly.io/login")

# Find the email address input box and enter the email using XPath
email_input = driver.find_element("xpath", "//*[@id=\"email\"]")  
email_input.send_keys("727721euai030@skcet.ac.in")
email_input.send_keys(Keys.RETURN)
time.sleep(5)

password_input = driver.find_element("xpath", "//*[@id='password']")  # Replace the XPath accordingly
password_input.send_keys("Error403")
password_input.send_keys(Keys.RETURN)
time.sleep(20)

hamburger = driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-header/div/div[2]/div/div/div[1]/div[1]/img")
hamburger.click()
time.sleep(3)

labs = driver.find_element(By.XPATH, "/html/body/app-root/div/app-sidebar/div[2]/ul/li[11]/a/div/div")
hamburger.click()
time.sleep(10)

IRC = driver.find_element(By.XPATH, "//*[@id='courseCardID-1']/div")
IRC.click()
time.sleep(10)

position = driver.find_element(By.XPATH, "//*[@id='teamsID']/app-accordian/div/div/div/div[1]")
position.click()
time.sleep(1)
position.click()
time.sleep(2)

position.send_keys(Keys.END)
position.send_keys(Keys.END)
position.send_keys(Keys.END)

test = driver.find_element(By.XPATH, "//*[@id='pannel037']")
test.click()

taketest = driver.find_element(By.XPATH, "//*[@id='undefinedTake Test']")
taketest.click()

agree = driver.find_element(By.XPATH, "//*[@id='tt-start-accept']")
agree.click()

# //*[@id="tt-start-accept"]

driver.quit()
