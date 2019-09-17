# Kaivan Taylor
# Uses twillo API to send a message to desired contacts

from twilio.rest import Client
from secret import sms_SID,sms_token
from secret import elijsha,rendell,kaivan,twillonumber

def message(message):
    client = Client(sms_SID, sms_token)

    client.messages.create(to=kaivan,
                           from_=twillonumber,
                           body=message)

    client.messages.create(to=elijsha,
                           from_=twillonumber,
                           body=message)
