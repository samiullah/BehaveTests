Feature: Authentication

    Scenario Outline: User logs in
      Given I open insurance website
      When I log in as "<username>"
      Then I should see the message <auth message>

      Examples: Users
        | username          | auth message               |
        | registeredUser    | The meaning of life is 42  |
        | unregisteredUser  | Please sign up             |

