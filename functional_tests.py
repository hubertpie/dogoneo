from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#issue with chrome version, change it later
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000')

assert 'Django' in driver.title