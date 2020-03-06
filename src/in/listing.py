from collections.abc import MutableSequence


class messageList(MutableSequence):
    def __init__(self,credentials, **kwargs):
        self.start = kwargs.pop('start',-1)
        self.end = kwargs.pop('end',0)
        self.count = kwargs.pop('count',self.end - self.start)
        super().__init__(credentials=credentials, **kwargs)
    
    def __len__(self):
        return self.count
    def __mids(self):
        """pull all message ids from email address"""
        messages = []
        kw = dict(userId=self.user, q=self.qstr)
        _msgs = self.msgs.list(**kw)
        msgs = _msgs.execute()
        if 'messages' in msgs:
            messages.extend(msgs['messages'])
        while 'nextPageToken' in msgs:
            kw['pageToken'] = msgs['nextPageToken']
            msgs = self.msgs.list(**kw).execute()
            messages.extend(msgs['messages'])
        ids = map(op.itemgetter('id'), messages)
        self._mids = np.fromiter(ids, dtype=(str, 16))

    @property
    def mids(self):
        if hasattr(self, '_mids'):
            self.__mids()
        return self._mids
