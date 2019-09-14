# # we import the Twilio client from the dependency we just installed
# from twilio.rest import Client
# from secret import sms_SID,sms_token
#
# # the following line needs your Twilio Account SID and Auth Token
# client = Client(sms_SID, sms_token)
#
# # change the "from_" number to your Twilio number and the "to" number
# # to the phone number you signed up for Twilio with, or upgrade your
# # account to send SMS to any phone number
# client.messages.create(to="+15714394213",
#                        from_="+16143680178",
#                        body="hi dad!")

from googlevoice import Voice
from googlevoice.util import input

voice = Voice()
voice.login()

phoneNumber = input('Number to send message to: ')
text = input('Message text: ')

voice.send_sms(phoneNumber, text)
