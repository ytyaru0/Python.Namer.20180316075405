from Analizer import Analizer 
class Camel(Analizer):
    def __init__(self, args):
        self.__args = args
    def TargetIs(self):
        return any(t.islower() for t in self.__args.target) and any(t.isupper() for t in self.__args.target) 
    def RuleIs(self): return 'camel' == self.__args.rule
    def Split(self):
        from CamelSplitter import CamelSplitter
        return CamelSplitter().Split(self.__args.target)
    def To(self, words):
        if 'as-is' != self.__args.case: words = [w[0].upper()+w[1:].lower() for w in words]
        res = ''.join(words)
        if 'lower' == self.__args.case: return res[0].lower() + res[1:]
        else: return res
