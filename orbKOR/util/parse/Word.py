
class Word:
    def __init__(self, idx, txt, dp):
        self.idx = idx
        self.txt = txt
        self.dp = dp
        self.head = None
        self.children = []
