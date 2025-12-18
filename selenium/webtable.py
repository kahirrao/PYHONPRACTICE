from errno import ECANCELED
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("https://money.rediff.com/gainers")

driver.maximize_window()

allCompanies = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr/td[1]/a")
print(len(allCompanies))

allPrices = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr/td[4]")
print(len(allPrices))

expected = "TV Vision"

# for i in range(len(allCompanies)):
#     if allCompanies[i].text.lower() == expected.lower():
#         print(allCompanies[i].text + " ==== " + allPrices[i].text)
#         allCompanies[i].click()
#         break



for company, price in zip(allCompanies, allPrices):
    if company.text.strip().lower() == expected.lower():
        print(f"{company.text} ==== {price.text}")
        company.click()
        break

time.sleep(5)
driver.quit()