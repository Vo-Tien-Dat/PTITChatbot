from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime
from shared.slot_identification import SlotIdentification
from shared.slot_identification import CON_SLOT_NONE, CON_SLOT_EXISTING, CON_SLOT_NOT_EXISTING

# ĐỌC DỮ LIỆU TẠM THỜI BẰNG FILE JSON
def read_json(fileName: Text): 
    data = None
    with open(fileName, 'r') as file: 
        data = json.loads(file.read())
    return data

data = read_json('data.json')

# XÂY DỰNG CÁC ACTION DÀNH CHO MỘT TRONG MỘT PHƯƠNG ÁN TUYỂN SINH
class ActionListOfScholarship(Action):

    def name(self) -> Text:
        return "action_list_of_scholarships"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        rows = []
        values = data['scholarship'].values()
        index = 1

        for value in values: 
            rows.append("{}. {}: {}".format(index, value['name'], value['description']))
            index = index + 1
        message = '' if len(rows) == 0 else '\n' .join(rows)

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
        
        scholarshipConditionsObj = data.get('scholarship_conditions')
        scholarshipConditionMes = map(lambda sub: '{}: {}'.format(sub.get('name'), sub.get('description')), list(scholarshipConditionsObj.values()))
        message = '\n'.join(list(scholarshipConditionMes))

        dispatcher.utter_message(text=message)
        return []
    
class ActionScholarshipDocument(Action): 
    def name(self) -> Text:
        return "action_scholarship_documents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        scholarshipDocumentsObj = data.get('scholarship_documents')
        scholarshipDocumentsMes  =map(lambda sub: '{}: {}'.format(sub.get('name'), sub.get('description')), list(scholarshipDocumentsObj.values()))
        message = '\n'.join(scholarshipDocumentsMes)

        dispatcher.utter_message(text=message)
        return []
    

class ActionScholarshipDeadline(Action): 
    def name(self) -> Text:
        return "action_scholarship_deadline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        scholarshipDeadlineValue = data.get('deadline')
        datePattern = "%d-%m-%Y %H:%M:%S"

        dateScholarshipDeadlineObj = datetime.strptime(str(scholarshipDeadlineValue),datePattern)
        message = 'Hạn cuối nộp hồ sơ vào ngày {} tháng {} năm {} vào lúc {}'.format(dateScholarshipDeadlineObj.day, dateScholarshipDeadlineObj.month, dateScholarshipDeadlineObj.year, dateScholarshipDeadlineObj.year, dateScholarshipDeadlineObj.hour)
        
        dispatcher.utter_message(text=message)
        return []

class ActionScholarshipMoney(Action): 
    def name(self) -> Text:
        return "action_scholarship_money"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        scholarshipMoneyObj = data.get('scholarship_money')
        scholarshipMoneyValue = scholarshipMoneyObj.get('value')
        scholarshipMoneyType = scholarshipMoneyObj.get('type')

        message = 'Số tiền bạn được cấp trong đợt học bổng này {} {}'.format(scholarshipMoneyValue, scholarshipMoneyType)

        dispatcher.utter_message(text=message)
        return []
    

class ActionScholarshipTime(Action): 
    def name(self) -> Text:
        return "action_scholarship_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        scholarshipTimeObj = data.get('scholarship_time')
        scholarshipTimeValue = scholarshipTimeObj.get('value')
        scholarshipTimeType = scholarshipTimeObj.get('type')

        message = 'Thời gian bạn hoàn thành cho đợt học bổng này {} {}'.format(scholarshipTimeValue, scholarshipTimeType)

        dispatcher.utter_message(text=message)
        return []


class ActionSpecificScholarship(Action): 
    def name(self) -> Text:
        return "action_the_specific_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot_scholarship_value = tracker.get_slot("scholarship_name")
        exis_scholarship_name = ['hoc_bong_nghien_cuu_khoa_hoc', 'hoc_bong_khuyen_khich_hoc_tap']

        print(slot_scholarship_value)

        # slot_status = SlotIdentification.builder(slot_scholarship_value[0]).check_none().check_existing(exis_scholarship_name).build()

        # if(slot_status == CON_SLOT_NONE): 
        #     message = "Vui lòng cung câp thêm tên học bổng"

        # elif slot_status == CON_SLOT_NOT_EXISTING:
        #     message = "Học bổng này không tông tài"
        # else: 
        #     message = "run"

        message = ''
        dispatcher.utter_message(text=message)
        return []

