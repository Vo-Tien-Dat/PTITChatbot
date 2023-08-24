
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
import requests
from underthesea import classify
from config import CONST_DOMAIN
from  utils.element import *


scholarship_name_values = ['khuyen_khich_hoc_tap', 'nghien_cuu_khoa_hoc']

def check_scholarship_name(scholarship_name):
    if  scholarship_name is None:
        return False
    if scholarship_name not in scholarship_name_values:
        return False
    return True


class ActionCostProgram(Action):
    def name(self) -> Text:
        return "action_cost_program"

    async def run(self, dispatcher: CollectingDispatcher,
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

class ActionCostSupport(Action):
    def name(self) -> Text:
        return "action_cost_support"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text_scholarship = 'Trường có những học bổng sau'
        btn_scholarship_attr = [
            {
                'title': 'khuyến khích học tập', 
                'payload': '/ask_for_cost_support_details',
            },
            {
                'title': 'nghiên cứu khoa học', 
                'payload': '/ask_for_cost_support_details'
            },
        ]
        dispatcher.utter_message(text=text_scholarship)
        dispatcher.utter_message(buttons=btn_scholarship_attr)
        return [FollowupAction('utter_cost_support')]
class ActionCostSupportDetails(Action):
    def name(self) -> Text:
        return "action_cost_support_details"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        scholarship_name = tracker.get_slot("scholarship_name")
        print(scholarship_name)
        if check_scholarship_name(scholarship_name) == False:
            return [FollowupAction('action_cost_support')]
        
                
        return [FollowupAction('utter_cost_support_details')]
    
class ActionCostSupportDetailsNumber(Action):
    def name(self) -> Text:
        return "action_cost_support_details_number"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        scholarship_name = tracker.get_slot("scholarship_name")
        if check_scholarship_name(scholarship_name) == False:
            return [FollowupAction('action_cost_support_details')]
        
        message = 'Số lượng học bổng là 15 suất học bổng'

        dispatcher.utter_message(text = message)
        return []
    
class ActionCostSupportDetailsCondition(Action):
    def name(self) -> Text:
        return "action_cost_support_details_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        scholarship_name = tracker.get_slot("scholarship_name")
        if check_scholarship_name(scholarship_name) == False:
            return [FollowupAction('action_cost_support_details')]
        
        message = 'Điều kiện có học bổng '

        dispatcher.utter_message(text = message)
        return []
    
class ActionCostSupportDetailsMoney(Action):
    def name(self) -> Text:
        return "action_cost_support_details_money"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        scholarship_name = tracker.get_slot("scholarship_name")
        if check_scholarship_name(scholarship_name) == False:
            return [FollowupAction('action_cost_support_details')]
        
        message = 'Số tiền của học bổng'

        dispatcher.utter_message(text = message)
        return []