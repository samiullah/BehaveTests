Feature: Login

    Scenario: User logs in
      Given I open insurance website
      When I log in as "registeredUser"
      Then I wait for "15" seconds
      Then I should see the logout button

