from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import spacy

nlp = spacy.load("pl_core_news_lg")

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Witaj w Audytorium! Przed przystąpieniem do audytu upewnij się, czy sprawdziłeś wszystkie wymogi przeprowadzenia dobrego audytu. Jeśli jesteś gotów, daj znać")
        return []

class ActionStart(Action):
    def name(self) -> str:
        return "action_start"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy istnieje system monitorujący czas pracy Pracowników? Jaki to system?")
        return []

class ActionAskQuestion1(Action):
    def name(self) -> str:
        return "action_ask_question_1"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy istnieje system monitorujący czas pracy pracowników? Jaki to system?")
        return []

class ActionProcessAnswer1(Action):
    def name(self) -> str:
        return "action_process_answer_1"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. System monitorujący to: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion2(Action):
    def name(self) -> str:
        return "action_ask_question_2"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie są konsekwencje nieprzestrzegania wymogów dotyczących czasu pracy?")
        return []

class ActionProcessAnswer2(Action):
    def name(self) -> str:
        return "action_process_answer_2"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Konsekwencje nieprzestrzegania to: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion3(Action):
    def name(self) -> str:
        return "action_ask_question_3"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak przestrzegane są przepisy BHP?")
        return []

class ActionProcessAnswer3(Action):
    def name(self) -> str:
        return "action_process_answer_3"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Przestrzeganie przepisów BHP wygląda tak: {user_response}"
        dispatcher.utter_message(text=response)
        return []

# Dalej według tego samego schematu dla pozostałych pytań i odpowiedzi...

class ActionAskQuestion4(Action):
    def name(self) -> str:
        return "action_ask_question_4"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak Personel jest szkolony w zakresie przestrzegania przepisów BHP?")
        return []

class ActionProcessAnswer4(Action):
    def name(self) -> str:
        return "action_process_answer_4"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Szkolenie personelu wygląda tak: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion5(Action):
    def name(self) -> str:
        return "action_ask_question_5"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="W jaki sposób Pracodawca zapewnia możliwość udzielenia pierwszej pomocy?")
        return []

class ActionProcessAnswer5(Action):
    def name(self) -> str:
        return "action_process_answer_5"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Zapewnienie pierwszej pomocy wygląda tak: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion6(Action):
    def name(self) -> str:
        return "action_ask_question_6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie kroki podejmowane są w przypadku stwierdzenia naruszeń przepisów BHP?")
        return []

class ActionProcessAnswer6(Action):
    def name(self) -> str:
        return "action_process_answer_6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Kroki podejmowane w przypadku naruszeń przepisów BHP to: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion7(Action):
    def name(self) -> str:
        return "action_ask_question_7"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy na terenie zakładu pracy obowiązuje zakaz palenia papierosów? Jeżeli tak, jak egzekwowane jest złamanie zakazu?")
        return []

class ActionProcessAnswer7(Action):
    def name(self) -> str:
        return "action_process_answer_7"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Zakaz palenia i jego egzekwowanie wygląda tak: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion8(Action):
    def name(self) -> str:
        return "action_ask_question_8"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie są najczęstsze przyczyny zakłóceń w pracy niezależnych od pracowników?")
        return []

class ActionProcessAnswer8(Action):
    def name(self) -> str:
        return "action_process_answer_8"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Najczęstsze przyczyny zakłóceń to: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion9(Action):
    def name(self) -> str:
        return "action_ask_question_9"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie działania podejmowane są w celu minimalizacji wpływu zakłóceń zewnętrznych na wydajność i efektywność pracy?")
        return []

class ActionProcessAnswer9(Action):
    def name(self) -> str:
        return "action_process_answer_9"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Działania minimalizujące wpływ zakłóceń to: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion10(Action):
    def name(self) -> str:
        return "action_ask_question_10"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak firma radzi sobie z awariami technicznymi podczas pracy linii produkcyjnej?")
        return []

class ActionProcessAnswer10(Action):
    def name(self) -> str:
        return "action_process_answer_10"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Radzenie sobie z awariami technicznymi wygląda tak: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion11(Action):
    def name(self) -> str:
        return "action_ask_question_11"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy są prowadzone szkolenia z obsługi technicznej maszyn i urządzeń? Jak często są prowadzone te szkolenia?")
        return []

class ActionProcessAnswer11(Action):
    def name(self) -> str:
        return "action_process_answer_11"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Szkolenia z obsługi technicznej maszyn i urządzeń są prowadzone tak: {user_response}"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion12(Action):
    def name(self) -> str:
        return "action_ask_question_12"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy masz jeszcze jakieś pytania lub wątpliwości dotyczące BHP i czasu pracy?")
        return []

class ActionProcessAnswer12(Action):
    def name(self) -> str:
        return "action_process_answer_12"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Dziękuję za odpowiedź. Dodatkowe pytania lub wątpliwości: {user_response}"
        dispatcher.utter_message(text=response)
        return []
