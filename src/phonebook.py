import json


class Phonebook:

    def __init__(self, filename):

        self.filename = filename
        self.records = []
        self.loadRecords()

    def loadRecords(self):

        allText = self._readFile()

        self.records = json.loads(allText)

    def saveRecords(self):

        self._writeFile()

    def _readFile(self):

        data = None
        with open(self.filename, 'r') as f:
            data = f.read()
            f.close()
        return data

    def _writeFile(self):

        text = json.dumps(self.records)

        with open(self.filename, 'rw') as f:
            f.write(text)
            f.close()
