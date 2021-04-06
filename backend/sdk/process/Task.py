from jieba import load_userdict, analyse, cut
from snownlp import SnowNLP
import os

tfidf = analyse.extract_tags
dirName = os.path.dirname(os.path.realpath(__file__))

stopwords = {}.fromkeys([line.rstrip()
                         for line in open(dirName + '\\Stopword.txt', encoding='utf-8')])

def init():
    print("====================================")
    print("=           Loading...             =")
    print("====================================")
    load_userdict(dirName + "\\SogouLabDic.txt")
    load_userdict(dirName + "\\dict_baidu_utf8.txt")
    load_userdict(dirName + "\\dict_pangu.txt")
    load_userdict(dirName + "\\dict_sougou_utf8.txt")
    load_userdict(dirName + "\\dict_tencent_utf8.txt")
    load_userdict(dirName + "\\my_dict.txt")
    print("====================================")
    print("=              Done.               =")
    print("====================================")


class Task:
    def __init__(self):
        self.data = ''
        self.pos = 0
        self.neg = 0

    def append(self, text):
        seg = cut(text)
        tmp = ''
        for i in seg:
            if i not in stopwords:
                tmp += i + " "

        keywords = tfidf(tmp, allowPOS=('ns', 'nr', 'nt', 'nz',
                                        'nl', 'n', 'vn', 'vd', 'vg', 'v', 'vf', 'a', 'an', 'i'))

        tmp = ''
        for keyword in keywords:
            if SnowNLP(keyword).sentiments >= 0.5:
                self.pos += 1
            else:
                self.neg += 1
            tmp += keyword + " "

        self.data += tmp + "\n"

    def process(self):
        result1 = analyse.textrank(self.data, topK=50, withWeight=True)
        result2 = {
            "pos": self.pos,
            "neg": self.neg
        }
        return {
            "rank": result1,
            "nlp": result2
        }
