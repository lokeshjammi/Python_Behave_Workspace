Feature: Register a new user

  @UI
  Scenario: Register user one
    Given lauch browser and open the "properties.angular_practice_url"
    When proper user details are entered
    Then Click on Submit button and check the homepage
    And Close the browser