Feature: Clean textfield

  Scenario: Text of size 4 submit
    Given I have "text"
    When I press "reset" button
    Then I clean the text field

  Scenario: Text of size 0
    Given I have " "
    When I press "reset" button
    Then I clean the text field

  Scenario: Text of size 101
    Given I have "Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem"
    When I press "reset" button
    Then I clean the text field

  Scenario: Text of size 6 submit
    Given I have "holiwi"
    When I press "submit" button
    Then I clean the text field
