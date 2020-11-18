# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requestAPI as api

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAPI(Action):

    def name(self) -> Text:
        return "action_get_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        api.getallgroup()
        section = tracker.get_slot('SECTION')
        field = tracker.get_slot('FIELD')
        group = tracker.get_slot('GROUP')
        text = "Si j'ai bien compris vous êtes en "+ field + " " + section + " " + group
        dispatcher.utter_message(text)

        return []
