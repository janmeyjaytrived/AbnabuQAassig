from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time



# Setup Chrome Driver
service =Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # Open Website
    driver.get("https://adnabu-store-assignment1.myshopify.com")

     # Enter Store Password
    password = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "form-input"))
      )
    password.send_keys("AdNabuQA"+Keys.ENTER)

    

     # Open Search
    WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "header__search"))
    ).click()

    search_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
     )
    search_box.send_keys("SnowBoard"+Keys.ENTER)

    first_product = wait.until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-grid > ul > li:nth-child(1) > div > div"))
    )
    product_name = first_product.text
    first_product.click()

    wait.until(
       EC.element_to_be_clickable((By.NAME, "add"))
    ).click()

    cart_popup = wait.until(
        EC.visibility_of_element_located((By.ID, "CartDrawer-Form"))
    )
    assert cart_popup.is_displayed()

    print(f"SUCCESS: {product_name} added to cart")

except Exception as e:
   print("TEST FAILED:", e)

finally:
   driver.quit()
