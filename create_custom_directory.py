from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create an instance of ChromeOptions
options = Options()

# Specify the user data directory
options.add_argument("user-data-dir=D:\\path\to\\your\\directory")

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=options)
