from listing import messageList

class Message(object):
    """Message object for Parsing articles from an email

    Parameters
    ----------
        message_obj : email dictionary

    """
    __slots__ = ('ID', 'Date', 'marr')

    def __init__(self, message_obj):
        self.ID = message_obj['id']
        self.Date = datetime.datetime.fromtimestamp(
            int(message_obj['internalDate'])/1000.0
        )
        mess = message_from_bytes(
            urlsafe_b64decode(message_obj['raw'].encode('ASCII'))
        )
        self.marr = np.array(mess.as_string().splitlines())

   
