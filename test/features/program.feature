Feature: Search

  Scenario: Search a name
    Given the name "Alex"
     When search it in Phonebook
     Then the result is "123 456"
    