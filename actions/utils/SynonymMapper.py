import os
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class SynonymMapper(): 
    def __init__(self):
        logger.info('Loading Synonym Mapper...')
        self.data = self.load()

    def find_files(self,directory_list, file_extension):
        for root, dirs, files in os.walk(directory_list):
            for file in files:
                if file.endswith(file_extension):
                    return(os.path.join(root, file))
                
        return None
    def read_json_file(self,file_path): 
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
        
        return {}

    def load(self):
        data = None
        try: 
            directory_list = '../.rasa/cache'
            file_extension = 'synonyms.json'
            file_path = self.find_files(directory_list=directory_list, file_extension=file_extension)
            if file_path is None: 
                return None
            data = self.read_json_file(file_path=file_path)
        except Exception: 
            logger.debug("Don't find file synonym in storage")
        return data

    def mapping_text(self,word):
        synonym = self.data.get(word)

        if synonym is None:
            return None
        
        return synonym.lower()


    
