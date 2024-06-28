from selenium import webdriver
from percy import percy_snapshot

resolutions = [
    (375, 667),
    (480, 800),
    (720, 1280),
    (1280, 800),
    (1440, 900),
    (1920, 1080)
]

browsers = ['firefox', 'edge']

endpoints = [
    "/",
    "/pricing",
    "/integrations/automate",
    "/docs"
]

base_urls = [
    "https://www.browserstack.com",
    "https://k8s.bsstag.com"
]

def run_tests(driver, base_url, endpoints):
    for endpoint in endpoints:
        url = base_url + endpoint
        driver.get(url)
        for width, height in resolutions:
            driver.set_window_size(width, height)
            percy_snapshot(driver, name=f'{endpoint}_{width}x{height}')

for browser in browsers:
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    for base_url in base_urls:
        run_tests(driver, base_url, endpoints)

    driver.quit()
