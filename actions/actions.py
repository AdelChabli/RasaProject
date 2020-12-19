# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requestAPI as api
import utilFunction as uti
from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionGetSchedule(Action):

    def name(self) -> Text:
        return "action_get_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        section = tracker.get_slot('SECTION')
        spec = tracker.get_slot('SPEC')

        # if api.isMultipleLesson(section, spec):
        if True:
            return [SlotSet("isMultipleLesson", True)]

        now = datetime.now().astimezone()
        title = uti.respForAllLesson(api.getScheduleByPromo(section, spec, now))

        if title == "":
            text = "Vous n'avez pas cours actuellement"
        else:
            text = title
        dispatcher.utter_message(text)

        return []


class ActionGetScheduleWithGroup(Action):

    def name(self) -> Text:
        return "action_get_schedule_with_group"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        section = tracker.get_slot('SECTION')
        group = tracker.get_slot('GROUP')
        spec = tracker.get_slot('SPEC')

        now = datetime.now().astimezone()
        title = uti.respForAllLesson(api.getScheduleByPromo(section, spec, now))

        if title == "":
            text = "Vous n'avez pas cours actuellement"
        else:
            text = title
        dispatcher.utter_message(text)

        return []


class ActionGiveRoom(Action):

    def name(self) -> Text:
        return "action_give_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # TODO
        title = ""
        if title == "":
            text = "Vous n'avez pas cours actuellement"
        else:
            text = title
        dispatcher.utter_message(text)

        return []
