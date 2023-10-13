
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
import requests
from config import CONST_DOMAIN
from rasa_sdk.events import FollowupAction
from config import CONST_DOMAIN
from  utils.element import *
from utils.SynonymMapper import * 
from rasa_sdk.types import DomainDict

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

        # if check_major_name(major_name) == False:
        #     return [FollowupAction('action_major')]
        
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
        message_pattern = 'Những kỹ năng cần có trong ngành học này \n {}'
        message = ''
        try: 
            request = requests.get(domain)
            if request.status_code == 200:
                data = request.json()
                skills = [ name_element(ski.get('name')) for ski in list(data['data'].values())]
                format_skills_message = '\n'.join(skills)
                message = message_pattern.format(format_skills_message)

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
        message_pattern = "Sinh viên ra trường của trường có cơ hội làm một số tập đoàn \n{}"
        messages = ''
        try: 
            request = requests.get(domain)
            if request.status_code == 200:
                data = request.json()
                opptunities = [ name_and_description_element(opp.get('name'), opp.get('description')) for opp in list(data['data'].values())]
                oppotunities_messages = '\n'.join(opptunities)
                print(oppotunities_messages)
                messages  = message_pattern.format(oppotunities_messages)
        except Exception as e: 
            print(e)
        
        dispatcher.utter_message(text = messages)
        return []
    

class ValidateMajorNameForm(FormValidationAction):
    def name(self) -> Text:
        self.synonyms = SynonymMapper()
        return "validate_major_name_form"

    def validate_major_name(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict ) -> Dict[Text, Any]: 

        major_name = "cong_nghe_thong_tin"
        print(slot_value)

        try: 
            major_name_from_entity = next(tracker.get_latest_entity_values("major_name"), None)
           
            # ưu tiên bấm nút
            if(major_name_from_entity is not None): 
                slot_value = major_name_from_entity
            
            slot_value = slot_value.strip()
            major_name = self.synonyms.mapping_text(slot_value)
            print(slot_value)
            if check_major_name(major_name=major_name) == True: 
                return {"major_name": major_name}
        
            message = "Trường không có ngành học bổng này"
            dispatcher.utter_message(text = message)

        except Exception: 
            dispatcher.utter_message(text = "Lỗi phát sinh! Vui lòng thử lại sau")
       
        return {"major_name": major_name}