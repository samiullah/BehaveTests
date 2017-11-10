Feature: Navigate to url,see signup button and signup

  Scenario: Open website
    Given I open insurance website
    Then I print the title

  Scenario: See if  Signup Button is clickable
    Given I open insurance website
    Then I click on  the Signup Button

  Scenario: Signup as a new user
    Given I open insurance website
    Then I click on  the Signup Button
    Then I wait for "15" seconds
    Then I wait for the element with xpath "//input[@id='signup:fname']"
    And I fill the signup form  with values
    Then I wait for "5" seconds
    When I click on  the Submit Button
    Then I wait for "7" seconds
    Then I should see continue button
