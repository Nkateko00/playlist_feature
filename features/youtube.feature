Feature: Youtube Search for Vibes Playlist
    Scenario: Starting youtube & searching for vibes playlist
    Given I am on the Youtube homepage
    When I search for the vibes playlist on search bar
    Then I click  enter
    Then I should get Vibes playlist displayed 
    Then I click on playlist to open