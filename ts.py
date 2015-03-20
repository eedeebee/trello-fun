#!/usr/local/bin/python 

import json
import requests
import urllib
from string import Template


key='00018fcfa04e7a44db89b65ff9a4c7b2'
token='80cd8c6430aa41fefb0e60f1cad2bd73aa53ee4116108676fd5e45dda418fd77'
days=30
board=urllib.quote("Engineering: Team Web App")

t = Template('https://trello.com/1/search?key=$key&token=$token&query=board%3A"$board"%20created%3A$days%20label%3Abug&modelTypes=cards&card_fields=name,url,short_url&cards_limit=1000')

url = t.substitute(key=key, token=token, days=days, board=board)

r = requests.get(url)

for card in r.json()['cards'] :
    print card['name'], ',', card['url']

