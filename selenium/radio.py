from numpy import info
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Script started")

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH,"//a[@id='gender-help']/i").click()

# info_text = driver.find_element(By.XPATH,"//div[@class='_9hzn']").text
# print(info_text)

# female_radio = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@name='sex' and @value='2']"))
# )

# driver.execute_script("arguments[0].click();", female_radio)

radios = driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radios))

for ra in radios:
    if ra.get_attribute("value") == "-1" :
        ra.click()
        break

# print("Radio button clicked")
# print("Is selected:", female_radio.is_selected())

time.sleep(5)
driver.quit()

print("Script finished")
