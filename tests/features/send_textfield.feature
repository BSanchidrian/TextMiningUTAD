Feature: Send textfield

  Scenario: Text of size 4
    Given I have "text"
    When I press "submit" button
    Then I expected "text - 1"

  Scenario: Text of size 101
    Given I have "Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem"
    When I press "submit" button
    Then I expected "lorem - 16, lore - 1"

  Scenario: Text of size 0
    Given I have " "
    When I press "submit" button
    Then I expected " "
