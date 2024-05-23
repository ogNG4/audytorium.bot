from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import spacy

nlp = spacy.load("pl_core_news_lg")

class ActionGreet(Action):
    def name(self) -> str:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Cześć! Jak mogę Ci pomóc?")
        return []

class ActionStart(Action):
    def name(self) -> str:
        return "action_start"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy zaczynamy?")
        return []

class ActionAskQuestion1(Action):
    def name(self) -> str:
        return "action_ask_question_1"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy istnieje system monitorujący czas pracy pracowników? Jaki to system?")
        return [ActionListen()]
    

class ActionProcessAnswer1(Action):
    def name(self) -> str:
        return "action_process_answer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = process_answer(user_response)
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion2(Action):
    def name(self) -> str:
        return "action_ask_question_2"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie są konsekwencje nieprzestrzegania wymogów dotyczących czasu pracy?")
        return [ActionListen()]

class ActionProcessAnswer2(Action):
    def name(self) -> str:
        return "action_process_answer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = process_answer(user_response)
        dispatcher.utter_message(text=response)
        return []



class ActionGoodbye(Action):
    def name(self) -> str:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Dziękuję za rozmowę! Do zobaczenia!")
        return []

def process_answer(answer: Text):
    doc = nlp(answer)
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]

    if nouns and verbs:
        return f"Nie rozumiem. Czy możesz wyjaśnić, jak {verbs[0]} {nouns[0]}?"
    else:
        return "Przepraszam, nie mogę zrozumieć pytania. Proszę spróbować ponownie."
