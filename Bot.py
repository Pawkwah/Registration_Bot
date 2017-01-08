#!/usr/bin/env python3

from twilio.rest import TwilioRestClient
import requests
from bs4 import BeautifulSoup

url = "https://ungssb.ung.edu/pls/ungprod/bwckschd.p_disp_detail_sched?term_in=201702&crn_in=1174"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

table = soup.find(text="Seats").findNext('td').findNext('td').findNext('td').contents[0]

if int(table) > 0:
	account_sid = "ACa47f1775cfcac1b4e91afe0a233dbebc" # Your Account SID from www.twilio.com/console
	auth_token  = "f09ba7280486a5c2c4052d92bb226c82"  # Your Auth Token from www.twilio.com/console

	client = TwilioRestClient(account_sid, auth_token)
	message = "There are " + table + " seats open."
	message = client.messages.create(body=message,
   	to="+14042728020",    # Replace with your phone number
    	from_="+14044187863") # Replace with your Twilio number	

