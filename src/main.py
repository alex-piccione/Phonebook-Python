import sys
from src.program import Program


def main(program, argv=None):
    if argv is None:
        argv = sys.argv
    program.run()
    return 0

if __name__ == '__main__':
    program = Program()
    exit_value = main(program)
    sys.exit(exit_value)
