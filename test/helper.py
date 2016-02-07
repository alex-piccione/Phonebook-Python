import os

#filename = os.path.join(os.getcwd(), "ignore", "phonebook_test.data")
from src.entry import Entry


class Helper:

    #def createEptyPhonebookFile(self):

    filename = os.path.join(os.getcwd(), "ignore", "phonebook_test.data")

    @staticmethod
    def getTestEntry():
        name = "John"
        mobile = "+39 333 123456"
        entry = Entry(name=name, mobile=mobile)
        return entry

    @staticmethod
    def assertPhonebookContainsEntry(phonebook, entry):
        for item in phonebook.records:
            if item.name == entry.name and item.mobile == entry.mobile:
                return True
        return False
