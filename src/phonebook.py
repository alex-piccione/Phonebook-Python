import pickle
import os.path


class Phonebook:

    def __init__(self, filename):

        self.filename = filename
        self.records = []
        self.loadRecords()

    def loadRecords(self):

        data = self._readFile()
        if data is None:
            data = []
        self.records = data

    def saveRecords(self):

        self._writeFile()

    def addRecord(self, record):

        self.records.append(record)

    def searchName(self, text):

        result = []

        for record in self.records:
            if record.name.__contains__(text):
                result.append(record)

        return result

    def _readFile(self):

        data = []
        if os.path.isfile(self.filename):
            with open(self.filename, 'rb') as f:
                #data = f.read()
                data = pickle.load(f)
                f.close()

        return data

    def _writeFile(self):

        #text = pickle.dumps(self.records)

        with open(self.filename, 'ab') as f:
            #f.write(text)
            pickle.dump(self.records, f)
            f.close()
