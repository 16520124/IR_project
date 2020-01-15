import os


def create_pairs(pair_of_words):
    pairs = []
    for pair_of_word in pair_of_words:
        pair_of_word = pair_of_word.strip()
        if '/' in pair_of_word:
            word, type = pair_of_word.rsplit('/', 1)
            if word == '' or type == '':
                continue
            pairs.append({word: type})
    return pairs


def read_files(name='dataset'):
    files = os.listdir(name)
    pair_words = list()
    for file in files:
        stream = open(f"{name}\\" + file, 'r+', encoding="utf8")
        lines = stream.readlines()
        for line in lines:
            line = line.replace(u'\ufeff', '')
            line = line.replace('\n', '')
            if line == '':
                continue
            pair_of_words = line.lower().split(' ')
            pair_words.extend(create_pairs(pair_of_words))

        stream.close()
    return pair_words


wh = [',', '[', ']', "'", '"', '-', '(', ')', ':', '“', '”']
end = ['.', ';', '!', '...', '?']


def create_table_a(pair_words):
    types_a = dict()
    ss = dict()
    isStart = False
    pre_type = ''
    for pair in pair_words:
        word, type = list(pair.items())[0]

        if type in end:
            isStart = True
            pre_type = ''
            continue

        if type in wh:
            pre_type = ''
            continue

        if pre_type == '':
            pre_type = type
        else:
            if isStart:
                isStart = False
                if type in ss.keys():
                    ss[type] = ss[type] + 1
                else:
                    ss[type] = 1
                pre_type = type

            if pre_type in types_a.keys():
                if type in types_a[pre_type].keys():
                    types_a[pre_type][type] = types_a[pre_type][type] + 1
                else:
                    types_a[pre_type][type] = 1
            else:
                types_a[pre_type] = dict()
                types_a[pre_type][type] = 1
            pre_type = type
    types_a['ss'] = ss
    return types_a


def create_table_b(pair_words):
    table_b = dict()
    for pair in pair_words:
        word, type = pair.popitem()
        if type in wh or type in end:
            continue
        if type in table_b.keys():
            if word in table_b[type].keys():
                table_b[type].update(
                    {word: table_b[type][word] + 1})
            else:
                table_b[type][word] = 1
        else:
            table_b[type] = dict()
            table_b[type][word] = 1
    return table_b


def smooth(table):
    for key in table.keys():
        for type in table.keys():
            if 'ss' == type:
                continue
            if type not in table[key].keys():
                table[key][type] = 1
            else:
                table[key][type] = table[key][type] + 1
    return table


def sum_table(table):
    for key in table.keys():
        s = sum(table[key].values())
        table[key]['sum'] = s
    return table


def probability(table):
    matrix = dict()
    for col in table.keys():
        for row in table[col].keys():
            if row == 'sum':
                continue
            if col not in matrix.keys():
                matrix[col] = dict()
            matrix[col][row] = table[col][row] / table[col]['sum']
    return matrix


def create_sub(root, sub_type, value):  # tạo đường đi à
    root[sub_type] = dict()
    root[sub_type]['val'] = value


class HMM:

    def __init__(self):
        self.prob_b = dict()
        self.prob_a = dict()
        self.pair_words = read_files()
        self.create_a()
        self.create_b()

    def create_a(self):
        table_a = smooth(create_table_a(self.pair_words))
        sum_a = sum_table(table_a)
        self.prob_a = probability(sum_a)

    def create_b(self):
        table_b = smooth(create_table_b(self.pair_words))
        sum_b = sum_table(table_b)
        self.prob_b = probability(sum_b)

    def find_sub(self, word):
        sub = dict()
        for key in self.prob_b.keys():
            if word in self.prob_b[key].keys():
                sub[key] = self.prob_b[key][word]
        return sub

    def cal_hmm(self, words):
        root_pos = dict()
        self.hmm(root_pos, words, 0, len(words), True, 0)
        pos = []
        self.veterbi(root_pos, pos)
        return pos

    def hmm(self, root, words, index, max, head, parent_value):
        if index >= max:
            return
        word = words[index]
        if head:
            sub = self.find_sub(word)
            for sub_type, value in sub.items():
                if sub_type in self.prob_a['ss'].keys():
                    create_sub(root, sub_type, self.prob_a['ss'][sub_type] * value)
                    self.hmm(root[sub_type], words, 1, max, False,
                            self.prob_a['ss'][sub_type] * value)
        else:
            sub_type_max = ''
            value_max = 0
            for sub_type, value in self.find_sub(word).items():
                if sub_type in self.prob_a.keys():
                    for type in self.prob_a[sub_type].keys():
                        if value_max < parent_value * self.prob_a[sub_type][type] * value:
                            sub_type_max = sub_type
                            value_max = parent_value * \
                                self.prob_a[sub_type][type] * value

            if value_max == 0:
                return
            create_sub(root, sub_type_max, value_max)
            self.hmm(root[sub_type_max], words,
                     index + 1, max, False, value_max)

    def veterbi(self, root, pos):
        key_max = ''
        max_value = 0
        for key, value in root.items():
            if 'val' in key:
                continue
            if 'val' not in value.keys():
                break
            sub_val = value['val']
            if max_value < sub_val:
                max_value = sub_val
                key_max = key

        if '' == key_max:
            return
        if len(root.keys()) == 1 and 'val' in root.keys():
            pos.append(key_max)
            return
        else:
            pos.append(key_max)
            self.veterbi(root[key_max], pos)
