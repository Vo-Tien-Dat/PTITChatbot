import logging
from typing import Any, Text, Dict, List
import json
from datetime import datetime
import os
from dotenv import load_dotenv
from action_greet import *
from action_major import *
from action_program import * 
from action_scholarship import * 


logger = logging.getLogger(__name__)
print(logger)

load_dotenv()
port = os.getenv('PORT')
url = os.getenv('URL')
CONST_DOMAIN = '{}:{}'.format(url,port)


