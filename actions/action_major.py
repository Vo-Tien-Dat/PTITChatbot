
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from config import CONST_DOMAIN
from rasa_sdk.events import FollowupAction
from config import CONST_DOMAIN
from  utils.element import *

major_name_values = ['an_toan_thong_tin', 'cong_nghe_thong_tin', 'ke_toan', 'quan_tri_kinh_doanh']


def check_major_name(major_name):
    if major_name is None:
        return False

    if major_name not in major_name_values: 
        return False

    return True

class ActionMajor(Action):
    def name(self) -> Text:
        return "action_major"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return [FollowupAction('utter_major')]

class ActionMajorDetails(Action):
    def name(self) -> Text:
        return "action_major_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        major_name = tracker.get_slot("major_name")
        print(major_name)
        print(check_major_name(major_name))
        if check_major_name(major_name) == False:
            return [FollowupAction('action_major')]

        return [FollowupAction('utter_major_details')]
    

class ActionMajorContent(Action):
    def name(self) -> Text:
        return "action_major_content"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        major_name = tracker.get_slot("major_name")

        if check_major_name(major_name) == False:
            return [FollowupAction('action_major')]
        
        domain = '{}/major/content/{}'.format(CONST_DOMAIN,major_name)
        message_pattern = 'Nội dung học tập {}'
        message = ''
        try: 
            request = requests.get(domain)
            if request.status_code == 200:
                data = request.json()
                message = ''.join(list(data.values()))
        except Exception as e: 
            print(e)
        print(message)
        dispatcher.utter_message(text=message)
        return []
    
class ActionMajorSkill(Action):
    def name(self) -> Text:
        return "action_major_skill"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        major_name = tracker.get_slot("major_name")

        if check_major_name(major_name) == False:
            return [FollowupAction('action_major')]
    
        domain = '{}/major/skills/{}'.format(CONST_DOMAIN,major_name)
        try: 
            request = requests.get(domain)
            if request.status_code == 200:
                data = request.json()
                skills = [ name_element(ski.get('name')) for ski in list(data['data'].values())]
                message = ' '.join(skills)
        except Exception as e: 
            print(e)
        
        dispatcher.utter_message(text = message)
        return []
    
class ActionMajorOpportunity(Action):
    def name(self) -> Text:
        return "action_major_opportunity"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        major_name = tracker.get_slot("major_name")

        if check_major_name(major_name) == False:
            return [FollowupAction('action_major')]
    
        domain = '{}/major/opportunities/{}'.format(CONST_DOMAIN,major_name)
        try: 
            request = requests.get(domain)
            if request.status_code == 200:
                data = request.json()
                opptunities = [ name_and_description_element(opp.get('name'), opp.get('description')) for opp in list(data['data'].values())]
                messages = ' '.join(opptunities)
        except Exception as e: 
            print(e)
        
        dispatcher.utter_message(text = messages)
        return []