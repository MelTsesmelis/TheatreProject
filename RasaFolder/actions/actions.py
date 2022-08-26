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
import arrow

#PREPEI NA KANOYME POLLA ACTIONS AKOMA POU THA NAI GIA ANAZHTHSEIS ME KATHE STHLH 
#DHLADH GIA KATHE STHLH MIA IDEA EINAI NA FTIAKSOUME KAI APO ENA ACTION
#OPOY GIA KATHENA APO AUTA THA KANOYME ENTINIES STO NLU 
#KKAI SO DOMAIN THA TA DHLWNOUME KAI HA KANOYME SLOTS

#EPISHS AUTH THN SUNARTHSH LEW NA THN BALOUME KAPOU EKTOS THS KLASHS
#EFOSON OLES OI KLASEIS AUTHN THN SUNARTHSH THA XRHSIMOPOIOUN
#KAI NA THN KANOUME STATIC GIA NA THN BLEPOUN OLES

class ActionSearchPlayBasedAuthor(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh Author

    def name(self) -> Text:
        return "action_search_play_based_author"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="author"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("theatrical_writer"),None)
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []


class ActionSearchPlayBasedId(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh ID
    def name(self) -> Text:
        return "action_search_play_based_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="id"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("id_play"),None)
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []

class ActionSearchPlayBasedTranslator(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh ID
    def name(self) -> Text:
        return "action_search_play_based_translator"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="translator"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("translator"),None)
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []


        
class ActionSearchPlayBasedType(Action):
#  Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
#  parastaseis me bash thn sthlh ID
    def name(self) -> Text:
        return "action_search_play_based_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn= MyFunctions.create_connection(MyFunctions,'theatre.sqlite')
        slot_name_parastaseis="type"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("kind"),None)
        get_query_results_parastaseis = MyFunctions.select_by_slot_parastaseis(MyFunctions,conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   
        return []        
    # slot_name_parastaseis="Μετάφραση"
        # # slot_value_parastaseis="Λεωνίδας Καρατζάς"
        # slot_value_parastaseis= next(tracker.get_latest_entity_values("translator"),None)
        # get_query_results_parastaseis = self.select_by_slot_parastaseis(conn, slot_name_parastaseis, slot_value_parastaseis)
        # dispatcher.utter_message(text= get_query_results_parastaseis)


        # current_theatrical_play = next(tracker.get_slot("theatrical_writer"), None)
        # utc = arrow.utcnow()

        # print(current_theatrical_play)
        # if not current_theatrical_play:
        #     msg = f"Με συγχωρείτε αλλά δεν βρίσκω τέτοια παράσταση.😁"
        #     dispatcher.utter_message(text=msg)
        #     return []

        
       
        # print(self.create_connection('../theatre_db/theatre.sqlite'))
        

        # res= select_by_slot_parastaseis(conn, slot_name, slot_value)
        
    
        
        # db_string_parastaseis = select_by_slot_parastaseis(conn, slot_name, slot_value) 

        # if not db_string_parastaseis:
        #     msg = f"Δεν μπορώ να βρω κάτι για {current_theatrical_play}. Το έχετε γράψει σωστά?"
        #     dispatcher.utter_message(text=msg)
        #     return []
        # conn = create_connection("../theatre_db/theatre.sqlite")
        # slot_name= "Συγγραφέας" #EDW THA PREPEI KAPWS NA PAIRNOUME ME BASH TO INPUT TOU XRHSTH 
        # slot_value= tracker.get_slot("resource_type") 
       

        # slot_name_proswpa="ID"
        # slot_value_proswpa="1"
        # get_query_results_proswpa = self.select_by_slot_proswpa(conn, slot_name_proswpa, slot_value_proswpa)
        # dispatcher.utter_message(text= get_query_results_proswpa)
        # # return db_string_parastaseis
        


class MyFunctions():
    @staticmethod
    def select_by_slot_parastaseis(self,conn, slot_name, slot_value):
        cur = conn.cursor()
        results= "\t"
        cur.execute(f"""SELECT * FROM parastaseis
                WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return "Δεν βρεθηκε κατι στην βάση μας.Προσπαθήστε ξανά !"
        else:
            for row in rows:
                results= results + (f"\n\ID: {row[0]},\nΌνομα Παράστασης: {row[1]},\nΕίδος: {row[2]},\nΕτος συγγραφής: {row[3]},\nΣκηνή: {row[4]},\nΣυγγραφέας: {row[5]},\nΜετάφραση:{row[6]},\nΣκηνοθεσία:{row[7]},\nΈτος Παραστάσεων: {row[8]}\n\n")
            return results   


    @staticmethod
    def create_connection(self,db_file):
        conn = None
        try:
            conn = sqlite3.connect(f'{db_file}')
            print(conn)
        except Error as e:
            print(e)
        return conn

  

    @staticmethod
    def select_by_slot_proswpa(self,conn, slot_name, slot_value):
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM proswpa
             WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return "Δεν βρεθηκε κατι στην βάση μας.Προσπαθήστε ξανά!"
        else:
            for row in rows:
                return[print(f"\nID:{row[0]},\nΟνοματεπώνυμο: {row[1]},\nΙδιότητα: {row[2]},\nΗμερομηνία Γέννησης: {row[3]},\nΗμερομηνία Θανάτου: {row[4]},\nIDParastasewn που έχει λάβει μέρος: {row[5]}\n\n")]
        return []