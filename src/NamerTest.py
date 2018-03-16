import unittest
import collections
from Namer import Namer
class NamerTest(unittest.TestCase):
    def test_from_camel(self):
        rules = ['snake', 'chain', 'space']
        cases = ['lower', 'upper']
        camel_targets = ['getHTML', 'GetHTML', 'GETHtml', 'getHTMLParser', 'GetHTMLParser', 'getHtmlParser', 'GetHtmlParser']
        snake_targets =  ['get_html', 'get_html', 'get_html', 'get_html_parser', 'get_html_parser', 'get_html_parser', 'get_html_parser']
        for rule in rules:
            for case in cases:
                args = collections.namedtuple('Namespace', 'target,rule,case')
                args.case = case
                args.rule = rule
                targets = camel_targets
                expecteds = self.__get_expecteds(rule, camel_targets, snake_targets)
                if 'lower' == case: expecteds = [e.lower() for e in expecteds]
                elif 'upper' == case: expecteds = [e.upper() for e in expecteds]
                for i, target in enumerate(targets):
                    args.target = target
                    #print(args.target)
                    self.assertEquals(expecteds[i], Namer(args).Generate())

    def test_from_camel_as(self):
        rules = ['snake', 'chain', 'space']
        cases = ['as-is']
        camel_targets = ['getHTML', 'GetHTML', 'GETHtml', 'getHTMLParser', 'GetHTMLParser', 'getHtmlParser', 'GetHtmlParser']
        snake_targets =  ['get_HTML', 'Get_HTML', 'GET_Html', 'get_HTML_Parser', 'Get_HTML_Parser', 'get_Html_Parser', 'Get_Html_Parser']
        for rule in rules:
            for case in cases:
                targets = camel_targets
                expecteds = self.__get_expecteds(rule, camel_targets, snake_targets)
                for i, target in enumerate(targets):
                    self.assertEquals(expecteds[i], Namer(self.__get_args(target, rule, case)).Generate())

    def __get_args(self, target, rule, case):
        args = collections.namedtuple('Namespace', 'target,rule,case')
        args.target = target
        args.rule = rule
        args.case = case
        return args
    
    def __get_expecteds(self, rule, camel_targets, snake_targets):
        if 'camel' == rule: return camel_targets
        elif 'snake' == rule: return snake_targets
        elif 'chain' == rule: return [t.replace('_','-') for t in snake_targets]
        elif 'space' == rule: return [t.replace('_',' ') for t in snake_targets]
        else: raise Exception()
    
    def test_from_snake(self):
        rules = ['camel', 'chain', 'space']
        cases = ['lower', 'upper']
        camel_targets = ['getHTML', 'GetHTML', 'GETHtml', 'getHTMLParser', 'GetHTMLParser', 'getHtmlParser', 'GetHtmlParser']
        snake_targets =  ['get_html', 'get_html', 'get_html', 'get_html_parser', 'get_html_parser', 'get_html_parser', 'get_html_parser']
        camel_expected = ['getHtml', 'GetHtml', 'GetHtml', 'getHtmlParser', 'GetHtmlParser', 'getHtmlParser', 'GetHtmlParser']
        for rule in rules:
            for case in cases:
                args = collections.namedtuple('Namespace', 'target,rule,case')
                args.case = case
                args.rule = rule
                targets = snake_targets
                expecteds = self.__get_expecteds(rule, camel_expected, snake_targets)
                if 'camel' == rule:
                    if 'lower' == case: expecteds = [e[0].lower()+e[1:] for e in expecteds]
                    elif 'upper' == case: expecteds = [e[0].upper()+e[1:] for e in camel_expected]
                else:
                    if 'lower' == case: expecteds = [e.lower() for e in expecteds]
                    elif 'upper' == case: expecteds = [e.upper() for e in expecteds]
                for i, target in enumerate(targets):
                    args.target = target
                    #print(rule, case, args.target, expecteds[i])
                    self.assertEquals(expecteds[i], Namer(args).Generate())

    def test_from_snake_as(self):
        rules = ['snake', 'chain', 'space']
        cases = ['as-is']
        camel_targets = ['getHTML', 'GetHTML', 'GETHtml', 'getHTMLParser', 'GetHTMLParser', 'getHtmlParser', 'GetHtmlParser']
        snake_targets =  ['get_HTML', 'Get_HTML', 'GET_Html', 'get_HTML_Parser', 'Get_HTML_Parser', 'get_Html_Parser', 'Get_Html_Parser']
        camel_expected = ['getHTML', 'GetHTML', 'GetHtml', 'getHTMLParser', 'GetHTMLParser', 'getHtmlParser', 'GetHtmlParser']
        for rule in rules:
            for case in cases:
                targets = snake_targets
                expecteds = self.__get_expecteds(rule, camel_expected, snake_targets)
                for i, target in enumerate(targets):
                    self.assertEquals(expecteds[i], Namer(self.__get_args(target, rule, case)).Generate())

    def test_error_0(self):
        rules = ['snake', 'chain', 'space', 'camel']
        cases = ['lower', 'upper', 'as-is']
        targets = ['GETHTML', 'gethtml']
        for rule in rules:
            for case in cases:
                for i, target in enumerate(targets):
                    args = collections.namedtuple('Namespace', 'target,rule,case')
                    args.case = case
                    args.rule = rule
                    args.target = target
                    with self.assertRaises(Exception) as e:
                        Namer(args).Generate()
                    #print(e.exception.args)
                    self.assertEqual('targetが不正値です。camel, snake, chain, space のいずれかに合わせた文字列にしてください。: {}'.format(targets[i]), e.exception.args[0])


if __name__ == "__main__":
    unittest.main()
