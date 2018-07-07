#coding=utf-8
import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open('./data/hupu.json','r') as load_f:
  cards = json.load(load_f)

# data = json.dumps(cards, indent=4).decode('unicode_escape')

for card in cards:
  hotposts = card['hotposts']
  for p in hotposts:
    if p.find('"') > -1:
      print('quote')
      p.replace('"', '+')
      print(p.find('+'))

# card = cards[0]
# hotposts = card['hotposts']
# res = json.dumps(hotposts, indent=4).decode('unicode_escape')
# print(res)

# print(data)