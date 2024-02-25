from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
from time import sleep
import os

from dotenv import load_dotenv

# .env file contains api keys in the format of API_KEY="xxxxxx", get it using os.environ['API_KEY']; before that pip install python-dotenv
load_dotenv()  # take environment variables from .env.


my_email = "yuvalco1@gmail.com"
my_password = os.environ['LD_PASS']


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.linkedin.com/jobs/search/?currentJobId=3814556261&geoId=101620260&keywords=director&location=Israel&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

driver.get(url)

sign_in_btn = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_btn.click()


# sign in page

email_input = driver.find_element(By.ID,"username")
email_input.send_keys(my_email)


email_input = driver.find_element(By.ID,"password")
email_input.send_keys(my_password)

sleep(2)

sign_in_btn2 = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
print(sign_in_btn2.text)
sign_in_btn2.click()

# find 1st easy apply

sleep(2)
easy_apply_btn = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
print(easy_apply_btn.text)
easy_apply_btn.click()

# fill the form
sleep(1)
next_btn = driver.find_element(By.CSS_SELECTOR,".display-flex button")
next_btn.click()

sleep(1)
nd_next = driver.find_elements(By.CSS_SELECTOR,".display-flex button span")
for i in nd_next:
    if i.text == "Next":
        i.click()


