# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
from secret import sms_SID,sms_token
from secret import elijsha,rendell,kaivan,twillonumber

# the following line needs your Twilio Account SID and Auth Token
client = Client(sms_SID, sms_token)

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to=rendell,
                       from_=twillonumber,
                       body="Hello from Python!")
