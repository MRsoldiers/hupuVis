import jieba
jieba.load_userdict('./data/dict.txt')
import jieba.posseg as pseg

class MyJieba():
  def __init__(self, textCollection):
    self.textCollection = textCollection
    self.words = []
    self.frequencyDict = {}
    self.frequency = []
  
  def parse(self):
    words = pseg.cut(self.textCollection)
    newWords = []
    for word,flag in words:
      # if (flag == 'x' or flag == 'y' or flag == 'o' or flag == 'c' or flag == 'cc' or flag == 'ul' or flag == 'uj' or flag == 'c' or flag == 'd' or flag == 'f' or flag == 'z')):
      #   continue
      # else:
      #   newWords.append(word)
      if flag == 'n' or flag == 'a':
        newWords.append(word)
    newText = ''.join(newWords)
    self.words = jieba.cut(newText, cut_all=True)

  def calculateFrequency(self):
    for word in self.words:
      if word not in self.frequencyDict:
        self.frequencyDict[word] = 1
      else:
        self.frequencyDict[word] += 1
    wordsList = []
    for key in self.frequencyDict:
      wordsList.append([key, self.frequencyDict[key]])

    self.frequency = sorted(wordsList, key=lambda w: w[1])
    
  def getFrequency(self):
    return self.frequency
  
  def getWords(self):
    return self.words

  def workerPipeline(self):
    self.parse()
    self.calculateFrequency()
    return self.frequency