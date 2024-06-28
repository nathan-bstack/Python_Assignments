from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://bstackdemo.com/")
    wait = WebDriverWait(driver, 10)
    
    sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "signin")))
    sign_in_button.click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#username input')))
    username = driver.find_element(By.CSS_SELECTOR, "#username input")
    username.send_keys("demouser\n")
    #Entering the password
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password input')))
    password = driver.find_element(By.CSS_SELECTOR, "#password input")
    password.send_keys("testingisfun99\n")
    #Clicking on Login
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
    driver.find_element(By.ID, "login-btn").click()
    
    
    iphone12_add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/div[4]")))
    iphone12_add_to_cart_button.click()
    time.sleep(3)
    checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[3]/div[3]")))
    checkout_button.click()
    
    firstname_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/ol/li/div/div/div[2]/form/fieldset/div/fieldset/div/div/div[1]/div/input")))
    firstname_input.send_keys("Nathan")
    lastname_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/ol/li/div/div/div[2]/form/fieldset/div/fieldset/div/div/div[2]/div/input")
    lastname_input.send_keys("Joe")
    address_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/ol/li/div/div/div[2]/form/fieldset/div/fieldset/div/div/div[3]/div/input")
    address_input.send_keys("test")
    state_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/ol/li/div/div/div[2]/form/fieldset/div/fieldset/div/div/div[4]/div/input")
    state_input.send_keys("t")
    zip_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/ol/li/div/div/div[2]/form/fieldset/div/fieldset/div/div/div[5]/div/input")
    zip_input.send_keys("40000")
    submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/ol/li/div/div/div[2]/form/div/button")
    submit_button.click()
    
    # success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your Order has been successfully placed.')]")))
    # assert success_message.is_displayed()
    # print("Order successfully placed.")

finally:
    driver.quit()