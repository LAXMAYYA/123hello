from selenium import webdriver

# Create an instance of the Firefox WebDriver
driver = webdriver.Firefox()

# Load the atg.world website
driver.get("https://atg.world/")

# Check if the website has loaded properly
assert "ATG World" in driver.title

# Close the browser instance
driver.quit()
