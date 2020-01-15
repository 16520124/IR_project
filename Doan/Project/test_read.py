# import os


# def create_pairs(pair_of_words):
#     pairs = []
#     for pair_of_word in pair_of_words:
#         pair_of_word = pair_of_word.strip()
#         if '/' in pair_of_word:
#             word, type = pair_of_word.rsplit('/', 1)
#             if word == '' or type == '':
#                 continue
#             pairs.append({word: type})
#     return pairs

# def read_files(name):
#     files = os.listdir(name)
#     pair_words = list()
#     for file in files:
#         stream = open(f"${name}/" + file, 'r+', encoding="utf8")
#         lines = stream.readlines()
#         for line in lines:
#             line = line.replace(u'\ufeff', '')
#             line = line.replace('\n', '')
#             if line == '':
#                 continue
#             pair_of_words = line.lower().split(' ')
#             pair_words.extend(create_pairs(pair_of_words))

#         stream.close()
#     return pair_words


# pair_words = read_files()
# print(pair_words)
# # print(words[0][:1])
