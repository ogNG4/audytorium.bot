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
        dispatcher.utter_message(text="Jakie są konsekwencje nieprzestrzegania wymogów dotyczących czasu pracy?")
        return []

class ActionProcessAnswer1(Action):
    def name(self) -> str:
        return "action_process_answer_1"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie są konsekwencje nieprzestrzegania wymogów dotyczących czasu pracy?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion2(Action):
    def name(self) -> str:
        return "action_ask_question_2"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak przestrzegane są przepisy BHP?")
        return []

class ActionProcessAnswer2(Action):
    def name(self) -> str:
        return "action_process_answer_2"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jak przestrzegane są przepisy BHP?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion3(Action):
    def name(self) -> str:
        return "action_ask_question_3"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak Personel jest szkolony w zakresie przestrzegania przepisów BHP?")
        return []

class ActionProcessAnswer3(Action):
    def name(self) -> str:
        return "action_process_answer_3"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jak Personel jest szkolony w zakresie przestrzegania przepisów BHP?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion4(Action):
    def name(self) -> str:
        return "action_ask_question_4"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="W jaki sposób Pracodawca zapewnia możliwość udzielenia pierwszej pomocy?")
        return []

class ActionProcessAnswer4(Action):
    def name(self) -> str:
        return "action_process_answer_4"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"W jaki sposób Pracodawca zapewnia możliwość udzielenia pierwszej pomocy?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion5(Action):
    def name(self) -> str:
        return "action_ask_question_5"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie kroki podejmowane są w przypadku stwierdzenia naruszeń przepisów BHP?")
        return []

class ActionProcessAnswer5(Action):
    def name(self) -> str:
        return "action_process_answer_5"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie kroki podejmowane są w przypadku stwierdzenia naruszeń przepisów BHP?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion6(Action):
    def name(self) -> str:
        return "action_ask_question_6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Czy na terenie zakładu pracy obowiązuje zakaz palenia papierosów? Jeżeli tak, jak egzekwowane jest złamanie zakazu?")
        return []

class ActionProcessAnswer6(Action):
    def name(self) -> str:
        return "action_process_answer_6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Czy na terenie zakładu pracy obowiązuje zakaz palenia papierosów? Jeżeli tak, jak egzekwowane jest złamanie zakazu?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion7(Action):
    def name(self) -> str:
        return "action_ask_question_7"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie są najczęstsze przyczyny zakłóceń w pracy niezależnych od pracowników?")
        return []

class ActionProcessAnswer7(Action):
    def name(self) -> str:
        return "action_process_answer_7"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie są najczęstsze przyczyny zakłóceń w pracy niezależnych od pracowników?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion8(Action):
    def name(self) -> str:
        return "action_ask_question_8"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie działania podejmowane są w celu minimalizacji wpływu zakłóceń zewnętrznych na wydajność i efektywność pracy?")
        return []

class ActionProcessAnswer8(Action):
    def name(self) -> str:
        return "action_process_answer_8"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie działania podejmowane są w celu minimalizacji wpływu zakłóceń zewnętrznych na wydajność i efektywność pracy?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion9(Action):
    def name(self) -> str:
        return "action_ask_question_9"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak firma radzi sobie z awariami technicznymi podczas pracy linii produkcyjnej?")
        return []

class ActionProcessAnswer9(Action):
    def name(self) -> str:
        return "action_process_answer_9"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jak firma radzi sobie z awariami technicznymi podczas pracy linii produkcyjnej?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion10(Action):
    def name(self) -> str:
        return "action_ask_question_10"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakiego typu uwagi pracownicy zgłaszają dotyczące infrastruktury?")
        return []

class ActionProcessAnswer10(Action):
    def name(self) -> str:
        return "action_process_answer_10"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakiego typu uwagi pracownicy zgłaszają dotyczące infrastruktury?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion11(Action):
    def name(self) -> str:
        return "action_ask_question_11"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak firma zapewnia zgodność z regulacjami dotyczącymi ochrony środowiska?")
        return []

