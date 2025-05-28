from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tempfile
import time

BASE_URL = "http://ec2-3-83-86-27.compute-1.amazonaws.com/index.php"

def test_form_submission():
    options = Options()

    # Create a unique temporary directory for Chrome user data
    user_data_dir = tempfile.mkdtemp(prefix="chrome-user-data-")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Optional: run headless if Jenkins is headless environment
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)

    time.sleep(2)

    input_box = driver.find_element(By.NAME, "username")
    input_box.send_keys("Alice")

    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    time.sleep(2)

    greeting = driver.find_element(By.TAG_NAME, "h3")
    print("Greeting found:", repr(greeting.text))

    assert greeting.text == "Hello, Alice!", "Greeting did not match expected text!"

    driver.quit()

if __name__ == "__main__":
    test_form_submission()
