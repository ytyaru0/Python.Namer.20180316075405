from Analizer import Analizer 
class Delimiter(Analizer):
    def __init__(self, args, delimiter, rule):
        self._args = args
        self._delimiter = delimiter
        self._rule = rule
        if 1 != len(self._delimiter): raise Exception('delimiterは1文字にしてください。')
    def TargetIs(self): return self._delimiter in self._args.target
    def RuleIs(self): return self._rule == self._args.rule
    def Split(self): return self._args.target.split(self._delimiter)
    def To(self, words):
        res = self._delimiter.join(words)
        if 'lower' == self._args.case: return res.lower()
        elif 'upper' == self._args.case: return res.upper()
        else: return res
class Snake(Delimiter):
    def __init__(self, args): super().__init__(args, '_', self.__class__.__name__.lower())
class Chain(Delimiter):
    def __init__(self, args): super().__init__(args, '-', self.__class__.__name__.lower())
class Space(Delimiter):
    def __init__(self, args): super().__init__(args, ' ', self.__class__.__name__.lower())
