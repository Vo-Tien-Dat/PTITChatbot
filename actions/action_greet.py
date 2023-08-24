# import logging
# from typing import Any, Text, Dict, List, Union, Optional
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionGreet(Action):
#     def name(self) -> Text:
#         return "action_greet"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         domain = CONST_DOMAIN + '/major/read/lecturer'
#         request = requests.get(domain)

#         slot_major_value = tracker.get_slot("major")
#         classify_major_value = classify(slot_major_value)

#         try: 
#             major_name = classify_major_value[0]
#             if check_existing_major(major_name=major_name) == False:
#                 raise ValueError("Chúng tôi không có mảng này")
            
#             if request.status_code == 200: 
#                 lecturers = list_lecturer(request.json(),major_name=major_name)
            
#                 message = message_lecturer(lecturers)
            
#             if request.status_code == 500: 
#                 raise ValueError('Error Server')
            
#         except Exception as e: 
#             message = str(e)

#         dispatcher.utter_message(text=message)
#         return []