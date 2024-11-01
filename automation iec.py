from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Define variables
url = "https://dgft.gov.in/CP/?opt=view-any-iec"
iec_code = "YOUR_IEC_CODE_HERE"
name_chars = "YOUR_NAME_CHARS_HERE"
security_code = "YOUR_SECURITY_CODE_HERE"

# Initialize the browser
driver = webdriver.Chrome()  # Ensure Chrome WebDriver is in PATH
driver.get(url)

# Step-by-step automation
try:
    # Click on "View any IEC"
    view_iec_button = driver.find_element(By.XPATH, '//*[contains(text(), "view any iec")]')
    view_iec_button.click()


    time.sleep(2)

    # Enter the IEC code
    iec_code_field = driver.find_element(By.ID, 'iec')
    iec_code_field.send_keys(iec_code)

    # Enter the 3 characters of the name
    name_chars_field = driver.find_element(By.ID, 'name_chars')  # Update ID if different
    name_chars_field.send_keys(name_chars)


    security_code_field = driver.find_element(By.ID, 'security_code')
    security_code_field.send_keys(security_code)

    # Click on the "View IEC" button
    submit_button = driver.find_element(By.ID, 'submit_button')  # Update ID if different
    submit_button.click()

    # Wait for the page to load results
    time.sleep(3)  # Adjust if necessary

    # Fetch and print all the text from the result page
    result_text = driver.find_element(By.TAG_NAME, 'body').text  # Captures all text on the page
    print(result_text)

finally:
    # Close the browser
    driver.quit()
