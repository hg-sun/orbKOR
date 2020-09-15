
from Clade import Clade

class ModelMgr:
    def __init__(self):
        self.clade_list = None
        self.cladeObj_list = []

    def addClade(self, clade_list):
        self.clade_list = clade_list

        for clade in self.clade_list:
            rule_id = clade.pop(0)
            cladeObj = Clade(rule_id, clade)
            self.cladeObj_list.append(cladeObj)
