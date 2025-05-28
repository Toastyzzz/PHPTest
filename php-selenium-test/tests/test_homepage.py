from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace with your actual EC2 public IP or hostname
BASE_URL = "http://ec2-3-83-86-27.compute-1.amazonaws.com/index.php"

def test_homepage_heading():
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH or specify path
    driver.get(BASE_URL)

    time.sleep(2)  # wait for page load, better to use explicit waits in real tests

    heading = driver.find_element(By.TAG_NAME, "h1")
    print("Heading text found:", repr(heading.text))

    expected_text = "Hello, World!\nThis is a simple web app for testing."
    assert heading.text == expected_text, "Heading text did not match!"

    driver.quit()

if __name__ == "__main__":
    test_homepage_heading()