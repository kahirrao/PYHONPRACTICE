from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
driver.implicitly_wait(10)
page_titel = driver.title

if page_titel == "Google":
    print("Test case passed")

driver.find_element(By.ID,"APjFqb").send_keys("Selenium")
driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@value='Google Search']").click()
validation_text = driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").text
print(validation_text)
