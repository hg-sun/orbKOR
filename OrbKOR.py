import os, sys

from ConfigMgr import ConfigMgr
from RuleMgr import RuleMgr
from ModelMgr import ModelMgr
from util.parse.Parser import Parser

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
        else:
            return "No Sentence"

    def getClade(self):
        ret = []
        for cladeObj in self.model_mgr.cladeObj_list:
            clade = cladeObj.clade
            text = " ".join([word.txt for word in clade])
            ret.append(text)
        return ret
