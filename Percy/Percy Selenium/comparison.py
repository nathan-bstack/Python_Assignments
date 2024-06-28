from selenium import webdriver
from percy import percy_snapshot

driver = webdriver.Chrome()
# driver.get('https://bstackdemo.com/')
driver.get('https://k8s.bsstag.com/ ')
driver.implicitly_wait(10)
percy_snapshot(driver, '1st')