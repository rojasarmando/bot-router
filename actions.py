import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tags import Tags
from env import Env
from typing import Type
from wifi import enable_wifi, disable_wifi

class ActionPage:
    
    def __init__(self) -> None:
        
        if not Env.CONTAINER:
            disable_wifi()
            time.sleep(1)
            enable_wifi()
    
    @staticmethod
    def login(driver: Type[webdriver.Firefox]):
        
        time.sleep(1)
        field_password = driver.find_element(By.ID , Tags.ID_PASSWORD_LOGIN)
        field_password.send_keys(Env.PASSWORD_TPLINK)
        
        button_ok = driver.find_element(By.ID, Tags.ID_BTN_LOGIN)
        button_ok.click()
        
    def get_list_users(self, driver: Type[webdriver.Firefox]):
        
        time.sleep(1)
        device_list = []
       
        self.get_list_data(driver , device_list)
        btn_guest = driver.find_element(By.ID , Tags.BTN_GUEST)
        btn_guest.click()
        
        time.sleep(1)
        self.get_list_data(driver , device_list , is_invited=True)
        return device_list
        
    
    def get_list_data(self , driver , device_list , is_invited=False):
        
        tag_list = driver.find_element(By.ID  , Tags.DEVICE_LIST)
        
        items = tag_list.find_elements( By.TAG_NAME , "li")

        
    
        for item in items:
            try:
                name = item.find_element(By.CLASS_NAME , Tags.LI_HOST_NAME).text
                info = item.find_element(By.CLASS_NAME , Tags.LI_HOST_IP).text.split('\n')
            except:
                continue
                
            element = {
               'name' :  name,
               'ip' : info[0] ,
               'type' : info[1] ,
               'is_invited' : is_invited
            }
            device_list.append(element)
            
       
               
                    
    
     