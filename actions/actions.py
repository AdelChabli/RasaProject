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
from db_sqlite import select_data

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


class ActionGetSchedule(Action):

    def name(self) -> Text:
        return "action_get_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        section = tracker.get_slot('SECTION')
        spec = tracker.get_slot('SPEC')

        if api.isMultipleLesson(section, spec):
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

        duration = tracker.get_slot('DURATION')
        hour_start = tracker.get_slot('START')
        date = datetime.now().astimezone()
        title = api.free_room(duration, hour_start, date)
        if title == "":
            text = "Il n'y a pas de salle disponible pour l'instant"
        else:
            text = title
        dispatcher.utter_message(text)

        return []


class ActionGetDirection(Action):

    def name(self) -> Text:
        return "action_get_direction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        room = tracker.get_slot('ROOM')
        title = select_data(room)
        if title == "":
            text = "Je ne connais pas cette salle."
            dispatcher.utter_message(text)
            return [FollowupAction('action_back')]
        else:
            text = title
            dispatcher.utter_message(text)

        return []
