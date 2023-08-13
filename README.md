# IT Support System Chatbot

A conversational AI chatbot built with Rasa to provide IT support to users.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Training](#training)
  - [Running the Chatbot](#running-the-chatbot)
- [Functionalities](#functionalities)
  - [Supported Intents](#supported-intents)


## Introduction

The IT Support System Chatbot is designed to assist users with their IT-related issues and inquiries through natural language conversations. It leverages Rasa, a powerful open-source conversational AI framework, to provide quick and efficient support to users.

## Getting Started

Get started with the IT Support System Chatbot by following these steps.

### Prerequisites

- Python 3.7 or higher
- Rasa 



### Installation
pip install -r requirements.txt

### Usage
Learn how to use and interact with the IT Support System Chatbot.

### Training
Train the Rasa models for the chatbot using annotated data. Annotate conversations, intents, and entities, and then run:

rasa train

### Running the Chatbot
Start the chatbot interaction in the command line:

rasa shell

In order to run the actions.py file, open the cmd or anaconda prompt:

rasa run actions

Both of the above mentioned commands must be executed simultaneously in order to obtain the desired output.

The command to permits external applications or platforms to interact with the Rasa chatbot's API, making it accessible for integration into various front-end interfaces or other GUI is:
rasa run -m models --enable-api --cors "*"

### functionalities

Let's delve into the features provided by the IT Support System Chatbot.

# supported-intents

<ul>
reset_password
password_req
unlock_acnt
request_folder_access
transfer_account
create_new_user_account
report_unauthorized_access
troubleshoot_application_access
update_contact_information
wifi_problems
vpn_connection
internet_troubleshooting

</ul>

For more info please refer the official rasa docs
https://rasa.com/docs/rasa/


