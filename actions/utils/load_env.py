import os
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)
load_dotenv()



def check_environment_variable(vars: []): 
    result = {}
    for var in vars: 
        env_variable = os.environ.get(var)
        
        if env_variable is None: 
            raise ValueError('Value of {} is None'.format(var))

        else: 
            result[var] = env_variable
            print(result)
    logging.info('Loading Env is successful')
    return result
   