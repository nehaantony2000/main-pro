from selenium import webdriver
import time
# Open the browser and maximize the window
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# Navigate to the login page
driver.get("http://127.0.0.1:8000/Account/login/")
# Enter email and password for login
driver.find_element("id", "email").send_keys("nehaantonyk@gmail.com")
time.sleep(3)
driver.find_element("id", "password").send_keys("Neha@1219")
time.sleep(3)

# Click on the login button
driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/input[2]").click()
time.sleep(3)
print("User Logged In")
print("Test Case Passed Successfully")

# Navigate to the change password page
driver.get("http://127.0.0.1:8000/Account/Change_Password/")

# Enter the current password, new password, and confirm password
driver.find_element("id", "currentpassword").send_keys("Neha@1219")
driver.find_element("id", "newpassword").send_keys("Neha@2000")
driver.find_element("id", "confirmpassword").send_keys("Neha@2000")

# Click on the change password button
driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div[2]/div/div/form/div[4]/input").click()

# Verify if the password was successfully changed
if "Account/login" in driver.current_url:
    print("Password Changed Successfully")
    print("Test Case Passed Successfully")
else:
    print("Failed to Change Password")
    print("Test Case Failed")

# Close the browser
driver.quit()
