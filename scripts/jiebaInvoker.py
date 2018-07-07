from myJieba import MyJieba


if __name__ == "__main__":
  with open('./data/nbaTest.txt','r') as f:
    ftext = f.read()
    jieba = MyJieba(ftext)
    words = jieba.workerPipeline()
    # jieba.parse()
    # jieba.calculateFrequency()
    # words = jieba.getFrequency()

    print(words)
    
