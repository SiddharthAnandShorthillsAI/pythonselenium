from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Function to check responsiveness
def check_responsiveness(driver, resolutions):
    for width, height in resolutions:
        # Resize the browser window
        driver.set_window_size(width, height)
        time.sleep(2)  # Allow the page to adjust to the new size

        # Take a screenshot for each resolution
        screenshot_name = f"screenshot_{width}x{height}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved for resolution {width}x{height}: {screenshot_name}")

        # Check if the username field is displayed
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # Print the visibility status of key elements
        print(f"Username field visible: {username_field.is_displayed()}")
        print(f"Password field visible: {password_field.is_displayed()}")
        print(f"Login button visible: {login_button.is_displayed()}\n")

# List of browsers to test
browsers = {
    "Chrome": webdriver.Chrome,
    "Firefox": webdriver.Firefox,
    "Edge": webdriver.Edge
}

# Define resolutions to check
resolutions = [
    (1366, 768),   # HD
    (1280, 800),   # WXGA
    (768, 1024),   # Tablet Portrait
    (360, 640),    # Mobile
    (1920, 1080),  # Full HD
]

# Loop through each browser
for browser_name, Browser in browsers.items():
    print(f"\nTesting with {browser_name}...")
    
    # Initialize the WebDriver for the specific browser
    driver = Browser()  # Ensure you have the corresponding WebDriver executable in your PATH

    # Open the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)  # Wait for the page to load

    # Take an initial screenshot of the login page
    driver.save_screenshot(f"screenshot_initial_{browser_name}.png")

    # Check responsiveness at defined resolutions
    check_responsiveness(driver, resolutions)

    # Locate the username field and enter the username
    driver.find_element(By.NAME, "username").send_keys("Admin")

    # Locate the password field and enter the password
    driver.find_element(By.NAME, "password").send_keys("admin123")

    # Click the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for the page to load after login
    time.sleep(5)

    # Verify the title of the page
    act_title = driver.title
    exp_title = "OrangeHRM"

    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login Test Failed")
    user_dropdown = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
    user_dropdown.click()

    # Wait for the dropdown options to be visible
    time.sleep(2)

    # Click the logout link
    # Use XPath to locate the logout link and click it
    logout_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='oxd-userdropdown-link' and contains(text(),'Logout')]"))
    )
    logout_link.click()

    # Wait for the logout page to load
    WebDriverWait(driver, 10).until(EC.title_is("OrangeHRM"))  # Adjust the expected title as necessary

    # Print out the title after logout
    print("Logged out. Current page title:", driver.title)
    # Wait before logging out
    time.sleep(5)

    # Close the browser
    driver.close()
