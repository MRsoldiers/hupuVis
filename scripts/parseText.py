#coding=utf-8
import re
import json
from myJieba import MyJieba
# import sys
# sys.setdefaultencoding('utf-8')

class HotpostsProcessor():
  clientPattern = re.compile(r"发自虎扑(\w*)客户端")

  def __init__(self, card):
    self.hotposts = card['hotposts']
    self.wellHotposts = []
    self.textCollection = ''

  def getWellHotposts(self):
    return self.wellHotposts

  def getTextCollection(self):
    return self.textCollection

  def delGeneralField(self, postSplit):
    del postSplit[6]
    del postSplit[6]
    del postSplit[6]
    del postSplit[6]
    del postSplit[2]
    del postSplit[2]
    del postSplit[3]

  def parseLastField(self, postSplit):
    lastField = str(postSplit[len(postSplit) -1])
    match = self.clientPattern.match(lastField)
    if match:
      del postSplit[len(postSplit) -1]
      return str(match.group(1))
    else:
      return 'web'

  def getNumberOfLike(self, postSplit):
    nLike = int(postSplit[0])
    del postSplit[0]
    return nLike

  def getAuthor(self, postSplit):
    author = str(postSplit[0])
    del postSplit[0]
    return author

  def getTime(self, postSplit):
    time = postSplit[0]
    del postSplit[0]
    return time

  def process(self):
    hotposts = []
    textCollection = ''
    for hp in self.hotposts:
      p = hp.replace('"', '+').replace('\\n', '')
      arr = p.split('|')
      self.exceptLouzhu(arr)
      self.delGeneralField(arr)
      post = {}
      post['clientAgent'] = self.parseLastField(arr)
      post['replier'] = self.getAuthor(arr)
      post['time'] = self.getTime(arr)
      post['nLike'] = self.getNumberOfLike(arr)
      post['postText'] = '|'.join(arr)
      hotposts.append(post)
      textCollection = textCollection + post['postText'] + '='
    self.wellHotposts = hotposts
    self.textCollection = textCollection

  def exceptLouzhu(self, postSplit):
    if str(postSplit[1]) == '楼主':
      del postSplit[1]

if __name__ == "__main__":
  with open('./data/hupu.json','r') as load_f:
    cards = json.load(load_f)

    data = []
    i = 0
    l = len(cards)
    for card in cards:
      print('processing card %s %s' % (i, l))
      i += 1
      hotpostsProcessor = HotpostsProcessor(card)
      hotpostsProcessor.process()
      card['wellHotpost'] = hotpostsProcessor.getWellHotposts()
      del card['hotposts']
      card['textCollection'] = hotpostsProcessor.getTextCollection()
      jieba = MyJieba(card['textCollection'])
      wordFrequency = jieba.workerPipeline()
      card['wordFrequency'] = wordFrequency
      data.append(card)

    fw = open('./data/hupu-wellpost-min.json', 'w')
    js_str = json.dumps(data, ensure_ascii=False)
    fw.write(js_str)
    fw.close()