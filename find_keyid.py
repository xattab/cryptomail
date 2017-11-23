#!/usr/bin/env python

import gnupg
from pprint import pprint
gpg = gnupg.GPG(homedir='~/.gnupg')

#keys = gpg.list_keys()
#for key in keys:
#    for uid in key['uids']:
#        print uid


public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)
print 'public keys:'
pprint(public_keys)
print 'private keys:'
pprint(private_keys)
