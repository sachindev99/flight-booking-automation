Feature: Flight booking

  Scenario: Book a one-way flight
    Given user is on the flight booking site
    And user selects the From and To locations
      | Delhi | Paris |
    And user selects the departure date and number of passengers
    And user selects the one way trip
    And user selects the travel class
    And user clicks the search flight button
    When user selects a "AL248" departure flight from the list
    And proceed to the customer details page
    And user enters passenger details
    And user enters payment details
    Then booking should be confirmed

  Scenario: Book a round trip flight
    Given user is on the flight booking site
    And user selects the From and To locations
      | Sydney | Singapore |
    And user selects the departure date and number of passengers
    And user selects the return date
    And user selects the travel class
    And user clicks the search flight button
    When user selects a "AL248" departure flight from the list
    And user selects a "BJ311" return flight from the list
    And proceed to the customer details page
    And user enters passenger details
    And user enters payment details
    Then booking should be confirmed

  Scenario: Return date only for the round trip
    Given user is on the flight booking site
    When user selects the one way trip
    Then Return date field is not visible
    And when user unticked the one way trip
    Then Return date field is visible