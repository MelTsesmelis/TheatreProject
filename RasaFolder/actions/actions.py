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

class ActionTellparastaseis(Action):
 #Me ayto to action sthn ousia twra mporoume na kanoyme anazhthsh sto pinaka me tis 
 # parastaseis me bash thn sthlh suggrafeas

    def name(self) -> Text:
        return "action_tell_parastaseis"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        conn= self.create_connection('theatre.sqlite')
        conn2= self.create_connection('theatre.sqlite')

        slot_name_parastaseis="Συγγραφέας"
        # slot_value_parastaseis="Γουίλιαμ Σαίξπηρ"
        slot_value_parastaseis= next(tracker.get_latest_entity_values("theatrical_writer"),None)
        get_query_results_parastaseis = self.select_by_slot_parastaseis(conn, slot_name_parastaseis, slot_value_parastaseis)
        dispatcher.utter_message(text= get_query_results_parastaseis)   

        slot_name_parastaseis2="Μετάφραση"
        # slot_value_parastaseis="Λεωνίδας Καρατζάς"
        slot_value_parastaseis2= next(tracker.get_latest_entity_values("translator"),None)
        get_query_results_parastaseis2 = self.select_by_slot_parastaseis2(conn2, slot_name_parastaseis2, slot_value_parastaseis2)
        dispatcher.utter_message(text2= get_query_results_parastaseis2)

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
        return []

   
    def select_by_slot_parastaseis(self,conn, slot_name, slot_value):
        cur = conn.cursor()
        results= ""
        cur.execute(f"""SELECT * FROM parastaseis
                WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return[("There are no resources matching your query.")]
        else:
            for row in rows:
                results= results + (f"\tΌνομα Παράστασης: {row[1]},\n\tΕίδος: {row[2]},\n\tΕτος συγγραφής: {row[3]},\n\tΣκηνή: {row[4]},\n\tΣυγγραφέας: {row[5]},\n\tΜετάφραση:{row[6]},\n\tΣκηνοθεσία:{row[7]},\n\tΈτος Παραστάσεων: {row[8]}\n\n")
        return results   


    def select_by_slot_parastaseis2(self,conn2, slot_name2, slot_value2):
        cur = conn2.cursor()
        results2= ""
        cur.execute(f"""SELECT * FROM parastaseis
                WHERE {slot_name2}='{slot_value2}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return[("There are no resources matching your query.")]
        else:
            for row in rows:
                results2= results2 + (f"\tΌνομα Παράστασης: {row[1]},\n\tΕίδος: {row[2]},\n\tΕτος συγγραφής: {row[3]},\n\tΣκηνή: {row[4]},\n\tΣυγγραφέας: {row[5]},\n\tΜετάφραση:{row[6]},\n\tΣκηνοθεσία:{row[7]},\n\tΈτος Παραστάσεων: {row[8]}\n\n")
        return results2

    
        

    def create_connection(self,db_file):
        conn = None
        print(db_file)
        try:
            conn = sqlite3.connect(f'{db_file}')
            print(conn)
        except Error as e:
            print(e)
        return conn

    def create_connection2(self,db_file2):
        conn2 = None
        print(db_file)
        try:
            conn2 = sqlite3.connect(f'{db_file2}')
            print(conn2)
        except Error as e:
            print(e)
        return conn2    

   
    def select_by_slot_proswpa(self,conn, slot_name, slot_value):
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM proswpa
                WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return[("There are no resources matching your query.")]
        else:
            for row in rows:
                return[print(f"\tID:{row[0]},\n\tΟνοματεπώνυμο: {row[1]},\n\tΙδιότητα: {row[2]},\n\tΗμερομηνία Γέννησης: {row[3]},\n\tΗμερομηνία Θανάτου: {row[4]},\n\tIDParastasewn που έχει λάβει μέρος: {row[5]}\n\n")]
        return []