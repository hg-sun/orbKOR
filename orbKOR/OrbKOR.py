import os, sys

from orbKOR.ConfigMgr import ConfigMgr
from orbKOR.RuleMgr import RuleMgr
from orbKOR.ModelMgr import ModelMgr
from orbKOR.util.parse.Parser import Parser

current_path = os.path.dirname(os.path.abspath(__file__))
global_config = ConfigMgr(current_path)
parser = None

class OrbKOR:
    parser = Parser(global_config)
    rule_mgr = RuleMgr(global_config, rule=None)

    def __init__(self, rule=None):

        if rule is None:
            rule = 'default'

        if OrbKOR.rule_mgr.rule != rule:
            OrbKOR.rule_mgr = RuleMgr(global_config, rule)

    def parse(self, data):
        self.model_mgr = ModelMgr()
        clade_list = []
        if OrbKOR.parser.getSent(data):
            word_list = OrbKOR.parser.getSent(data).word_list
            clade_list = OrbKOR.rule_mgr.getClade(word_list)
            self.model_mgr.addClade(clade_list)
            return True
        else:
            return False

    def getClade(self):
        ret = []
        for cladeObj in self.model_mgr.cladeObj_list:
            clade = cladeObj.clade
            text = " ".join([word.txt for word in clade])
            ret.append(text)
        return ret
