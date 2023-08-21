from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime
import requests
from config import CONST_DOMAIN


class Entity:
    def __init__(self) -> None:
        print('Check entity')

    def builder(self, data): 
        self.data = data; 
        return self


    def field(self, key, payload = None): 
        if self.data.get(key) is not None: 
            self.data = self.data.get(key)
            return self
        
        if(payload is not None): 
            print('run')

        raise ValueError('Không tồn tai thuộc tính này')
    
    def build(self): 
        return self.data
 
class ActionListOfScholarship(Action):

    def name(self) -> Text:
        return "action_list_of_scholarships"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = ''

        dispatcher.utter_message(text=message)
        return []
    
class ActionDetailScholarship(Action):

    def name(self) -> Text:
        return "action_detail_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = ''

        dispatcher.utter_message(text=message)
        return []


class ActionScholarshipConditions(Action):

    def name(self) -> Text:
        return "action_scholarship_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        message = 'điều kiện đẻ đạt học bổng'

        dispatcher.utter_message(text=message)
        return []
    
class ActionScholarshipDocument(Action): 
    def name(self) -> Text:
        return "action_scholarship_documents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = ''

        dispatcher.utter_message(text=message)
        return []
    

class ActionScholarshipDeadline(Action): 
    def name(self) -> Text:
        return "action_scholarship_deadline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = ''
        
        dispatcher.utter_message(text=message)
        return []

class ActionScholarshipMoney(Action): 
    def name(self) -> Text:
        return "action_scholarship_money"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        message = ''

        dispatcher.utter_message(text=message)
        return []
    

class ActionScholarshipTime(Action): 
    def name(self) -> Text:
        return "action_scholarship_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # scholarshipTimeObj = data.get('scholarship_time')
        # scholarshipTimeValue = scholarshipTimeObj.get('value')
        # scholarshipTimeType = scholarshipTimeObj.get('type')


        # message = 'Thời gian bạn hoàn thành cho đợt học bổng này {} {}'.format(scholarshipTimeValue, scholarshipTimeType)
        message = ''

        dispatcher.utter_message(text=message)
        return []





def element_btn(payload, title): 
    return {
        'payload': payload,
        'title': title
    }

def list_btn_scholarship(data): 
    names = [element_btn(title='học bổng ' + item['name'], payload = '/ask_for_the_specific_scholarship') for item in data['data']]
    return names


class ActionListBtnOfScholarship(Action): 
    def name(self) -> Text:
        return "action_list_btn_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        domain = CONST_DOMAIN + '/scholarship/collect'
        request = requests.get(domain)
        
        try: 
            if request.status_code == 200:
                btn_scholarships = list_btn_scholarship(request.json())
                dispatcher.utter_message(buttons=btn_scholarships)
                return []
        except Exception as e: 
            message = str(e)

        message = 'hello tat ca moi nguoi tets'
        dispatcher.utter_message(text=message)
        return []


class ActionSpecificScholarship(Action): 
    def name(self) -> Text:
        return "action_the_specific_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_scholarship_value = tracker.get_slot("scholarship_name")
        exis_scholarship_name = ['nghien_cuu_khoa_hoc', 'khuyen_khich_hoc_tap']
        btn_scholarships = [
            {
                "payload": "/ask_for_the_specific_scholarship",
                "title": "học bổng nghiên cứu khoa học"
            }, 
            {
                "payload": "/ask_for_the_specific_scholarship",
                "title": "học bổng khuyến khích học tập"
            }
        ]

        if(slot_scholarship_value is None): 
            dispatcher.utter_message(buttons=btn_scholarships)
            return []

        if(slot_scholarship_value not in exis_scholarship_name): 
            dispatcher.utter_message(buttons=btn_scholarships)
            return []
        
        sub_mes_pattern = '{}: {}'
        message_pattern = 'Điều kiện để đạt được học bổng {}'
        message = message_pattern.format(message)


        

        message = 'hello tat ca moi nguoi tets'
        dispatcher.utter_message(text=message)
        return []





