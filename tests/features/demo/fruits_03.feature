@DEMO-epicNo @DEMO-storyNo
Feature: Fruites - Section 02 - Cherries
    Fruits tests



    @TR-C199
    Scenario: Test with no tags cherries
        Given I have 5 cherries
        When I eat 5 cherries
        Then I should have 0 cherries

    @TR-C197 @TR-C198 @automated
    Scenario Outline: Test with examples and tags cherries
        Given I have <pieces> cherries
        When I eat <pieces_eaten> cherries
        Then I should have <pieces_left> cherries
        Examples:
            | pieces | pieces_eaten | pieces_left |
            | 6      | 3            | 3           |
            | 1      | 1            | 0           |
