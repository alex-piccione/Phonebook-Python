import unittest
from unittest.mock import MagicMock
import sys
from io import StringIO

from src.program import Program


class ProgramTest (unittest.TestCase):

    def setUp(self):
        self.program = Program()
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
        phonebook = self.program.getList()
        self.assertIsNotNone(phonebook)
        self.assertIsInstance(phonebook, list)
        #assert hasattr(phonebook, "__iter__"); # is iterable
