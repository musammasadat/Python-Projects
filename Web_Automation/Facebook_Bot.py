from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Facebook:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
        
    def login(self):
        bot = self.bot
        bot.get("https://www.facebook.com/")
        
        try:
           
            WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email = bot.find_element(By.ID, "email")
            email.clear()
            email.send_keys(self.username)
            
            password = bot.find_element(By.ID, "pass")
            password.clear()
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            
          
            WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Account']"))
            )
            print("Login successful")
        except Exception as e:
            print(f"An error occurred during login: {e}")
        
    def post_status(self, status_text):
        try:
            bot = self.bot
           
            WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@name='xhpc_message']"))
            )
            status_box = bot.find_element(By.XPATH, "//textarea[@name='xhpc_message']")
            status_box.click()
            status_box.send_keys(status_text)
            status_box.send_keys(Keys.RETURN)
            print("Status posted successfully!")
        except Exception as e:
            print(f"Error posting status: {e}")
            
    def logout(self):
        try:
            bot = self.bot
           
            WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Account']"))
            )
            account_menu = bot.find_element(By.CSS_SELECTOR, "div[aria-label='Account']")
            account_menu.click()
            
            
            WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Log Out')]"))
            )
            logout_button = bot.find_element(By.XPATH, "//span[contains(text(),'Log Out')]")
            logout_button.click()
            print("Logged out successfully!")
        except Exception as e:
            print(f"Error logging out: {e}")
        

load = Facebook('enter_email', 'enter_password')
load.login()
time.sleep(5) 
load.post_status("Hello, this is an automated post!")
time.sleep(5)  
load.logout()
