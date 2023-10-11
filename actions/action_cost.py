
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from rasa_sdk.types import DomainDict
import requests
from underthesea import classify
from config import CONST_DOMAIN
from  utils.element import *
from utils.SynonymMapper import * 


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
    

class ActionCostMethod(Action):
    def name(self) -> Text:
        return "action_cost_methods"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        domain = '{}/cost/methods'.format(CONST_DOMAIN)
        message = ''
        message_pattern = 'Trường có hai phương thức thanh toán: \n{}'
        try: 
            request = requests.get(domain)
            if request.status_code == 200:
                data = request.json()
                description_list = [method_data["description"] for method_data in data["data"].values()]
                message = message_pattern.format(('\n').join(element_enumerate(description_list, start = 1)))
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
        domain = domain = '{}/cost/scholarship/{}/{}'.format(CONST_DOMAIN, scholarship_name, 'number')

        request = requests.get(domain)
        message = ''
        message_pattern = 'Số lượng suất học bổng của trường ở ngành này là {}'

        try: 
            if request.status_code == 200:
                data = request.json()
                scholarship_number = data['data']
                print(scholarship_number)
                message = message_pattern.format(scholarship_number)
        except Exception as e: 
            print(e)

        dispatcher.utter_message(text = message)
        return []
    
class ActionCostSupportDetailsCondition(Action):

    def name(self) -> Text:
        return "action_cost_support_details_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        scholarship_name = tracker.get_slot("scholarship_name")
        domain = domain = '{}/cost/scholarship/{}/{}'.format(CONST_DOMAIN, scholarship_name, 'conditions')

        request = requests.get(domain)
        message = ''
        message_pattern = 'Để đạt được học bổng bạn cần có những điều kiện sau: \n{}'

        try: 
            if request.status_code == 200:
                data = request.json()
                descriptions = [ '- ' + doc.get('description') for doc in list(data['data'].values())]
                message = message_pattern.format(('\n').join(descriptions))
        except Exception as e: 
            print(e)
                
    
        dispatcher.utter_message(text = message)
        return []
    
class ActionCostSupportDetailsMoney(Action):
    def name(self) -> Text:
        return "action_cost_support_details_money"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        scholarship_name = tracker.get_slot("scholarship_name")
        domain = domain = '{}/cost/scholarship/{}/{}'.format(CONST_DOMAIN, scholarship_name, 'money')

        request = requests.get(domain)
        message = ''
        message_pattern = 'Số tiền của học bổng là {} {}'

        try: 
            if request.status_code == 200:
                data = request.json()
                money_value = data['data']['value']
                money_type = data['data']['type']
        
                message = message_pattern.format(money_value, money_type)
        
        except Exception as e: 
            print(e)
        dispatcher.utter_message(text = message)
        return []

class ValidateScholarshipNameForm(FormValidationAction):
    def name(self) -> Text:
        self.synonyms = SynonymMapper()
        return "validate_scholarship_name_form"

    def validate_scholarship_name(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict ) -> Dict[Text, Any]: 
        scholarship_name = None
        try: 
            scholarship_name = self.synonyms.mapping_text(slot_value)
        except Exception: 
            print('error')
       
        if check_scholarship_name(scholarship_name=scholarship_name) == True: 
            
            return {"scholarship_name": scholarship_name}
        
        message = "Chúng tôi không có loại học bổng này! Vui lòng kiểm tra lại trên học bổng"
        dispatcher.utter_message(text = message)

        return {"scholarship_name": None}
