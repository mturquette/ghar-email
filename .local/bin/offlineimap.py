#!/usr/bin/python
import re, subprocess

def decrypt_passwd(account=None):
    command = "/usr/bin/pass %s/imap" % account
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    return output
