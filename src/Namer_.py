import string

# ファイル数から名前を生成する
class Namer:
    def __init__(self, args):
        self.__args = args

    def Generate(self):
        self.__GetFileNames()
        print(self.__files)
        count = len(self.__files)
        name = self.__GetCountName(count)
        self.__Alignment(count)
        return name

    def __Determine(self):
        if self.__args.target in ' ': return 'space'
        elif self.__args.target in '_': return 'snake'
        elif self.__args.target in '-': return 'chain'
        else: return 'camel'

    def __Change(self):
        typ = self.__Determine()
        lower = self.__args.target.strip()[0].islower()
        if typ != self.__args.rule:
            
        if lower and ('upper' == self.__args.case):

    def __SpaceTo(self):
        targets = self.__args.target.split()
        if 'snake' == self.__args.rule: res = '_'.join(targets)
        elif 'chain' == self.__args.rule: res = '-'.join(targets)
        else:
            for i in len(targets):
                targets[i] = targets[i].lower()
            res = ''.join([t[0].upper() for t in targets])

        if 'lower' == self.__args.case:
            if 'snake' == self.__args.rule: res = res.lower()
            elif 'chain' == self.__args.rule: res = res.lower()
            else: res = res[0].lower()
        else:
            if 'snake' == self.__args.rule: res = res.upper()
            elif 'chain' == self.__args.rule: res = res.upper()
            else: res = res[0].upper()

    def __SnakeTo(self): return __DelimiterTo('snake', '_')
    def __ChainTo(self): return __DelimiterTo('chain', '-')
    def __DelimiterTo(self, typ, delimiter):
        if typ == self.__args.rule: return self.__args.target
        else:
            targets = self.__args.target.split(delimiter)
            if 'camel' == self.__args.rule:
                for i in len(targets):
                    targets[i] = targets[i].lower()
                res = ''.join([t[0].upper() for t in targets])
                if 'lower' == self.__args.case: return res[0].lower() + res[1:]
                elif 'upper' == self.__args.case: return res[0].upper() + res[1:]
                else: return res
            else:
                res = '-'.join(targets)
                if 'lower' == self.__args.case: return res.lower()
                elif 'upper' == self.__args.case: return res.upper()
                else: return res
    
    def __CamelTo(self):
        if 'camel' != self.__args.rule:
            from CamelSplitter import CamelSplitter
            targets = CamelSplitter().Split(self.__args.target)
            if 'snake' == self.__args.rule:res = '_'.join(targets)
            elif 'chain' == self.__args.rule: res = '-'.join(targets)
            else: res = ''.join(targets)
            if 'lower' == self.__args.case: return res.lower()
            elif 'upper' == self.__args.case: return res.upper()
            else: return res
        else:
            if 'lower' == self.__args.case: return self.__args.target[0].lower() + self.__args.target[1:]
            elif 'upper' == self.__args.case: return self.__args.target[0].upper() + self.__args.target[1:]
            else: return self.__args.target
            
from abc import ABCMeta, abstractmethod
class Analizer(metaclass=ABCMeta):
    @abstractmethod
    def Is(self): pass
    @abstractmethod
    def Split(self): pass
    @abstractmethod
    def To(self, words): pass
class Camel(Analizer):
    def __init__(self, args):
        self.__args = args
    def Is(self): return any(t.isupper() for t in self.__args.target)
    def Split(self):
        from CamelSplitter import CamelSplitter
        return CamelSplitter().Split(self.__args.target)
    def To(self, words):
        res = ''.join(words)
        if 'lower' == self.__args.case: return res[0].lower() + res[1:]
        elif 'upper' == self.__args.case: return res[0].upper() + res[1:]
        else: return res
class Snake(Delimiter):
    def __init__(self, args): super().__init__(args, '_')
class Chain(Delimiter):
    def __init__(self, args): super().__init__(args, '-')
class Space(Delimiter):
    def __init__(self, args): super().__init__(args, ' ')
class Delimiter(Analizer):
    def __init__(self, args, delimiter):
        self._delimiter = delimiter
        if 1 == len(self._delimiter): raise Exception('delimiterは1文字にしてください。')
    def Is(self): return self._delimiter in self.__args.target
    def Split(self): return self.__args.target.split(self._delimiter)
    def To(self, words):
        res = self._delimiter.join(words)
        if 'lower' == self.__args.case: return res.lower()
        elif 'upper' == self.__args.case: return res.upper()
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

