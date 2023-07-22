# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#

# class ActionHelloWorld(Action):
#     def name(self) -> Text:
#         return "action_hello_world"

#     print("hello in func")

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="raising a ticket !")

#         return []


class ActionGenerateRandomNumber(Action):
    def name(self) -> Text:
        return "action_generate_random_number"

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
        # message2 = f"Your ticket number is: {random_number}"

        # Sending the mail
        s.sendmail("chatbotjio@gmail.com", email_id, message)

        # Closing the connection
        s.quit()

        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

        return []


# class SendEmailAction(Action):
#     def name(self):
#         return "action_send_email"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         # Extract relevant information from the tracker
#         sender_email = "chatbotjio@gmail.com"  # Replace with your email address
#         sender_password = "jnebvajxyzhqihvr"  # Replace with your email password
#         receiver_email = (
#             "rao.harshitha04@gmail.com"  # Replace with the recipient's email address
#         )
#         subject = "Test Email"
#         message = "This is a test email sent through Rasa!{random_number}"

#         try:
#             # Set up the SMTP server
#             smtp_server = (
#                 "smtp.gmail.com"  # Change this if using a different email provider
#             )
#             smtp_port = 587  # Change this if using a different port

#             # Create a connection to the SMTP server
#             server = smtplib.SMTP(smtp_server, smtp_port)
#             server.starttls()

#             # Log in to your email account
#             server.login(sender_email, sender_password)

#             # Compose the email
#             msg = MIMEMultipart()
#             msg["From"] = sender_email
#             msg["To"] = receiver_email
#             msg["Subject"] = subject
#             msg.attach(MIMEText(message, "plain"))

#             # Send the email
#             server.sendmail(sender_email, receiver_email, msg.as_string())

#             # Close the connection to the SMTP server
#             server.quit()

#             # Send a response to the user indicating that the email was sent
#             dispatcher.utter_message("The email has been sent successfully.")

#         except Exception as e:
#             # Handle the exception if the email sending fails
#             dispatcher.utter_message("Oops! An error occurred while sending the email.")
#             print("An error occurred while sending the email:", e)

#         return []
