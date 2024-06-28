import os,time
from Appium_sdk.sdk_appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL") 

options = UiAutomator2Options().load_capabilities({
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",
    "app" : "bs://b938fc17506786ad2ba97b08f541e2d76378cbf3",
    'bstack:options' : {
        "projectName" : "Andriod App Automate project",
        "buildName" : "browserstack-build-12",
        "sessionName" : "BStack app_auto_test",
        "userName" : BROWSERSTACK_USERNAME,
        "accessKey" : BROWSERSTACK_ACCESS_KEY,
    }
})

driver = webdriver.Remote("https://hub-cloud.browserstack.com:443/wd/hub", options=options)

# options = UiAutomator2Options().set_capability('sessionName', 'BStack Sample Test')
# driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
el1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.FrameLayout\").instance(5)")
el1.click()
time.sleep(1)
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="filter-btn")
el2.click()
time.sleep(1)
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Samsung\")")
el3.click()
time.sleep(1)
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"High to Low\")")
el4.click()
time.sleep(1)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(546, 1926)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(557, 1666)
actions.w3c_actions.pointer_action.release()
actions.perform()

el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="add-to-cart-12")
el5.click()
time.sleep(1)

el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"\")")
el6.click()
time.sleep(1)
el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="checkout-btn")
el7.click()
time.sleep(1)
el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="username-input")
el8.click()
time.sleep(1)
el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"demouser\")")
el9.click()
time.sleep(1)
el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="password-input")
el10.click()
time.sleep(1)
el11 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"testingisfun99\")")
el11.click()
time.sleep(1)
el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="login-btn")
el12.click()
time.sleep(1)
el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="firstNameInput")
el13.click()
time.sleep(1)
el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="firstNameInput")
el14.click()
time.sleep(1)
el14.send_keys("Nathan")
time.sleep(1)
el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="lastNameInput")
el15.click()
time.sleep(1)
el15.send_keys("Joe")
time.sleep(1)
el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="addressInput")
el16.click()
time.sleep(1)
el16.send_keys("Test")
time.sleep(1)
el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="stateInput")
el17.click()
time.sleep(1)
el17.send_keys("Test")
time.sleep(1)
el18 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.LinearLayout\").instance(0)")
el18.click()
time.sleep(1)
el19 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="postalCodeInput")
time.sleep(1)
el19.send_keys("222")
time.sleep(1)
el20 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="submit-btn")
el20.click()
time.sleep(1)
driver.quit()
