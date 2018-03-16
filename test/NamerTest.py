import unittest
import collections
from Namer import Namer
class NamerTest(unittest.TestCase):
    def test_some_0(self):
        args = collections.namedtuple('Namespace', ['target'])
        args.target = 'getHTMLParser'
        self.assertEquals('get_html_parser', Namer(args).Generate())
    """
    def test_some_1(self):
        with self.assertRaises(Exception) as e:
            raise Exception('ERROR MESSAGE')
        self.assertEqual('ERROR MESSAGE', e.exception.args[0])
    """


if __name__ == "__main__":
    unittest.main()
