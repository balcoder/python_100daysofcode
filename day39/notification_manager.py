''' class takes care of notifications using twilio '''
from twilio.rest import Client

class NotificationManager:
    '''This class is responsible for sending notifications with the deal flight details
        from twilio '''
    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token


    def send_sms(self, message):
        ''' use twilio to send sms text message '''        
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_='+15627413568',
            body=message,
            to='+353866067654'
            )
        print(message.status)
        