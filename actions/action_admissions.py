
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from underthesea import classify
from config import CONST_DOMAIN


class ActionForAdmisisonDocument(Action):
    def name(self) -> Text:
        return "action_admission_document"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = 'admission document'
        dispatcher.utter_message(text=message)
        return []