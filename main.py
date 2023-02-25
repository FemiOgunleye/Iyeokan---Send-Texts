import os
from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC9eedcb63eab86ced5a842a1289ebe00a'
auth_token = 'a3b934ec2ee15e8f95893953dd5478ef'

# Create a Twilio client object
client = Client(account_sid, auth_token)

# The phone number you want to send the message to
to_number = '+13202474299'

# The phone number associated with your Twilio account
from_number = '+17739006301'

# The text message content with editable information
message = 'Hello {name}, your appointmnet is tomorrow {date} at {time}.'

# The editable information to be replaced in the message
name = 'Iyeokan'
date = '02/25/2023'
time = '3:30PM'

# Replace the placeholders in the message with the actual information
message = message.format(name=name, date=date, time=time)

# Send the message using the Twilio client
message = client.messages.create(
    to=to_number,
    from_=from_number,
    body=message)

# Print the message SID to confirm it was sent
print(f'Message SID: {message.sid}')
