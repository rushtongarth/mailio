from base64 import urlsafe_b64encode
from email.mime.text import MIMEText
from src import GoogleObj

class MailOutput(GoogleObj):
    def __init__(self, creds, **kwargs):
        super().__init__(creds, **kwargs)
        self._body = ''
        self._recipient = ''
        self._sender = ''

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

    @body.deleter
    def body(self):
        del self._body

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, value):
        self._recipient = value

    @recipient.deleter
    def recipient(self):
        del self._recipient

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value

    @sender.deleter
    def sender(self):
        del self._sender

    def __call__(self, subject, body, recipient, sender):
        
        message = MIMEText(body, 'html')
        message['to'] = recipient
        message['from'] = sender
        message['subject'] = subject
        mstr = message.as_bytes()
        msg = dict(raw=urlsafe_b64encode(mstr).decode())
        gmess = self.service.users().messages()
        try:
            tosend = gmess.send(userId=self.user, body=msg).execute()
            return tosend
        except Exception as E:
            raise E
