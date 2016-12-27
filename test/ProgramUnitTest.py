import unittest.mock
from unittest.mock import MagicMock
from unittest.mock import patch
from src.program import Program
from src.phonebook import Phonebook
from test.helper import Helper


class ProgramTest (unittest.TestCase):

    def setUp(self):
        phonebook = MagicMock()
        phonebook.records = []
        self.program = Program(phonebook)
        self.program._read = MagicMock(return_value="")
        self.program._write = MagicMock()

    def test_menu__should__exists(self):
        assert hasattr(self.program, "menu")

    def test_run__should__exist(self):
        hasattr(self.program, "run")
        self.program.run()

    def test_run__should__show_menu_and_wait_for_input(self):
        expectedText = self.program.menu

        self.program.run()

        self.program._write.assert_called_once_with(expectedText)

        self.program._read.assert_called_once_with()

    def test_get_list__should__exists(self):
        assert hasattr(self.program, "getList")

    def test_get_list__should__return_a_list(self):
        entries = self.program.getList()
        self.assertIsNotNone(entries)
        self.assertIsInstance(entries, list)
        # assert hasattr(phonebook, "__iter__"); # is iterable

    def test_getList__when__an_entry_is_added__should__return_a_list_with(self):

        # Arrange
        entry = Helper.getTestEntry()

        phonebook = Phonebook(Helper.filename)
        phonebook.records = MagicMock(return_value=[entry])
        program = Program(Helper.filename)

        # Act
        entries = self.program.getList()

        # Assert
        Helper.assertPhonebookContainsEntry(phonebook, entry)

    def test_showList__should__call_getList(self):
        program = Program(Helper.filename)
        list = []

        with patch.object(self.program, "getList", return_value=list) as mock_getList:
            # Act
            self.program.showList()

        mock_getList.assert_called_once_with()




