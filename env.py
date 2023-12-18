import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    PASSWORD_TPLINK = os.getenv('PASSWORD_TPLINK')
    URL = os.getenv('URL')
    CONTAINER = os.getenv('CONTAINER') == 'Y' 
    DEBUG_BROWSER = os.getenv('DEBUG_BROWSER') == 'Y' 
    
