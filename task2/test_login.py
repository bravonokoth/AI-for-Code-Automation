# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Test cases
test_cases = [
    {"username": "tomsmith", "password": "SuperSecretPassword!", "expected": "success"},
    {"username": "invalid_user", "password": "wrong_pass", "expected": "failure"}
]

# Results
results = []

try:
    # Navigate to login page
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Wait for username field to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    
    for test in test_cases:
        # Enter credentials
        username_field = driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys(test["username"])
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(test["password"])
        driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        
        # Wait for response
        time.sleep(5)
        # Save screenshot for each test
        driver.save_screenshot(f"screenshot_{test['username']}.png")
        
        # Check result
        if "secure" in driver.current_url:  # Success redirects to /secure
            result = "success" if test["expected"] == "success" else "failure"
        else:  # Failure shows error message
            result = "success" if test["expected"] == "failure" else "failure"
        
        results.append({"test": test, "result": result})
        
finally:
    driver.quit()

# Print results
for res in results:
    print(f"Test: {res['test']['username']}, Expected: {res['test']['expected']}, Result: {res['result']}")

# Calculate success rate
success_rate = sum(1 for res in results if res['result'] == "success") / len(results) * 100
print(f"Success Rate: {success_rate}%")