class ActionProcessAnswer11(Action):
    def name(self) -> str:
        return "action_process_answer_11"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jak firma zapewnia zgodność z regulacjami dotyczącymi ochrony środowiska?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion12(Action):
    def name(self) -> str:
        return "action_ask_question_12"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie istnieją plany ewakuacyjne i ćwiczenia dla pracowników w przypadku nagłych sytuacji, takich jak pożar czy awaria?")
        return []

class ActionProcessAnswer12(Action):
    def name(self) -> str:
        return "action_process_answer_12"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie istnieją plany ewakuacyjne i ćwiczenia dla pracowników w przypadku nagłych sytuacji, takich jak pożar czy awaria?"
        dispatcher.utter_message(text=response)
        return []

class ActionAskQuestion13(Action):
    def name(self) -> str:
        return "action_ask_question_13"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie są procedury zapobiegania nadużyć w obszarze magazynowania?")
        return []

class ActionProcessAnswer13(Action):
    def name(self) -> str:
        return "action_process_answer_13"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie są procedury zapobiegania nadużyć w obszarze magazynowania?"
        dispatcher.utter_message(text=response)
        return []
    
class ActionAskQuestion14(Action):
    def name(self) -> str:
        return "action_ask_question_14"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak firma monitoruje i ocenia wydajność procesów produkcyjnych i magazynowych? Jakie są stosowane wskaźniki wydajności?")
        return []

class ActionProcessAnswer14(Action):
    def name(self) -> str:
        return "action_process_answer_14"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jak firma monitoruje i ocenia wydajność procesów produkcyjnych i magazynowych? Jakie są stosowane wskaźniki wydajności?"
        dispatcher.utter_message(text=response)
        return []    
    
class ActionAskQuestion15(Action):
    def name(self) -> str:
        return "action_ask_question_15"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie działania podejmowane są w celu minimalizacji strat materiałowych w procesie produkcyjnym i magazynowym?")
        return []

class ActionProcessAnswer15(Action):
    def name(self) -> str:
        return "action_process_answer_15"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie działania podejmowane są w celu minimalizacji strat materiałowych w procesie produkcyjnym i magazynowym?"
        dispatcher.utter_message(text=response)
        return []       
    
class ActionAskQuestion16(Action):
    def name(self) -> str:
        return "action_ask_question_16"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak firma reaguje na zmiany technologiczne i innowacje w celu poprawy wydajności i konkurencyjności?")
        return []

class ActionProcessAnswer16(Action):
    def name(self) -> str:
        return "action_process_answer_16"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jak firma reaguje na zmiany technologiczne i innowacje w celu poprawy wydajności i konkurencyjności?"
        dispatcher.utter_message(text=response)
        return []    
    
class ActionAskQuestion17(Action):
    def name(self) -> str:
        return "action_ask_question_17"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie są procedury zapewnienia jakości wyrobów na każdym etapie produkcji i magazynowania?")
        return []

class ActionProcessAnswer17(Action):
    def name(self) -> str:
        return "action_process_answer_17"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie są procedury zapewnienia jakości wyrobów na każdym etapie produkcji i magazynowania?"
        dispatcher.utter_message(text=response)
        return []        
    
class ActionAskQuestion18(Action):
    def name(self) -> str:
        return "action_ask_question_18"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jakie są procedury zarządzania ryzykiem w obszarze produkcji i magazynowania, i jak są one wdrażane?")
        return []

class ActionProcessAnswer18(Action):
    def name(self) -> str:
        return "action_process_answer_18"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jakie są procedury zarządzania ryzykiem w obszarze produkcji i magazynowania, i jak są one wdrażane?"
        dispatcher.utter_message(text=response)
        return []            
    
class ActionAskQuestion19(Action):
    def name(self) -> str:
        return "action_ask_question_19"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jak firma minimalizuje wpływ zmiany dostawców na ciągłość produkcji?")
        return []

class ActionProcessAnswer19(Action):
    def name(self) -> str:
        return "action_process_answer_19"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response = tracker.latest_message['text']
        response = f"Jak firma minimalizuje wpływ zmiany dostawców na ciągłość produkcji?"
        dispatcher.utter_message(text=response)
        return []      