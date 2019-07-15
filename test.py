# _*_coding:utf-8_*_

from __future__ import print_function

import logging

from stanfordcorenlp import StanfordCoreNLP
#
# local_corenlp_path = r'G:/JavaLibraries/stanford-corenlp-full-2016-10-31/'
# local_corenlp_path = r'G:\JavaLibraries\stanford-corenlp-full-2017-06-09'
local_corenlp_path = '/home/390891/PycharmProjects/stanford-corenlp-master/stanford-corenlp-full-2018-10-05'
print(local_corenlp_path,"111111111111")
# local_corenlp_path = r'/home/gld/JavaLibs/stanford-corenlp-full-2016-10-31'

# Simple usage
nlp = StanfordCoreNLP(local_corenlp_path, quiet=False, logging_level=logging.DEBUG)
print(nlp)

sentence = 'Guangdong University of Foreign Studies (GDUFS) is located in Guangzhou.'
#print('Tokenize:', nlp.word_tokenize(sentence))
#print('Part of Speech:', nlp.pos_tag(sentence))
#print('Named Entities:', nlp.ner(sentence))
print('Constituency Parsing:', nlp.parse(sentence))
print('Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close()



# from nltk.parse.stanford import StanfordDependencyParser
#
# eng_parser = StanfordDependencyParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
# res = list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split()))
# for row in res[0].triples():
#     print (row)

#%test upload
