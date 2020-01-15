# -*- coding: utf-8 -*-
from dataSet import *

# end = ['.', ';', '!', '...', '?']
# wh = [',', '[', ']', "'", '"', '-', '(', ')', ':', '“', '”']


hmm = HMM()


def test(sentence, types):
    pos = hmm.cal_hmm(sentence)
    i = 0
    exactly = 0
    for word in pos:
        if types[i] == word:
            exactly += 1
        i += 1
    print('========================================')
    print('Mau: ', types)
    print('KQ: ', pos)
    rate = exactly / len(types)
    print('Rate ', rate)
    print('========================================')
    return rate


pair_words = read_files(name='test')

max = len(pair_words)
isType = False

# pos = hmm.cal_hmm(words)
sentence = list()
types = list()

count = 0
rates = []
for pair in pair_words:
    word, type = list(pair.items())[0]
    if type in wh:
        continue
    if type in end:
        if len(sentence) < 1:
            continue
        rates.append(test(sentence, types))
        sentence.clear()
        types.clear()
        continue
    types.append(type)
    sentence.append(word)

print('sentence: ', len(rates))
print('Total: ', sum(rates) / len(rates))
