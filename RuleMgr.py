import csv

from CladeRule import CladeRule
from UnitRule import UnitRule

class RuleMgr:
    def __init__(self, config, rule):
        self.rule = rule if rule is not None else 'default'
        rule_path = config.getValue('RuleMgr', self.rule + '.rule.file')

        self.cladeRules = []
        
        self.loadRules(rule_path)

    def loadRules(self, path):
        with open(path, 'r') as f:
            rules = list(csv.reader(f))
            rules.pop(0)

        for line in rules:
            clade_id = line[0]
            clade_rule = self.findCladeRuleById(clade_id)

            if clade_rule is None:
                clade_rule = CladeRule(clade_id)
                self.cladeRules.append(clade_rule)

            unit_rule = UnitRule(line[1],
                    line[2].split("|"),
                    line[3].split("|"),
                    line[4])
            clade_rule.addUnitRule(unit_rule)

    def findCladeRuleById(self, clade_id):
        for clade_rule in self.cladeRules:
            if clade_id == clade_rule.getCladeId():
                return clade_rule
        return None

    def getClade(self, word_list):
        total_clade_list = []
        for rule in self.cladeRules:
            tmp = []
            for word in word_list:
                clades = rule.cladeCheck(word)
                if clades is not None:
                    if any(isinstance(unit, list) for unit in clades):
                        tmp.extend(clades)
                    else:
                        tmp.append(clades)
            total_clade_list.append(tmp)
        return total_clade_list
