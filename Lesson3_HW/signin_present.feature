# Created by Claudia at 2/17/2023
Feature: Verify if sign in is present upon clicking orders
  # This is part of the homework for lesson 3

  Scenario: signin presence on Amazon Page
    Given Open Amazon page
    When open Amazon orders page
    Then verify signin present in page
    Then verify email input present


