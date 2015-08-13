#!/usr/local/bin/python 

import argparse
import csv
import json
import requests
import urllib
import re
import sys
import yaml

from string import Template


parser = argparse.ArgumentParser(description='Trello board membership tool.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--dryrun', action='store_true', 
                    help='Just list the users', 
                    default=False)
parser.add_argument('--member', type=str, 
                    help='Member name', 
                    default='ebloch') 
parser.add_argument('--org', type=str, 
                    help='Organization name', 
                    default='udemy') 
parser.add_argument('--namePattern', type=str, 
                    help='Board name pattern', 
                    default='Engineering') 
parser.add_argument('--role', type=str, 
                    help='Role (normal or admin)', 
                    default='normal') 


args = parser.parse_args()


keys = yaml.load(open("keys.yml", 'r'))
key= keys['Key']
secret = keys['Secret']
token = keys['Token']
member=urllib.quote(args.member)
org=urllib.quote(args.org) 
role=urllib.quote(args.role)

print 'Adding member ' + ' "' + args.member + '" to organization ' + args.org + ' boards "'

t = Template('https://api.trello.com/1/organizations/$org/boards/?filter=organization&fields=name&key=$key&token=$token')
url = t.substitute(org=org, key=key, token=secret)
boards = requests.get(url).json()

t = Template('https://api.trello.com/1/members/$member/?&fields=name&key=$key&token=$token')
url = t.substitute(member=member, key=key, token=secret)
member = requests.get(url).json()

print "Member ID " + member['id']

print 'Boards'
for board in boards:
    name = board[u'name']
    id = board[u'id']

    if not re.search(args.namePattern, name):
        continue

    print ' ' + name

    if args.dryrun:
        continue

    t = Template('https://api.trello.com/1/board/$boardID/members/$member?key=$key&token=$token&type=admin')
    url = t.substitute(key=key, token=token, boardID=id, member=member[u'id'])

    print url

    r = requests.put(url)
    if r.status_code != 200:
        print r
        sys.exit

