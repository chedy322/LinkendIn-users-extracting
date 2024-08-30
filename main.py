from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

load_dotenv()
driver = webdriver.Chrome()  

# List to store user data
users = []
query = 'profile'

def login():
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)
    # Find the email and password fields and enter the credentials
    email = driver.find_element(By.ID, "username")
    email.send_keys(os.getenv('EMAIL'))
    time.sleep(2)
    password = driver.find_element(By.ID, "password")
    password.send_keys(os.getenv('MDP'))
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
    time.sleep(10)

def scrape_profiles():
    login() 
    i = 1
    while i <= 3:
        url = f'https://www.linkedin.com/search/results/people/?keywords={query}&origin=CLUSTER_EXPANSION&page={i}&sid=6%3A1'
        
        # Load the search results page with Selenium
        driver.get(url)
        time.sleep(5)
        # Parse the rendered HTML with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        for user in soup.find_all('div', {'class': 'gBWcDgvhUNYGLdvJbecWdUgMMwZzjVjRbLutgfLc'}):  # Replace this class with the correct one
            print(user)
            users.append(user.get_text(strip=True))
        
        i += 1
        time.sleep(2)

scrape_profiles()
print(users)

driver.quit()  # Close the browser when done
