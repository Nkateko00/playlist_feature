Feature: Youtube Search for Playlist & Podcast

    Scenario: Starting youtube & searching for vibes playlist
    Given I am on the Youtube homepage
    When I "<search>" for the vibes playlist on search bar
    Then I click  enter
    Then I click on playlist to open
    Then I click on selected song
    Then I should get Vibes playlist displayed 

    Scenario: Starting youtube & searching for Lex Fridmans podcast
    Given I am on the youtube landing page
    When I "<lookup>" Lex Fridmans podcast
    Then I click on the podcast to open 
    Then I verify Episode 435 is playing on youtube



