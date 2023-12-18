import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from actions import ActionPage
from env import Env
from utils import get_table_device_list

geckodriver_path = "/usr/local/bin/geckodriver"
os.environ['PATH'] = f"{os.environ['PATH']}:{geckodriver_path}"

if __name__ == "__main__":
    
    options = Options()
    
    if not Env.DEBUG_BROWSER:
        options.add_argument("--headless")
    
    driver = webdriver.Firefox(options=options)
    driver.get(Env.URL)
    
    
    ap = ActionPage()

    ap.login(driver)
    device_list = ap.get_list_users(driver)
    
    driver.quit()
    
    get_table_device_list(device_list)
    