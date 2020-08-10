# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
    AllSlotsReset,
    BotUttered,
    SlotSet
)
INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_description_mapping.csv"
import re, requests
backend_url = "http://127.0.0.1:5000"

class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
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
                        return {'mobile': value}
                     else:
                        dispatcher.utter_message(text="Please check your mobile number you have typed")
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return {'mobile': None}

    def validate_email(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     match = re.match("[^@ \t\r\n]+@vitwit\.[^@ \t\r\n]+", value.lower())
                     if match:
                        # validation succeeded
                        return {'email': value.lower()}
                     else:
                        dispatcher.utter_message(text='Your email should be your work Email')
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return {'email': None}

    def validate_emp_id(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     match = re.match("VW[0-9]{4}", value)
                     if match:
                        # validation succeeded
                        return {'emp_id': value}
                     else:
                        dispatcher.utter_message(text='Employee ID starts with VW and has 6 letters')
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return {'emp_id': None}

    def validate_role(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     if value.lower() in ["admin", "employee"]:
                         return {'role': value.lower()}
                     else:
                         dispatcher.utter_message(text='Role must be either admin or employee')
                         return {'role': None}
    def submit(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict]:
            if tracker.get_slot("is_authenticated"):
                dispatcher.utter_message(text="You have already signed in")
                return[]
            my_obj = {
                "email": tracker.get_slot("email"),
                "emp_id": tracker.get_slot("emp_id"),
                "role": tracker.get_slot("role"),
                "mobile": tracker.get_slot("mobile"),
                "name": tracker.get_slot("name")
            }
            response = requests.post("{}/employee/signup".format(backend_url), json=my_obj)
            body = response.json()
            if response.status_code == 409 or response.status_code == 401 or response.status_code == 500:
                dispatcher.utter_message(text=body['message'])
                return[AllSlotsReset()]
            elif response.status_code == 200:
                dispatcher.utter_message(text=body['message'])
                return[SlotSet("is_authenticated", True)]

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
                        return {'emp_id': value}
                     else:
                        dispatcher.utter_message(text='Employee ID starts with VW and has 6 letters')
                        # validation failed, set this slot to None, meaning the
                        # user will be asked for the slot again
                        return {'emp_id': None}

    def validate_role(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Optional[Text]:

                     if value.lower() in ["admin", "employee"]:
                         return {'role': value.lower()}
                     else:
                         dispatcher.utter_message(text='Role must be either admin or employee')
                         return {'role': None}
    def submit(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict]:
            if tracker.get_slot("is_authenticated"):
                dispatcher.utter_message(text="You have already signed in")
                return[]
            my_obj = {
                "emp_id": tracker.get_slot("emp_id"),
                "role": tracker.get_slot("role")
            }
            response = requests.post("{}/employee/signin".format(backend_url), json=my_obj)
            body = response.json()
            if response.status_code == 409 or response.status_code == 401 or response.status_code == 500:
                dispatcher.utter_message(text = body['message'])
                return [AllSlotsReset()]
            elif response.status_code == 200:
                dispatcher.utter_message(text= "You have successfully Logged in")
                return [SlotSet("email", value=body["email"]),
                        SlotSet("mobile", value=body["mobile"]),
                        SlotSet("name", value=body["name"]),
                        SlotSet("is_authenticated", True)]



class ActionExplainSignupForm(Action):
    """Returns the explanation for the signup form questions"""

    def name(self) -> Text:
        return "action_explain_signup_form"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        requested_slot = tracker.get_slot("requested_slot")

        if requested_slot not in SignupForm.required_slots(tracker):
            dispatcher.utter_message(
                text="Sorry, I didn't get that. Please rephrase or answer the question "
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
                text="Sorry, I didn't get that. Please rephrase or answer the question "
                "above."
            )
            return []
        dispatcher.utter_message(template=f"utter_explain_{requested_slot}")
        return []

class ActionPause(Action):
    """Pause the conversation"""

    def name(self) -> Text:
        return "action_pause"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        return [ConversationPaused()]

class ActionSignout(Action):
    def name(self) -> Text:
        return "action_signout"
    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        if not tracker.get_slot("is_authenticated"):
            dispatcher.utter_message(text="You are not logged in")
            return []
        dispatcher.utter_message(text="Hope you will come back!!")
        return [AllSlotsReset()]

class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]

        # for the intent name used to retrieve the button title, we either use
        # the name of the name of the "main" intent, or if it's an intent that triggers
        # the response selector, we use the full retrieval intent name so that we
        # can distinguish between the different sub intents
        first_intent_names = [
            intent.get("name", "")
            if intent.get("name", "") not in ["out_of_scope", "faq", "chitchat"]
            else tracker.latest_message.get("response_selector")
            .get(intent.get("name", ""))
            .get("full_retrieval_intent")
            for intent in intent_ranking
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            button_title = self.get_button_title(intent, entities)
            if "/" in intent:
                # here we use the button title as the payload as well, because you
                # can't force a response selector sub intent, so we need NLU to parse
                # that correctly
                buttons.append({"title": button_title, "payload": button_title})
            else:
                buttons.append(
                    {"title": button_title, "payload": f"/{intent}{entities_json}"}
                )

        buttons.append({"title": "Something else", "payload": "/trigger_rephrase"})

        dispatcher.utter_message(message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_message(template="utter_restart_with_button")
            return [ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_default")
            return [UserUtteranceReverted()]

class ActionMarkAttendance(Action):
    def name(self) -> Text:
        return "action_mark_attendance"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[EventType]:
        if not tracker.get_slot("is_authenticated"):
            dispatcher.utter_message(text="To do this action You must be logged in")
            return []
        my_obj = {
        "emp_id": tracker.get_slot("emp_id"),
        "role": tracker.get_slot("role")
        }
        response = requests.post("{}/mark/attendance".format(backend_url), json=my_obj)
        body = response.json()
        if response.status_code == 409 or response.status_code == 500 or response.status_code == 401 or response.status_code == 400:
            dispatcher.utter_message(text=body["message"])
            return []
        elif response.status_code == 200:
            dispatcher.utter_message(text=body["message"])
            return []
