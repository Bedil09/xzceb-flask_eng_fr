
'''Unit test for translator.py'''
import unittest
from translator import english_to_french
from translator import french_to_english


class TestTranslator(unittest.TestCase):
    '''Test class for translator'''

    def test_translateToFrench(self):
        '''Tests for french translation'''
        self.assertIsNone(None, "No input provided")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_translateToEnglish(self):
        '''Tests for english transalation'''
        self.assertIsNone(None, "No input provided")
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()
