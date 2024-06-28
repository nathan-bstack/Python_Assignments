import re
from playwright.sync_api import Page

def test_example(page: Page) -> None:
    page.goto("https://bstackdemo.com/")
    page.get_by_role("link", name="Sign In").click()
    page.locator("div").filter(has_text=re.compile(r"^Select Username$")).nth(2).click()
    page.get_by_text("demouser", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Select Password$")).nth(2).click()
    page.get_by_text("testingisfun99", exact=True).click()
    page.get_by_role("button", name="Log In").click()
    page.locator("[id=\"\\31 \"]").get_by_text("Add to cart").click()
    page.get_by_text("Checkout").click()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill("Nathan")
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill("Joe")
    page.get_by_label("Address").click()
    page.get_by_label("Address").fill("test")
    page.get_by_label("State/Province").click()
    page.get_by_label("State/Province").fill("test")
    page.get_by_label("Postal Code").click()
    page.get_by_label("Postal Code").fill("test")
    page.get_by_role("button", name="Submit").click()
    confirmation_message = page.inner_text('#confirmation-message')
    assert confirmation_message == "Your Order has been successfully placed."
    try:
        assert confirmation_message == "Your Order has been successfully placed."
        page.evaluate("_ => {}", 'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully Verified!"}}');
    except Exception as err:
        page.evaluate("_ => {}", 'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Test Failed!"}}');
        raise Exception
    page.close()