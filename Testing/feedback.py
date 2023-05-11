from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

print("Course Feedback test case started")

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

# Navigate to the feedback page
driver.get("http://127.0.0.1:8000/Course/feedback/")
print("Feedback page opened")

# Select the course "How to Get a Job at Amazon"
course_select = driver.find_element("name", "course")
select = Select(course_select)
select.select_by_value("1")
print("Course selected: How to Get a Job at Amazon")

# Enter name and email
name_input = driver.find_element("name", "name")
name_input.clear()
name_input.send_keys("Neha Antony")

email_input = driver.find_element("name", "email")
email_input.clear()
email_input.send_keys("nehaantonyk@gmail.com")

# Enter feedback
feedback_input = driver.find_element("name", "feedback")
feedback_input.clear()
feedback_input.send_keys("This course is amazing!")

# Submit the feedback
submit_button = driver.find_element("xpath", "/html/body/div/div[2]/div/div/div[2]/div/div/form/input[2]")
submit_button.click()
print("Feedback submitted")

print("Test Case Passed Successfully")

# Close the browser
driver.quit()
