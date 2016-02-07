import unittest
from unittest.mock import MagicMock
import sys
from io import StringIO

import src.program


class ProgramTest (unittest.TestCase):

    def test_run_exist(self):

        program = src.program.Program()
        program.run()

    def test_run_show_menu(self):

        # output = sys.stdout.getline().strip()
        outSpy = StringIO()
        sys.stdout = outSpy

        program = src.program.Program()
        program.run()
        output = outSpy.getvalue().strip()

        assert output.__contains__("Select")



