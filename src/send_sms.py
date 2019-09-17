# Kaivan Taylor
# Uses twillo API to send a message to desired contacts

from twilio.rest import Client
from secret import sms_SID,sms_token

def message(message, user): # requires string message and user's phone #
    client = Client(sms_SID, sms_token)
    client.messages.create(to=user,
                           from_=twillonumber,
                           body=message)
