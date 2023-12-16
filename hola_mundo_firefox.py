

from selenium import webdriver
url = 'https://www.selenium.dev/'
# Se crea la variable url
# Para no tener un dato harcodeado para cuando apliquemos page object model

driver = webdriver.Firefox()
driver.get(url)
print(driver.title)
driver.quit()
