
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from underthesea import classify
from config import CONST_DOMAIN
from rasa_sdk.events import FollowupAction

class ActionConditions(Action):
    def name(self) -> Text:
        return "action_conditions"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        return [FollowupAction('utter_conditions')]

class ActionConditionScore(Action):
    def name(self) -> Text:
        return "action_condition_score"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = 'Điểm trung học phổ thông quốc gia đạt tổng 3 môn trên 20 điểm'

        dispatcher.utter_message(text = message)
        return []
    


class ActionConditionDegree(Action):
    def name(self) -> Text:
        return "action_condition_degree"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        message = 'Bạn cần phải có bằng tốt nghiệp câp 3 để xét tuyển'

        dispatcher.utter_message(text = message)
        return []
    

class ActionConditionCertificates(Action):
    def name(self) -> Text:
        return "action_condition_certificates"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        message = 'Bạn cần phải có TOEIC với trên 650 điểm hoặc IELTS cần 5.5'

        dispatcher.utter_message(text = message)
        return []
    

class ActionConditionProfile(Action):
    def name(self) -> Text:
        return "action_condition_profile"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = 'Bạn cần phải có học bạ các môn trên 8.0'
        dispatcher.utter_message(text = message)
        return []
    


    