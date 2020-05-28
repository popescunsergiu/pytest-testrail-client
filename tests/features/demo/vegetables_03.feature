@DEMO-epicNo @DEMO-storyNo
Feature: Vegetables - Section 01
    Vegetables tests

    Background:
        Given I have 5 carrots

    @TR-C202 
    Scenario: Test with background and no tags carrots
        When I eat 3 carrots
        Then I should have 2 carrots

    @TR-C201 @automated
    Scenario: Test with background and tags carrots
        When I eat 2 carrots
        Then I should have 3 carrots