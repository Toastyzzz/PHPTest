from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace with your actual EC2 public IP or hostname
BASE_URL = "http://ec2-3-83-86-27.compute-1.amazonaws.com:8080/index.php"

def test_homepage_heading():
    # Setup Chrome WebDriver (make sure chromedriver is installed and in PATH)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless (no UI)
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(BASE_URL)
        time.sleep(2)  # wait for page load

        # Find heading element by tag name
        heading = driver.find_element(By.TAG_NAME, "h1")

        assert "Hello, World!" in heading.text, "Heading text did not match!"

        print("Test Passed: Heading contains 'Hello, World!'")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_homepage_heading()
