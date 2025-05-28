import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

BASE_URL = "http://ec2-3-83-86-27.compute-1.amazonaws.com/index.php"

@pytest.mark.parametrize("username", ["Alice", "Bob"])
def test_form_submission(username):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)

    time.sleep(2)

    input_box = driver.find_element(By.NAME, "username")
    input_box.send_keys(username)

    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    time.sleep(2)

    greeting = driver.find_element(By.TAG_NAME, "h3")
    print(f"Greeting found for {username}: {repr(greeting.text)}")

    assert greeting.text == f"Hello, {username}!", f"Greeting did not match expected text for {username}!"

    driver.quit()
