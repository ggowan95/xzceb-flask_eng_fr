import unittest

from translator import frenchtoenglish, englishtofrench

class TestFrenchToEnglish():
    def test_null(self):
        self.assertIsNone(frenchtoenglish(None))
        self.assertIsEqual(frenchtoenglish("Hello"), "Bonjour")
        self.assertIsEqual(frenchtoenglish("Love"), "Amour")
        self.assertIsNotEqual(frenchtoenglish("Ham"),"Jamboni")

class TestEnglishToFrench():
    def test_null(self):
        self.assertIsNone(englishtofrench(None))
        self.assertIsEqual(englishtofrench("Bonjour"), "Hello")
        self.assertIsEqual(englishtofrench("Eau"), "Water")
        self.assertIsNotEqual(englishtofrench("huile"), "vinaigre")

unittest.main()