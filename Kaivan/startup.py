# Source: https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873
# Getting familiar with fitbit API
# Kaivan Taylor

import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

CLIENT_ID = '22B4RG'
CLIENT_SECRET = 'c511ebbf0974a6a69516919bae59b33f'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
