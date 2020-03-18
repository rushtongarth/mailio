#!/usr/bin/env python
import argparse
import datetime
from src.out.send import MailOutput

parser = argparse.ArgumentParser('Send emails')
parser.add_argument('-c', '--creds', nargs=1,help="credentials file")


def digest_prep(testing=False):
    rightnow = datetime.datetime.now()
    fulltime = rightnow.strftime('%Y-%m-%d %H:%M:%S.%f')
    just_day = rightnow.strftime('%Y-%m-%d')
    
    if testing:
        subj = 'Testing %s'%(fulltime)
    else:
        subj = 'ArXiV Digest %s'%(just_day)

if __name__ == '__main__':
    out = MailOutput()
