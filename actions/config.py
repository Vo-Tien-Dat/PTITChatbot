from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
port = os.getenv('PORT')
url = os.getenv('URL')
CONST_DOMAIN = '{}:{}'.format(url,port)