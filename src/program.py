
class Program:

    def __init__(self):

        self.menu = """Select:
   1. Search number
   9. Quit
"""

    def run(self):

        self.showMenu()

    def showMenu(self):

        self._write(self.menu)

        selection = self._read()

    def getList(self):

        return []

    def _read(self, text=None):
        return input(text)

    def _write(self, text):
        print()