# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from socket import create_connection
from typing import Any, Text, Dict, List
from xmlrpc.client import Error
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3


#PREPEI NA KANOYME POLLA ACTIONS AKOMA POU THA NAI GIA ANAZHTHSEIS ME KATHE STHLH 
#DHLADH GIA KATHE STHLH MIA IDEA EINAI NA FTIAKSOUME KAI APO ENA ACTION
#OPOY GIA KATHENA APO AUTA THA KANOYME ENTINIES STO NLU 
#KKAI SO DOMAIN THA TA DHLWNOUME KAI HA KANOYME SLOTS

#EPISHS AUTH THN SUNARTHSH LEW NA THN BALOUME KAPOU EKTOS THS KLASHS
#EFOSON OLES OI KLASEIS AUTHN THN SUNARTHSH THA XRHSIMOPOIOUN
#KAI NA THN KANOUME STATIC GIA NA THN BLEPOUN OLES

class ActionSearchPlayBasedAuthor(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh author

    def name(self) -> Text:
        return "action_search_play_based_author"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="author"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("theatrical_writer"),None)
        print("i am on author play action")
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []


class ActionSearchPlayBasedId(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh id
    def name(self) -> Text:
        return "action_search_play_based_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="id"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("id_play"),None)
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        print("i am on id play action")
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []

class ActionSearchPlayBasedTranslator(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh translator
    def name(self) -> Text:
        return "action_search_play_based_translator"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="translator"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("translator"),None)
        print("i am on translator play action")
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []


        
class ActionSearchPlayBasedType(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh type
    def name(self) -> Text:
        return "action_search_play_based_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="type"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("type"),None)
        print("i am on type play action")
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []  

class ActionSearchPlayBasedTitle(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh title
    def name(self) -> Text:
        return "action_search_play_based_title"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        print("i am on play based title action")
        slot_name_parastaseis="title"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("title"),None)
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []   


class ActionSearchPlayBasedYearOfWriting(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh year_of_writing
    def name(self) -> Text:
        return "action_search_play_based_year_of_writing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="year_of_writing"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("year_of_writing"),None)
        print("i am on year of writing play action")
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []    

class ActionSearchPlayBasedPlace(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh year_of_writing
    def name(self) -> Text:
        return "action_search_play_based_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="place"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("place"),None)
        print("i am on place play action")
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []    

class ActionSearchPlayBasedDirection(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh year_of_writing
    def name(self) -> Text:
        return "action_search_play_based_direction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="direction"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("direction"),None)
        print("i am on direction play action")
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return [] 


class ActionSearchPlayBasedYearPlayed(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh year_of_writing
    def name(self) -> Text:
        return "action_search_play_based_year_played"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="year_played"
        print(" i am on year_played action")
        slot_value_parastaseis= next(tracker.get_latest_entity_values("year_played"),None)
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return [] 







#proswpa
class ActionSearchProswpaBasedRole(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me ta
#  proswpa me bash thn sthlh role
    def name(self) -> Text:
        return "action_search_proswpa_based_role"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_proswpa="role"
        print("i am on role proswpa action")
        slot_value_proswpa= next(tracker.get_latest_entity_values("role"),None)
        get_query_results_proswpa = MyFunctions.select_by_slot_proswpa(MyFunctions,conn, slot_name_proswpa, slot_value_proswpa)
        dispatcher.utter_message(text= get_query_results_proswpa)   
        return [] 

class ActionSearchProswpaBasedFullname(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me ta
#  proswpa me bash thn sthlh fullname
    def name(self) -> Text:
        return "action_search_proswpa_based_fullname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_proswpa="fullname"
        print("i am on fullname  proswpa action")
        slot_value_proswpa= next(tracker.get_latest_entity_values("fullname"),None)
        get_query_results_proswpa = MyFunctions.select_by_slot_proswpa(MyFunctions,conn, slot_name_proswpa, slot_value_proswpa)
        dispatcher.utter_message(text= get_query_results_proswpa)   
        return []

class ActionSearchProswpaBasedBirthday(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me ta
#  proswpa me bash thn sthlh birthday
    def name(self) -> Text:
        return "action_search_proswpa_based_birthday"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        print("i am on birthday  proswpa action")
        slot_name_proswpa="birthday"
        slot_value_proswpa= next(tracker.get_latest_entity_values("birthday"),None)
        get_query_results_proswpa = MyFunctions.select_by_slot_proswpa(MyFunctions,conn, slot_name_proswpa, slot_value_proswpa)
        dispatcher.utter_message(text= get_query_results_proswpa)   
        return [] 

        
class ActionSearchproswpaBasedDied(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me ta
#  proswpa me bash thn sthlh died
    def name(self) -> Text:
        return "action_search_proswpa_based_died"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_proswpa="died"
        print("i am on died  proswpa action")
        slot_value_proswpa= next(tracker.get_latest_entity_values("died"),None)
        get_query_results_proswpa = MyFunctions.select_by_slot_proswpa(MyFunctions,conn, slot_name_proswpa, slot_value_proswpa)
        dispatcher.utter_message(text= get_query_results_proswpa)   
        return [] 


class ActionSearchproswpaBasedId(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me ta
#  proswpa me bash thn sthlh died
    def name(self) -> Text:
        return "action_search_proswpa_based_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_proswpa="ID"
        print("i am on id  proswpa action")
        slot_value_proswpa= next(tracker.get_latest_entity_values("id"),None)
        get_query_results_proswpa = MyFunctions.select_by_slot_proswpa(MyFunctions,conn, slot_name_proswpa, slot_value_proswpa)
        dispatcher.utter_message(text= get_query_results_proswpa)   
        return [] 


class MyFunctions():
    @staticmethod
    def select_by_slot_parastaseis(self,conn, slot_name, slot_value):
        cur = conn.cursor()
        results= ""
        cur.execute(f"""SELECT * FROM parastaseis
                WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return "Δεν βρεθηκε κατι στην βάση μας.Προσπαθήστε ξανά!"
        else:
            for row in rows:
                results= results + (f"ID: {row[0]},\nΌνομα Παράστασης: {row[1]},\nΕίδος: {row[2]},\nΕτος συγγραφής: {row[3]},\nΣκηνή: {row[4]},\nΣυγγραφέας: {row[5]},\nΜετάφραση:{row[6]},\nΣκηνοθεσία:{row[7]},\nΈτος Παραστάσεων: {row[8]}\n\n")
            return results   


    @staticmethod
    def create_connection(self,db_file):
        conn = None
        try:
            conn = sqlite3.connect(f'{db_file}')
        except Error as e:
            print(e)
        return conn

  

    @staticmethod
    def select_by_slot_proswpa(self,conn, slot_name, slot_value):
        cur = conn.cursor()
        results= ""
        cur.execute(f"""SELECT * FROM proswpa
             WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return "Δεν βρεθηκε κατι στην βάση μας.Προσπαθήστε ξανά!"
        else:
            for row in rows:
                results= results + (f"ID:{row[0]},\nΟνοματεπώνυμο: {row[1]},\nΙδιότητα: {row[2]},\nΗμερομηνία Γέννησης: {row[3]},\nΗμερομηνία Θανάτου: {row[4]},\nIDParastasewn που έχει λάβει μέρος: {row[5]}\n\n")
            return results  