# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# ---------------------------------------------------------------------------------------------------------
# GLOBAL VARIABLES
product_links = []
service = Service(executable_path="C:/Users/elif-/Downloads/chromedriver-win64/chromedriver.exe")
url_results = "https://www.hepsiburada.com/ara?q=diz%C3%BCst%C3%BC+bilgisayar"

# ---------------------------------------------------------------------------------------------------------
# SETUP CHROME DRIVER
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs) # Disable all notifications
chrome_options.add_argument("--disable-extensions")  # Disable all extensions
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get(url_results)
li_elms = []

html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")
    
# i0 - i499
for i in range(500):
    li_id = "i" + str(i)
    li = soup.find("li", id=li_id)
    if li:
        li_elms.append(li)

print(len(li_elms))

driver.quit()