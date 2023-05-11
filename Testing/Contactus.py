from selenium import webdriver
import time

print("Contact Page Test Case Started")

# Set up WebDriver options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the contact page
driver.get("http://127.0.0.1:8000/contact/")
print("Contact page opened")

# Enter name, email, and message
name_input = driver.find_element("id", "name")
name_input.clear()
name_input.send_keys("John Doe")

email_input = driver.find_element("id", "email")
email_input.clear()
email_input.send_keys("johndoe@example.com")

message_input = driver.find_element("id", "comment")
message_input.clear()
message_input.send_keys("This is a test message.")

# Submit the contact form
submit_button = driver.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/section/form/input[2]")
submit_button.click()
print("Contact form submitted")

# Wait for form submission response
time.sleep(3)

print("Contact Page Tested Successfully")

# Close the browser
driver.quit()
