
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from underthesea import classify
from config import CONST_DOMAIN


class ActionConditions(Action):
    def name(self) -> Text:
        return "action_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text = "",buttons=[
            {
                'title': 'Điểm',
                'payload': '/ask_for_condition_score'
            },
            {
                'title': 'Bằng cấp', 
                'payload': 'ask_for_condition_degree'
            }, 
            {
                'title': 'Chứng chỉ',
                'payload': '/ask_for_condition_certificates'
            },
            {
                'title': 'Học bạ',
                'payload': '/ask_for_condition_profile'
            }
        ])
        return []

class ActionConditionScore(Action):
    def name(self) -> Text:
        return "action_condition_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        message = 'Điểm trung học phổ thông quốc gia đạt tổng 3 môn trên 20 điểm'

        dispatcher.utter_message(text = message)
        return []
    


class ActionConditionDegree(Action):
    def name(self) -> Text:
        return "action_condition_degree"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        message = 'Bạn cần phải có bằng tốt nghiệp câp 3 để xét tuyển'

        dispatcher.utter_message(text = message)
        return []
    

class ActionConditionCertificates(Action):
    def name(self) -> Text:
        return "action_condition_certificates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        message = 'Bạn cần phải có TOEIC với trên 650 điểm hoặc IELTS cần 5.5'

        dispatcher.utter_message(text = message)
        return []
    

class ActionConditionProfile(Action):
    def name(self) -> Text:
        return "action_condition_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        message = 'Bạn cần phải có học bạ các môn trên 8.0'

        dispatcher.utter_message(text = message)
        return []
    


    