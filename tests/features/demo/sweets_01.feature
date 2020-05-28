@DEMO-epicNo @DEMO-storyNo
Feature: Sweets
    Sweets tests


    @TR-C180
    Scenario: Test with no tags chocolates
        Given I have 5 chocolates
        When I eat 3 chocolates
        Then I should have 8 chocolates

    @TR-C179 @automated
    Scenario: Test with tags candies
        Given I have 5 candies
        When I eat 2 candies
        Then I should have 3 candies
