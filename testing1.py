import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to your ChromeDriver
chrome_service = Service("/home/shtlp_0041/Downloads/chromedriver-linux64/chromedriver")

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--start-maximized")  # Start browser maximized

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# # Your code here
driver.get("https://www.shorthills.ai")
driver.save_screenshot("screenshot.png")
# # Add a delay to keep the browser open
time.sleep(10)  # Keep the browser open for 10 seconds
driver.quit()   # Close the browser