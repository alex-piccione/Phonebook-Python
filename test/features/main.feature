Feature: Main program

  Scenario: Menu is shown
    Given the program
     When it starts
     Then Program.run() is called

