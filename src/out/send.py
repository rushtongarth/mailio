from base64 import urlsafe_b64encode
from email.mime.text import MIMEText
from src import GoogleObj

class Sender(GoogleObj):
    def __init__(self, creds, **kwargs):
        super().__init__(creds, **kwargs)
        self._body = ''
        self._to = ''
        self._from = ''

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, value):
        self._body = value
    @body.deleter
    def body(self):
        del self._body

    def __call__(self, subject, body, mess_to, mess_from):
        message = MIMEText(body, 'html')
        message['to'] = mess_to
        message['from'] = mess_from
        message['subject'] = subject
        mstr = message.as_bytes()
        msg = dict(raw=urlsafe_b64encode(mstr).decode())
        gmess = self.service.users().messages()
        try:
            tosend = gmess.send(userId=self.user, body=msg).execute()
            return tosend
        except Exception as E:
            raise E
