# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormAction

class ActionPizzaOrderForm(FormAction):

    def name(self) -> Text:
        return "action_pizza_order_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["pizza_size", "pizza_type", "pizza_amount"]

    def submit(self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Dict]:
        pizza_type = tracker.get_slot('pizza_type')
        pizza_size = tracker.get_slot('pizza_size')
        pizza_amount = tracker.get_slot('pizza_amount')

        print(pizza_amount, pizza_type, pizza_size)

        dispatcher.utter_message(text=f"Ok Great. Your order is {pizza_amount} {pizza_type} pizzza in {pizza_type} size. Can you please confirm your order?")

        return []