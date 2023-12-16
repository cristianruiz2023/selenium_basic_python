

from selenium import webdriver

# descargamos el driver especifico
# Reemplaza 'ruta/del/chromedriver' con la ubicación real de tu archivo chromedriver.exe
# ruta_del_chromedriver = '/dev/net/drivers_selenium/chromedriver.exe'

# Configura la ruta del controlador al inicializar el objeto webdriver.Chrome()
# driver = webdriver.Chrome(executable_path=ruta_del_chromedriver)


driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/')
print(driver.title)
driver.quit()
