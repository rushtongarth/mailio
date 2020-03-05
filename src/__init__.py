import pickle as pkl
import operator as op
import numpy as np
from googleapiclient.discovery import build


class GoogleObj(object):
    def __init__(self, credentials, **kwargs):
        qstr = " ".join([
            "from:no-reply@arxiv.org",
            "subject:(cs daily)",
        ])
        self.qstr = kwargs.get('query', qstr)
        self.user = "me"

    @property
    def service(self):
        with open(credentials, 'rb') as f:
            creds = pkl.load(f)
        return build('gmail', 'v1', credentials=creds) 
    @property
    def messages(self):
        return self.service.users().messages() 
