from twilio.rest import TwilioRestClient

#account_sid = "{ACa47f1775cfcac1b4e91afe0a233dbebc}" # Your Account SID from www.twilio.com/console
#auth_token  = "{f09ba7280486a5c2c4052d92bb226c82}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient()

message = client.messages.create(body="Hello from Python",
    to="+14042728020",    # Replace with your phone number
    from_="+14044187863") # Replace with your Twilio number

print(message.sid)
