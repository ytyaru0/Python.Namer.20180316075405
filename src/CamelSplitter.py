import glob
import os.path
import string
import math

# キャメルケース文字列を配列にする
class CamelSplitter:
    def __init__(self):
        pass

    def Split(self, target):
        return self.__Combin(self.__SplitUppercase(target))

    def __SplitUppercase(self, target):
        targets = []
        start = 0
        end = 0
        upper_start = -1
        # getHTML -> ['get','H','T','M','L']
        for i in range(1, len(target)):
            if target[i].isupper():
                end = i
                targets.append(target[start:end])
                start = i
        targets.append(target[start:])
        return targets

    def __Combin(self, targets):
        result = []
        for i, t in enumerate(targets):
            # ['get','H','T','M','L'] -> ['get','HTML']
            if 1 == len(t):
                if 0 == len(result): result.append(targets[i])
                else:
                    if result[-1].isupper(): result[-1] += targets[i]
                    else: result.append(targets[i])
            else: result.append(targets[i])
        return result


if __name__ == '__main__':
    s = CamelSplitter()
    assert(['get','Html'] == s.Split('getHtml'))
    assert(['Get','Html'] == s.Split('GetHtml'))
    assert(['get','HTML'] == s.Split('getHTML'))
    assert(['Get','HTML'] == s.Split('GetHTML'))
    assert(['Get','HTML', 'Parser'] == s.Split('GetHTMLParser'))
    assert(['Get','Html', 'Parser'] == s.Split('GetHtmlParser'))

