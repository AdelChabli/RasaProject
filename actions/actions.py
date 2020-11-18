from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from salles import salleLibre


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_give_salle"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = salleLibre('3','10.30','2020-11-18')

        dispatcher.utter_template("utter_salle", tracker, sallesDispo=response)

        return []
