import unittest
from unittest.mock import MagicMock

import src.main
import src.program


class MainTest(unittest.TestCase):

    def test_when_main_start_Program_run_is_called(self):

        program = src.program.Program()
        program.run = MagicMock()

        src.main.main(program)

        # doesn't work because
        program.run.assert_called_once_with()
