import sys

from src.phonebook import Phonebook
from src.program import Program

filename = "phonebook.data"


def main(program, argv=None):
    if argv is None:
        argv = sys.argv
    program.run()
    return 0

if __name__ == '__main__':

    phonebook = Phonebook(filename)
    program = Program(phonebook)
    exit_value = main(program)
    sys.exit(exit_value)
