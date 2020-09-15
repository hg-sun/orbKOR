
class CladeRule:
    def __init__(self, clade_id):
        self.idx = clade_id
        self.unit_list = []

    def getCladeId(self):
        return self.id

    def addUnitRule(self, unit_rule):
        self.unit_list.append(unit_rule)
