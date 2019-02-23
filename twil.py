# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC6f360c53ed36540386f12a136cf90075'
auth_token = 'fc6eb168bbf9038c10027d5847d9b2a5'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12023183287',
                     to='+919145581103'
                 )

print(message.sid)
