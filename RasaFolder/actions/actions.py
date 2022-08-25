# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from socket import create_connection
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import arrow


class ActionTellparastaseis(Action):

    def name(self) -> Text:
        return "action_tell_parastaseis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_theatrical_play = next(tracker.get_latest_entity_values("theatrical_plays"), None)
        utc = arrow.utcnow()

        if not current_theatrical_play:
            msg = f"Με συγχωρείτε αλλά δεν βρίσκω τέτοια παράσταση."
            dispatcher.utter_message(text=msg)
            return []

        slot_name="Συγγραφέας"
        slot_value="Γουίλιαμ Σαίξπηρ"
        db_string_parastaseis = select_by_slot_parastaseis(create_connection("../theatre_db/theatre.sqlite"),slot_name,slot_value) 

        if not db_string_parastaseis:
            msg = f"Δεν μπορώ να βρω κάτι για {current_theatrical_play}. Το έχετε γράψει σωστά?"
            dispatcher.utter_message(text=msg)
            return []
        # conn = create_connection("../theatre_db/theatre.sqlite")
        # slot_name= "Συγγραφέας" #EDW THA PREPEI KAPWS NA PAIRNOUME ME BASH TO INPUT TOU XRHSTH 
        # slot_value= tracker.get_slot("resource_type") 
        # get_query_results_parastaseis = select_by_slot_parastaseis(conn, slot_name, slot_value)
        # dispatcher.utter_message(text= get_query_results_parastaseis)
        # get_query_results_proswpa = select_by_slot_proswpa(conn, slot_name, slot_value)
        # dispatcher.utter_message(text= get_query_results_proswpa)
        return db_string_parastaseis

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def select_by_slot_parastaseis(conn, slot_name, slot_value):
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM parastaseis
                WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return[("There are no resources matching your query.")]
        else:
            for row in rows:
                return [print(f"\tΚωδικός Παράστασης:{row[0]},\n\tΌνομα Παράστασης: {row[1]},\n\tΕίδος: {row[2]},\n\tΕτος συγγραφής: {row[3]},\n\tΣκηνή: {row[4]},\n\tΣυγγραφέας: {row[5]},\n\tΜετάφραση:{row[6]},\n\tΣκηνοθεσία:{row[7]},\n\tΈτος Παραστάσεων: {row[8]}\n\n\n")]

    def select_by_slot_proswpa(conn, slot_name, slot_value):
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM proswpa
                WHERE {slot_name}='{slot_value}'""")
        rows = cur.fetchall()
        if len(list(rows)) < 1:
            return[("There are no resources matching your query.")]
        else:
            for row in rows:
                return[print(f"\tID:{row[0]},\n\tΟνοματεπώνυμο: {row[1]},\n\tΙδιότητα: {row[2]},\n\tΗμερομηνία Γέννησης: {row[3]},\n\tΗμερομηνία Θανάτου: {row[4]},\n\tIDParastasewn που έχει λάβει μέρος: {row[5]}\n\n\n")]
