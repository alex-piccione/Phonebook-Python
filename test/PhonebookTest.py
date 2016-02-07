import unittest
import os
import os.path

from src.phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        filename = os.path.join(os.getcwd(), "phonebook.js")
        self.phonebook = Phonebook(filename)

    def test_readFile__when__file_not_exists__should__return_an_empty_string(self):
        filename = os.path.join(os.getcwd(), "not_exists.js")
        if os.path.exists(filename):
            os.remove(filename)

        self.phonebook = Phonebook(filename)
        data = self.phonebook._readFile()

        self.assertIsNotNone(data)
        assert data == ""

    def test_readFile__should__return_a_text(self):

        data = self.phonebook._readFile()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, str)

    def test_writeFile__should__exists(self):

        assert hasattr(self.phonebook, "_readFile")

    def test_writeFile__when__file_not_exists__should__create_a_file(self):

        filename = os.path.join(os.getcwd(), "test_phonebook.js")
        if os.path.isfile(filename):
            os.remove(filename)

        self.phonebook = Phonebook(filename)
        self.phonebook._writeFile()

        assert os.path.isfile(filename)







