import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker, ValidationAction, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher

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
        print(name_slot)
        print(name_entity)
        if name_entity:
            # Use the entity value in your custom action logic
            dispatcher.utter_message(f": {name_entity}")
        else:
            dispatcher.utter_message("Vui lòng cung cấp tên bạn cho tôi")

        return []
