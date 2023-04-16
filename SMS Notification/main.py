from email.message import Message
import os
from twilio.rest import Client
import time

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC3a0df76dc1bb5391ee83aade94166aae'
auth_token = '2d6d4c2a2eeba8aeb45635ee2c4890aa'
client = Client(account_sid, auth_token)

cnt = 0

while cnt < 10:

    message = client.messages \
        .create(
            body='TEST',
            from_='+19853322427',
            # to='+381 65 8736021'
            to='+381 62 9627872'
        )

    print(message.sid)

    cnt = cnt + 1

    time.sleep(5)