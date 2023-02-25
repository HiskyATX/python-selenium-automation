# Created by Claudia at 2/23/2023
Feature: Finding the main categories on the Best Sellers page
  # Enter feature description here

  Scenario: Verify that Bestsellers page shows five categories
    Given Open Amazon Best Sellers page
    Then Verify that Bestsellers categories are present
    Then Verify that Best Sellers has 5 links