import unittest
import os
import os.path

from src.phonebook import Phonebook
from src.entry import Entry

filenameDir = os.path.join(os.getcwd(), "ignore")


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        filename = os.path.join(filenameDir, "phonebook.js")
        self.phonebook = Phonebook(filename)

    def test_readFile__when__file_not_exists__should__return_an_empty_string(self):
        filename = os.path.join(filenameDir, "not_exists.js")
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

        filename = os.path.join(filenameDir, "test_phonebook.js")
        if os.path.isfile(filename):
            os.remove(filename)

        self.phonebook = Phonebook(filename)
        self.phonebook._writeFile()

        assert os.path.isfile(filename)

    def test_addRecord__should__exists(self):

        assert hasattr(self.phonebook, "addRecord")

    def test_searchName__should__exists(self):

        assert hasattr(self.phonebook, "searchName")

    def test_searchName__should__return_record(self):
        name = "John"
        mobile = "123 456"

        data = []
        record = Entry(name=name, mobile=mobile)
        data.append(record)

        self.phonebook.records = data
        result = self.phonebook.searchName(name)

        self.assertIsNotNone(result)
        self.assertIn(record, result)

    def test_searchName_with_partial_string__should__return_record(self):

        name = "John"
        mobile = "123 456"

        data = []
        record = Entry(name=name, mobile=mobile)
        data.append(record)

        self.phonebook.records = data
        result = self.phonebook.searchName(name[2:]) # start

        self.assertIsNotNone(result)
        self.assertIn(record, result)

        result = self.phonebook.searchName(name[:2]) # end

        self.assertIsNotNone(result)
        self.assertIn(record, result)
