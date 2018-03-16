import string

# ファイル数から名前を生成する
class Namer:
    def __init__(self, args):
        self.__args = args
    def Generate(self):
        cases = [Snake(self.__args), Chain(self.__args), Space(self.__args), Camel(self.__args)]
        s = GetSpliter(cases)
        words = s.Split()
        c = GetChanger(cases)
        return c.To(words)
    # targetがどのcaseか判別する
    def __GetSpliter(self, cases):
        for a in cases:
            if a.TargetIs(): return a
    # ruleがどのcaseか判別する
    def __GetChanger(self):
        for a in cases:
            if a.RuleIs(): return a

from abc import ABCMeta, abstractmethod
class Analizer(metaclass=ABCMeta):
    @abstractmethod
    def TargetIs(self): pass
    @abstractmethod
    def RuleIs(self): pass
    @abstractmethod
    def Split(self): pass
    @abstractmethod
    def To(self, words): pass
class Camel(Analizer):
    def __init__(self, args):
        self.__args = args
    def TargetIs(self): return any(t.isupper() for t in self.__args.target)
    def RuleIs(self): return 'camel' == self.__args.rule
    def Split(self):
        from CamelSplitter import CamelSplitter
        return CamelSplitter().Split(self.__args.target)
    def To(self, words):
        res = ''.join(words)
        if 'lower' == self.__args.case: return res[0].lower() + res[1:]
        elif 'upper' == self.__args.case: return res[0].upper() + res[1:]
        else: return res
class Snake(Delimiter):
    def __init__(self, args): super().__init__(args, '_', self.__class__.__name__.lower())
class Chain(Delimiter):
    def __init__(self, args): super().__init__(args, '-', self.__class__.__name__.lower())
class Space(Delimiter):
    def __init__(self, args): super().__init__(args, ' ', self.__class__.__name__.lower())
class Delimiter(Analizer):
    def __init__(self, args, delimiter, rule):
        self._args = args
        self._delimiter = delimiter
        self._rule = rule
        if 1 == len(self._delimiter): raise Exception('delimiterは1文字にしてください。')
    def TargetIs(self): return self._delimiter in self._args.target
    def RuleIs(self): return self._rule == self.__args.rule
    def Split(self): return self._args.target.split(self._delimiter)
    def To(self, words):
        res = self._delimiter.join(words)
        if 'lower' == self._args.case: return res.lower()
        elif 'upper' == self._args.case: return res.upper()
        else: return res


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='NameGenerator.',
    )
    parser.add_argument('target')
    parser.add_argument('-r', '--rule', choices=['camel', 'snake', 'chain'], default='snake')                                        # 拡張子
    parser.add_argument('-c', '--case', choices=['lower', 'upper', 'as-is'], default='lower')
    args = parser.parse_args()
    if args.target is None: raise Exception('起動引数が足りません。対象の文字列を渡して下さい。')
    print(Namer(args).Generate())

