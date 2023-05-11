from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("Search test case started")

# Set up WebDriver options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the login page
driver.get("http://127.0.0.1:8000/Account/login/")
print("Login page opened")

# Enter login credentials
driver.find_element("id", "email").send_keys("nehaantonyk@gmail.com")
time.sleep(3)
driver.find_element("id", "password").send_keys("Neha@2000")
time.sleep(3)

# Submit the login form
driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/input[2]").click()
print("User logged in")

# Wait for the user home page to load
time.sleep(3)

# Perform search after login
search_input = driver.find_element("id", "query")
search_input.clear()
search_input.send_keys("IBM")
search_input.send_keys(Keys.ENTER)
print("Search performed after login")

# Wait for the search results to load
time.sleep(3)

# Validate search results

# TODO: Add your validation code here to assert/search for the expected results on the page

print("Test Case Passed Successfully")

# Close the browser
driver.quit()
