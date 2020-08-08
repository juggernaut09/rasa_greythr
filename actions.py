# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, AllSlotsReset, BotUttered, SlotSet,
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
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted
import re, requests
backend_url = "http://127.0.0.1:5000"

class ActionGreetUser(Action):
"""Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]


class SignupForm(FormAction):
    def name(self) -> Text:
    """Unique identifier of the form"""
    return "signup_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["emp_id", "name", "mobile", "email", "role"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "emp_id": [
                self.from_entity(entity="emp_id"),
                self.from_text(intent="inform"),
            ],
            "name": [self.from_text(intent="inform")],
            "email": [
                self.from_entity(entity="email"),
                self.from_text(intent="inform"),
            ],
            "mobile": [
                self.from_entity(entity="mobile"),
                self.from_text(intent="inform"),
            ],
            "role": [
                self.from_entity(entity="role"),
                self.from_text(intent="inform"),
            ],
        }

    def validate_mobile(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     match = re.match("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", value)
                     if match:
                        # validation succeeded
                        return value
                    else:
                        dispatcher.utter_message(template='Please check your mobile number you have typed', tracker)
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return None

    def validate_email(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     match = re.match("[^@ \t\r\n]+@vitwit\.[^@ \t\r\n]+", value.lower())
                     if match:
                        # validation succeeded
                        return value.lower()
                    else:
                        dispatcher.utter_message(template='Your email should be your work Email', tracker)
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return None

    def validate_emp_id(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     match = re.match("VW[0-9]{4}", value)
                     if match:
                        # validation succeeded
                        return value
                    else:
                        dispatcher.utter_message(template='Employee ID starts with VW and has 6 letters', tracker)
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return None

    def validate_role(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     if value.lower() in ["admin", "employee"]:
                         return value.lower()
                     else:
                         dispatcher.utter_message(template='Role must be either admin or employee', tracker)
                         return None
    def submit(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict]:
            data = {
                "email": tracker.get_slot("email"),
                "emp_id": tracker.get_slot("emp_id"),
                "role": tracker.get_slot("role"),
                "mobile": tracker.get_slot("mobile"),
                "name": tracker.get_slot("name")
            }
            response = requests.post("{}/employee/signup".format(backend_url), data)
            body = response.json()
            if response.status_code == 409 or response.status_code == 401 or response.status_code == 500:
                dispatcher.utter_message(template=body['message'], tracker)
                return[AllSlotsReset()]
            elif response.status_code == 200:
                dispatcher.utter_message(template=body['message'], tracker)
                return[]

class SigninForm(FormAction):
    def name(self) -> Text:
    """Unique identifier of the form"""
    return "signin_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["emp_id", "role"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "emp_id": [
                self.from_entity(entity="emp_id"),
                self.from_text(intent="inform"),
            ],
            "role": [
                self.from_entity(entity="role"),
                self.from_text(intent="inform"),
            ],
        }

    def validate_emp_id(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     match = re.match("VW[0-9]{4}", value)
                     if match:
                        # validation succeeded
                        return value
                    else:
                        dispatcher.utter_message(template='Employee ID starts with VW and has 6 letters', tracker)
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return None

    def validate_role(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     if value.lower() in ["admin", "employee"]:
                         return value.lower()
                     else:
                         dispatcher.utter_message(template='Role must be either admin or employee', tracker)
                         return None
    def submit(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict]:
            data = {
                "emp_id": tracker.get_slot("emp_id"),
                "role": tracker.get_slot("role")
            }
            response = requests.post("{}/employee/signin".format(backend_url), data)
            body = response.json()
            if response.status_code == 409 or response.status_code == 401 or response.status_code == 500:
                dispatcher.utter_message(template=body['message'], tracker)
                return [AllSlotsReset()]
            elif response.status_code == 200:
                dispatcher.utter_message(template=body['message'], tracker)
                return [SlotSet("email", value=body["email"]),
                        SlotSet("mobile", value=body["mobile"]),
                        SlotSet("name", value=body["name"])]



class ActionExplainSignupForm(Action):
    """Returns the explanation for the signup form questions"""

    def name(self) -> Text:
        return "action_explain_signup_form"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        requested_slot = tracker.get_slot("requested_slot")

        if requested_slot not in SignupForm.required_slots(tracker):
            dispatcher.utter_message(
                template="Sorry, I didn't get that. Please rephrase or answer the question "
                "above."
            )
            return []

        dispatcher.utter_message(template=f"utter_explain_{requested_slot}")
        return []

class ActionExplainSigninForm(Action):
    """Returns the explanation for the signin form questions"""

    def name(self) -> Text:
        return "action_explain_signin_form"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        requested_slot = tracker.get_slot("requested_slot")

        if requested_slot not in SigninForm.required_slots(tracker):
            dispatcher.utter_message(
                template="Sorry, I didn't get that. Please rephrase or answer the question "
                "above."
            )
            return []

        dispatcher.utter_message(template=f"utter_explain_{requested_slot}")
        return []
