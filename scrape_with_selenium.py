from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="C:/Users/elif-/Downloads/chromedriver-win64/chromedriver.exe")

# SETUP CHROME DRIVER
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs) # Disable all notifications
chrome_options.add_argument("--disable-extensions")  # Disable all extensions
""""
To prevent:
* Created TensorFlow Lite XNNPACK delegate for CPU.
* Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#58 is a dynamic-sized tensor).
Which appears when trying to access a dynamically rendered HTML elements
"""
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer

driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.hepsiburada.com/ara?q=diz%C3%BCst%C3%BC+bilgisayar"
driver.get(url) 
hyperlinks = []

# ACCEPT COOKIES
btn_accept_cookies = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    )
btn_accept_cookies.click()

# RESULTS LIST: doesn't work
results = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, '1'))
)
print(results)

# CLICK LOAD MORE: doesn't work
btn_load_more = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(By.XPATH, '//*[@id="ProductList_7e0b1457-b9cf-4e4d-08d1-aebeca49a1e3"]/div/div/div/div/div[1]/button')
)
btn_load_more.click()


time.sleep(60)
driver.quit()