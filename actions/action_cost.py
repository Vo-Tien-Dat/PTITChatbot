
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from underthesea import classify
from config import CONST_DOMAIN



class ActionForCostProgram(Action):
    def name(self) -> Text:
        return "action_cost_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        domain = '{}/admission/documents'.format(CONST_DOMAIN)
        message_pattern = "Bạn cần chuẩn bị những giấy tờ sau: {} "
        request = requests.get(domain)
        message = ''
        try: 
            if request.status_code == 200:
                data = request.json()
                docs = [ doc.get('name') for doc in list(data['data'].values())]
                message = message_pattern.format((',').join(docs))
        except Exception as e: 
            print(e)

        dispatcher.utter_message(text = message)
        return []