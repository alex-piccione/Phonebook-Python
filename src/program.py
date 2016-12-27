
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

        if selection == "2": self.showList()


    def showList(self):

        records = self.getList()
        text = 'Name | Number'
        for entry in records:
            text += '{name} {number}'.format(name=entry.Name, number=entry.Number)

        self._write(text)

    def getList(self):

        return self.phonebook.records

    def _read(self, text=None):
        return input(text or "")

    def _write(self, text):
        print(text)