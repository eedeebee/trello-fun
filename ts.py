#!/usr/local/bin/python 

import argparse
import csv
import json
import requests
import urllib
import sys
import yaml

from string import Template


parser = argparse.ArgumentParser(description='Trello search tool.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--board', type=str, 
                    help='Name of board', 
                    default='Engineering: Team Web App')
parser.add_argument('--days', type=int, 
                    help='Number of days of history to search', 
                    default=14)
# FIXME: ArgumentDefaultsHelpParser doesn't do a nice job with sys.stdout arg
parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'),
                    help="Output file",
                    default=sys.stdout)

args = parser.parse_args()

keys = yaml.load(open("keys.yml", 'r'))
key= keys['Key']
token = keys['Secret']
days=args.days
board=urllib.quote(args.board)

print 'Searching' + ' "' + args.board + '" ' + str(days) + ' days back'

t = Template('https://trello.com/1/search?key=$key&token=$token&query=board%3A"$board"%20created%3A$days%20label%3Abug&modelTypes=cards&card_fields=idShort,name,closed,url,shortUrl&cards_limit=1000')

url = t.substitute(key=key, token=token, days=days, board=board)

r = requests.get(url)

with args.outfile as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for card in r.json()['cards'] :
        c = []
        for key, value in card.iteritems():
            c.append(value)
        writer.writerow(c)

