# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted


class ActionHandleOptionA(Action):
    def name(self) -> Text:
        return "action_handle_option_a"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Perform actions related to Option A
        dispatcher.utter_message("I'm glad I could assist you. If you have more questions in the future, feel free to ask. Have a wonderful day ahead !")
        return []




class ActionHandleOptionB(Action):
    def name(self) -> Text:
        return "action_handle_option_b"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        random_number = random.randint(1000, 9999)
        dispatcher.utter_message(
            text=f"A ticket has been raised. Your ticket number is: {random_number}"
        )

        user_name = tracker.get_slot("name")
        email_id = tracker.get_slot("email")

        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP("smtp.gmail.com", 587)

        # Making connection secured
        s.starttls()

        # Authentication
        s.login("chatbotjio@gmail.com", "jnebvajxyzhqihvr")

        # Message to be sent
        print(random_number)
        message = (
            "Hello {} ,Your ticket has been raised and your ticket number is {}".format(
                user_name, random_number
            )
        )

        recipients = ['issuesvpn@gmail.com', email_id]

        # Sending the mail
        s.sendmail("chatbotjio@gmail.com", recipients, message)

        # Closing the connection
        s.quit()

        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []



class ActionHandleOptionWifi(Action):
    def name(self) -> Text:
        return "action_handle_option_wifi"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        random_number = random.randint(1000, 9999)
        dispatcher.utter_message(
            text=f"A ticket has been raised. Your ticket number is: {random_number}"
        )

        user_name = tracker.get_slot("name")  # Replace with your slot name
        email_id = tracker.get_slot("email")  # Replace with your slot name

        # Code to send email
        try:
            # Creating connection using smtplib module
            s = smtplib.SMTP("smtp.gmail.com", 587)

            # Making connection secured
            s.starttls()

            # Authentication
            s.login("chatbotjio@gmail.com", "jnebvajxyzhqihvr")

            # Message to be sent
            message = (
                f"Hello {user_name}, Your ticket has been raised and your ticket number is {random_number}"
            )

            recipients = ['issueswifi.jio@gmail.com', email_id]

            # Sending the mail
            s.sendmail("chatbotjio@gmail.com", recipients, message)

            # Closing the connection
            s.quit()

            # Confirmation message
            dispatcher.utter_message(text="Email has been sent.")
        except Exception as e:
            dispatcher.utter_message(text="An error occurred while sending the email.")
            print(e)

        return []
    
    



# from rasa_sdk.executor import CollectingDispatcher

# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("I'm sorry, I didn't understand. Can you please rephrase or provide more context?")
#         return []



# for future email trigerring 
# class ActionGenerateRandomNumberr(Action):
#     def name(self) -> Text:
#         return "action_generate_random_numberr"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         random_number = random.randint(1000, 9999)
#         dispatcher.utter_message(
#             text=f"A ticket has been raised. Your ticket number is: {random_number}"
#         )

#         user_name = tracker.get_slot("name")
#         email_id = tracker.get_slot("email")

#         # Code to send email
#         # Creating connection using smtplib module
#         s = smtplib.SMTP("smtp.gmail.com", 587)

#         # Making connection secured
#         s.starttls()

#         # Authentication
#         s.login("chatbotjio@gmail.com", "jnebvajxyzhqihvr")

#         # Message to be sent
#         print(random_number)
#         message = (
#             "Hello {} ,Your ticket has been raised and your ticket number is {}".format(
#                 user_name, random_number
#             )
#         )

#         recipients = ['issueswifi.jio@gmail.com', email_id]

#         # Sending the mail
#         s.sendmail("chatbotjio@gmail.com", recipients, message)

#         # Closing the connection
#         s.quit()

#         # Confirmation message
#         dispatcher.utter_message(text="Email has been sent.")
#         return []
    
