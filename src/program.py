
class Program:

    def __init__(self, phonebook):

        self.menu = """Select:
   1. Search number
   9. Quit
"""

        self.phonebook = phonebook

    def run(self):

        self.showMenu()

    def showMenu(self):

        self._write(self.menu)

        selection = self._read()

    def getList(self):

        return self.phonebook.records

    def _read(self, text=None):
        return input(text)

    def _write(self, text):
        print()