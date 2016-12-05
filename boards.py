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


parser = argparse.ArgumentParser(description='Trello boards.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--org', type=str, 
                    help='Name of org', 
                    default='udemy')
parser.add_argument('--namePattern', type=str, 
                    help='Board name pattern', 
                    default='Engineering') 
parser.add_argument('--countLists', action='store_true', 
                    help='Count numner of lists on each board', 
                    default=False)
parser.add_argument('--lists', action='store_true', 
                    help='Display lists for each board', 
                    default=False)

args = parser.parse_args()

keys = yaml.load(open("keys.yml", 'r'))
key= keys['Key']
token = keys['Secret']
org=urllib.quote(args.org)

t = Template('https://api.trello.com/1/organizations/$org/boards?filter=open&key=$key&token=$token')

url = t.substitute(key=key, token=token, org=org)

r = requests.get(url)

t = Template('https://api.trello.com/1/boards/$board/lists?filter=open&cards=open&card_fields=name&key=$key&token=$token')

total = 0

for board in r.json():
    name = board['name']
    if not re.search(args.namePattern, name):
        continue

    print unicode(name).encode('utf8'), board['id'], board['shortLink']

    url = t.substitute(key=key, token=token, board=board['shortLink'])
    r = requests.get(url)
    lists = r.json()
    count = 0
    for list in lists:
        num = len(list['cards'])
        count += num
        print '\t', list['name'] + ' (' + str(num) + ')'

    print '\tTotal: ' + str(count)
    total += count

print '\tGrand total: ' + str(total)

