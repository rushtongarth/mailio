from base64 import urlsafe_b64encode
from email.mime.text import MIMEText
from src import GoogleObj

class MailOutput(GoogleObj):
    def __init__(self, creds, **kwargs):
        self.body = kwargs.pop("body", "")
        self.recipient = kwargs.pop("recipient", "")
        self.sender = kwargs.pop("sender", "")
        super().__init__(creds, **kwargs)

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

    def __call__(self, subject=None, **kwargs):
        
        self.body = kwargs.pop("body", self.body)
        self.recipient = kwargs.pop("recipient", self.recipient)
        self.sender = kwargs.pop("sender", self.sender)
        message = MIMEText(self.body, 'html')
        message['to'] = self.recipient
        message['from'] = self.sender
        message['subject'] = subject or 'Test'
        mstr = message.as_bytes()
        msg = dict(raw=urlsafe_b64encode(mstr).decode())
        gmess = self.service.users().messages()
        try:
            tosend = gmess.send(userId=self.user, body=msg).execute()
            return tosend
        except Exception as E:
            raise E
