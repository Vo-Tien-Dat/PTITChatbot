import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker, ValidationAction, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher

class ValidateName(FormValidationAction):
    def name(self) -> Text:
        return "validate_name"

    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        print('oke')
        if len(value) > 10:
            dispatcher.messages(text = "Chúng tôi chỉ có tên dưới 10 ký tự")
            return {'name': None}
        dispatcher.utter_message(text="Vậy tên cậu là {value}")
        return {"name": value}