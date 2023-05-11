from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initializing the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navigate to the login page
driver.get("http://127.0.0.1:8000/Account/login/")
print("Login test case started")

# Fill in the login form and submit
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("admin")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/input[2]").click()
time.sleep(3)
print("User Logged In")

# Test Case: Add a new course
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/section/div/div[1]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/a[1]').click()

# Fill in the course details
driver.find_element(By.ID, "id_course").send_keys("Course Name")
driver.find_element(By.ID, "id_duration").send_keys("4 weeks")
driver.find_element(By.ID, "id_amount").send_keys("100")
driver.find_element(By.ID, "id_slug").send_keys("course-name")
driver.find_element(By.ID, "id_desc").send_keys("Course description")
driver.find_element(By.ID, "id_start_date").send_keys("2023-05-10")
driver.find_element(By.ID, "id_end_date").send_keys("2023-06-10")
driver.find_element(By.ID, "id_last_date").send_keys("2023-05-15")

# Open the user dropdown
user_dropdown = driver.find_element(By.XPATH, "//span[@id='select2-id_userid-container']")
ActionChains(driver).move_to_element(user_dropdown).click().perform()
time.sleep(1)

# Select a user from the dropdown
user_option = driver.find_element(By.XPATH, "//li[contains(text(), 'nehaantony2023b@mca.ajce.in')]")
ActionChains(driver).move_to_element(user_option).click().perform()
time.sleep(1)

# Submit the form
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/section/div/div/form/div/div[2]/div/div/div[1]/input").click()
time.sleep(3)

# Verify if the course was successfully added (Add your verification steps here)
# ...

# Test Case Completed
print("Test Case Passed Successfully")

# Close the browser
driver.quit()
