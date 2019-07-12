import unittest

from stanfordcorenlp import StanfordCoreNLP


class MyTestCase(unittest.TestCase):
    def test_args(self):
        self.assertRaises(IOError, StanfordCoreNLP, '/abc')
        self.assertRaises(ValueError, StanfordCoreNLP, r'../stanford-parser-full-2018-10-17/',
                          lang='abc')
        self.assertRaises(ValueError, StanfordCoreNLP, r'../stanford-parser-full-2018-10-17/',
                          memory='4m')


if __name__ == '__main__':
    unittest.main()
