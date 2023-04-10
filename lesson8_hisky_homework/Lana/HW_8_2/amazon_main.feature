Feature: Tests for Amazon main page

#  Scenario: Hamburger menu is present
#    Given Open amazon page
#    Then Verify hamburger menu is present
#
#  Scenario: Footer has correct amount of links
#    Given Open amazon page
#    Then Verify that footer has 38 links
#
#  Scenario: User can see language options
#    Given Open Amazon page
#    When Hover over language options
#    Then Verify Spanish option present

  Scenario: User can see new arrivals options
    Given Open Clothing page
    When Hover over New Arrivals
    Then Verify that categories appear