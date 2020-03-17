#!/usr/bin/env python

import datetime
from src.out.send import MailOutput


def digest_prep(testing=False):
    today = str(datetime.date.today())
    rightnow = str(datetime.datetime.now())
    if testing:
        subj = 'Testing %s'%(rightnow)
    else:
        subj = 'ArXiV Digest %s'%(today)

if __name__ == '__main__':
    out = MailOutput()
