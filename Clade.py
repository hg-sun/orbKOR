
class Clade:
    def __init__(self, rule_id, clade):
        self.rule_id = rule_id
        self.clade = sorted(clade, key=lambda word: word.idx)
