
class UnitRule:
    def __init__(self, unit_id, dp_edge, node_word, parent):
        self.idx = unit_id
        self.dp_edge = dp_edge
        self.node_word = node_word
        self.parent = parent

    def getUnitId(self):
        return self.idx

    def unitCheck(self, word):
        if self.edgeCheck(word) & self.wordCheck(word):
            return word
        else:
            return False

    def edgeCheck(self, word):
        if self.dp_edge == ['ALL']:
            return True
        elif word.dp in self.dp_edge:
            return True
        else:
            return False

    def wordCheck(self, word):
        if self.node_word == ['']:
            return True
        else:
            for nw in self.node_word:
                if word in nw:
                    return True
                else:
                    return False

