# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from service.action import get_text_weather_date
from service.normalization import text_to_date, date_to_daynum


class ActionReportWeather(Action):
    def __init__(self):
       pass 

    def name(self) -> Text:
        return "action_report_weather"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # print('tracker is ,', tracker)
        address = tracker.get_slot('address')
        date_time = tracker.get_slot('date-time')

        date_object = text_to_date(date_time)
        day_num = date_to_daynum(date_time)
        # print(address, day_num, date_object)
    

        if not date_time:  # parse date_time failed
            msg = "暂不支持查询 {} 的天气".format([address, date_time])
            return [SlotSet("matches", msg)]
            # print(msg)
            # dispatcher.utter_message(msg)
        else:
           try:
                weather_data = get_text_weather_date(address, date_to_daynum, date_object)
            except Exception as e:
                weather_data = str(e) + ' and your input is run. pls input 地点与时间。例如北京今天的天气'

            return [SlotSet("matches", "{}".format(weather_data))]
