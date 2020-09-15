
class CladeRule:
    def __init__(self, clade_id):
        self.idx = clade_id
        self.unit_list = []

    def getCladeId(self):
        return self.idx

    def addUnitRule(self, unit_rule):
        self.unit_list.append(unit_rule)

    def cladeCheck(self, word):
        word_dic = {}
        total_word_list = []

        for unit_rule in self.unit_list:
            if unit_rule.parent == '':
                if unit_rule.unitCheck(word):
                    key = unit_rule.idx
                    word_dic[key] = word
                else:
                    return None
            else:
                if len(total_word_list) == 0:
                    matched_word = []
                    for word_child in word_dic[uni_rule.parent].children:
                        if unit_rule.unitCheck(word_child):
                            matched_word.append(word_child)
                    if len(matched_word) == 1:
                        key = unit_rule.idx
                        word_dic[key] = matched_word[0]
                    else:
                        key = unit_rule.idx
                        for word in matched_word:
                            word_dic_tmp = word_dic.copy()
                            word_dic_tmp[key] = word
                            total_word_list.append(word_dic_tmp)
                else:
                    for dic in total_word_list:
                        condition = Flase
                        for word_child in dic[unit_rule.parent].children:
                            if unit_rule.unitCheck(word_child):
                                condition = True
                                key = unit_rule.idx
                                dic[key] - word_child
                            if not condition:
                                dic['condition'] = 'N'
                    total_word_list = [dic for dic in total_word_list if 'condition' not in dic]
                    if total_word_list == []:
                        return None
        if total_word_list != []:
            ret = []
            for dic in total_word_list:
                ret.append(self.tokenDicToList(dic))
            return ret
        else:
            return self.tokenDicToList(word_dic)

    def tokenDicToList(self, word_dic):
        word_list = []
        word_list.append(self.idx)
        for key, value in word_dic.items():
            word_list.append(value)
        return word_list
