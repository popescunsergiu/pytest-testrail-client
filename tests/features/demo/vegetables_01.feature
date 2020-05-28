@DEMO-epicNo @DEMO-storyNo
Feature: Vegetables - Section 01
    Vegetables tests


    @TR-C193
    Scenario: Test with no tags onions
        Given I have 5 onions
        When I eat 3 onions
        Then I should have 8 onions

    @TR-C192 @automated
    Scenario: Test with tags potatoes
        Given I have 5 potatoes
        When I eat 2 potatoes
        Then I should have 3 potatoes
