import os
import random
import math

stopwords = open('stopwords_vn.txt','r', encoding="utf-8").read()
marks = ('.',',',';',':','/','?','!','@','(',')','"','-','_','--','*','=', '+', '&', '-', '"', '%')
allfiles = os.listdir('dataset')
len_files = len(allfiles)
dictionary = []
strr = {}
file = {}
i = 0
for each_file in allfiles:
    file[i] = open("dataset\\" + each_file, 'r', encoding="utf_16")
    strr[i] = file[i].read()
    for a in marks:
        strr[i] = strr[i].replace(a, '')
    string = strr[i].split()
    
    string = [word.lower() for word in string]
    
    string = [word for word in string if word not in stopwords]
    strr[i] = ' '.join(string)
    
    for vocabulary in string:
        if vocabulary not in dictionary:
            dictionary += [vocabulary]
    file[i].close()
    i = i + 1
    if i == len_files:
        break

for vocabulary in dictionary:
    t = vocabulary + '.txt'
    f = open('indexing\\' + t, 'w+', encoding='utf_8')

    for i in range(len_files):
        if vocabulary in strr[i].split():
            tf = 1 + math.log10(strr[i].count(vocabulary))
            doc_tf = str(i) + ' ' + str(tf) +'\n'
            f.write(doc_tf)
    f.close()
