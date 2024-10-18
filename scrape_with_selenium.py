from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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

# ACCEPT COOKIES
btn_accept_cookies = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    )
btn_accept_cookies.click()


# Get the HTML content source
time.sleep(10)
html_content = driver.page_source


# Parse html_content with BeautifulSoup4
soup = BeautifulSoup(html_content, 'html.parser')


# Get the hyperlinks of the first 10 elements
href_list = []
for i in range(1, 10):
    product_id = 'i' + str(i)
    li_elm = soup.find('li', id=product_id)

    if li_elm:
        a_elm = li_elm.find('a')
        if a_elm and 'href' in a_elm.attrs:
            href_list.append(a_elm['href'])


print(href_list)


time.sleep(60)
driver.quit()