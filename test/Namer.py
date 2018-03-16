import string
from Camel import Camel
from Delimiter import Snake, Chain, Space

# ファイル数から名前を生成する
class Namer:
    def __init__(self, args):
        self.__args = args
    def Generate(self):
        cases = [Snake(self.__args), Chain(self.__args), Space(self.__args), Camel(self.__args)]
        s = self.__GetSpliter(cases)
        words = s.Split()
        c = self.__GetChanger(cases)
        return c.To(words)
    # targetがどのcaseか判別する
    def __GetSpliter(self, cases):
        for a in cases:
            if a.TargetIs(): return a
    # ruleがどのcaseか判別する
    def __GetChanger(self, cases):
        for a in cases:
            if a.RuleIs(): return a


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

