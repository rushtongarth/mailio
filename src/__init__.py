import pickle as pkl
from googleapiclient.discovery import build


class GoogleObj(object):
    def __init__(self, credentials, **kwargs):
        self.creds = credentials
        self.query = kwargs.get('query', [])
        self.user = "me"

    @property
    def service(self):
        with open(self.creds, 'rb') as f:
            creds = pkl.load(f)
        return build('gmail', 'v1', credentials=creds)

    @property
    def query(self):
        return self.qstr

    @query.setter
    def query(self, value):
        self.qstr = " ".join(value)

    @property
    def messages(self):
        return self.service.users().messages() 