from calendar import month
import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Kalpesh")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Ahirrao")

male_radio = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='sex' and @value='2']"))
)

driver.execute_script("arguments[0].click();", male_radio)

day_selection = driver.find_elements(
    By.XPATH, "//select[@name='birthday_day']/option"
)
for day in day_selection:
    if day.get_attribute("value") == "12" :
        day.click()
        break

print(day.is_displayed())


month_selection = driver.find_element(By.XPATH,"//select[@name='birthday_month']")
month_selection = Select(month_selection)

month_selection.select_by_visible_text("Feb")
print("Selected month:", month_selection.first_selected_option.text)
time.sleep(2)
month_selection.select_by_index(11)
print("Selected month:", month_selection.first_selected_option.text)
driver.find_element(By.XPATH,"//input[@name='reg_email__']").send_keys("9594037701")
time.sleep(10)