#!/usr/bin/python
import re, subprocess

def decrypt_passwd(account=None):
    command = "/usr/local/bin/pass %s" % account
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    return output
