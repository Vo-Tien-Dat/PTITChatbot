import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker, ValidationAction, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet


class ValidateName(Action):
    def name(self) -> Text:
        return "action_name"


    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Get the value of the 'name' entity
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        name_slot = tracker.get_slot("name")
        if name_entity:
            # Use the entity value in your custom action logic
            dispatcher.utter_message(f": {name_entity}")
        else:
            dispatcher.utter_message("Vui lòng cung cấp tên bạn cho tôi")

        return []

class ValidateEmailForm(FormValidationAction): 
    def name(self) -> Text: 
        return "validate_email_form"
    
    def validate_email(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict): 
    
        email = slot_value
        print(email)
        if email is None: 
            return {"email": None}
        if(len(email) >= 10): 
            print("email is less than 10 characters")
            dispatcher.utter_message(text = "Email này không đúng")
            return {"email": None}
        return {"email": slot_value}

class SubmitEmailForm(Action):
    def name(self) -> Text:
        return "submit_email_form"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        if email is not None: 
            dispatcher.utter_message(text = "email cua toi la: " + email)
        else: 
            print('email is None')
        return []

class ActionResetEmail(Action):
    def name(self) -> Text:
        return "action_reset_email"


    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        return [SlotSet('email', None)]

