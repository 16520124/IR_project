import os
import random
import math

allfiles = os.listdir('dataset')
num_docs = len(allfiles)
indexing = os.listdir('indexing/')

def _tf(query, term):
    tf = 0
    tf = tf + 1 + math.log10(query.count(term))
    return tf
def _idf(term):
    if term + '.txt' in indexing:
        txt = 'indexing/' + term + '.txt'
        index = open(txt, 'r+').read()
        index = index.replace(".txt", "")
        string = index.split()
        dtf = len(string)/2
        idf = 1 + math.log10(num_docs/dtf)
        return idf
    else:
        return 0


def _power(query, term, i):
    doc_tf = 0
    if term + '.txt' in indexing:
        txt = 'indexing/' + term + '.txt'
        index = open(txt, 'r+').read()
        index = index.replace(".txt", "")
        string = index.split()
        for j in range(len(string)):
            if string[j] == str(i):
                doc_tf = float(string[j + 1])
    dt = doc_tf * _idf(term )# dt la tf_idf file
    if term in query:
        qt = 2 * _idf(term)# qt là tf_idf query
    else:
        qt = _idf(term)
    return qt, dt


def _distance(query, doc):
    distance = {}
    for each_doc in doc:
        sum = 0
        for each_term in query:
            qt, dt = _power(query, each_term, each_doc)
            sum = sum + (qt - dt)**2
        distance[each_doc] = math.sqrt(sum)
    return distance
'''
def _cosine(query, doc):
    cosine = {}
    for each_doc in doc:
        sum_ = 0
        sum_q = 0
        sum_d = 0
        for each_term in query:
            qt, dt = _power(query, each_term, each_doc)
            sum_ = sum_ + qt*dt
            sum_q = sum_q + qt**2
            sum_d = sum_d + dt**2
        sum_q = math.sqrt(sum_q)
        sum_d = math.sqrt(sum_d)
        if sum_q*sum_d > 0:
            cosine[each_doc] = sum_/(sum_q*sum_d)
    return cosine
'''
# query = input('Nhập câu truy vấn: ')
# query = query.split()
    
def _search_doc(query):
    doc = []
    for term in query:
        if term + '.txt' in indexing:
            txt = 'indexing/' + term + '.txt'
            index = open(txt, 'r+').read()
            index = index.replace(".txt", "")
            string = index.split()
            
            for i in range(len(string)):
                if i % 2 == 0 and string[i] not in doc and float(string[i + 1]) >= 1:
                    doc.append(string[i])

    if len(doc) == 0:
        return []
    distance = _distance(query, doc)
    #cosine = _cosine(query, doc)
    sort_distance = doc
    #sort_cosine = doc
    for i in range(len(doc) - 1):
        for j in range(i + 1, len(doc)):
            if distance[doc[i]] > distance[doc[j]]:
                tmp = sort_distance[i]
                sort_distance[i] = sort_distance[j]
                sort_distance[j] = tmp
            '''
            if cosine[doc[i]] < cosine[doc[j]]:
                tmp = sort_cosine[i]
                sort_cosine[i] = sort_cosine[j]
                sort_cosine[j] = tmp
            '''
    docs = []
    for i in sort_distance:
        docs.append(open('{}/{}'.format('dataset', allfiles[int(i)]), 'r', encoding='utf16').read())
    return docs
#_search_doc(query)


'''
num_index = len(indexing)
i = 0
index = {}
strr = {}
for each_index in indexing:
    txt = 'indexing/' + each_index
    index[i] = open(txt, 'r+')
    each_term = each_index.replace(".txt", "")
    strr[each_term] = index[i].read()
''' 
    
