# Import various components to be used later
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException


#********************* Navigate Websites *********************#

# Open firefox browser.
driver = webdriver.Firefox()

# Navigate to desired URL
driver.get("http://www.duckcode.me/")

# Click a button based on the text it has
button = driver.find_element_by_xpath("//*[contains(text(), 'All Posts')]")
button.click()

# Wait for at least 10 seconds for the element with this class name to appear before moving on.
class_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'category_blog_div')))
class_button.click()

# You can also find elements by id. See the docs for all the different options.
id_button = driver.find_element_by_id("duck_logo")
id_button.click()

#************************ Submit Forms ***********************#

# Navigate to desired URL
driver.get("https://twitter.com")

# Prompt for login info
username = input('Enter username:')
password = input('Enter password:')

# Grab inputs
username_input = driver.find_element_by_name("session[username_or_email]")
password_input = driver.find_element_by_name("session[password]")

# Enter values
username_input.clear()
username_input.send_keys(username)

password_input.clear()
password_input.send_keys(password)

# Submit form
username_input.submit() 
