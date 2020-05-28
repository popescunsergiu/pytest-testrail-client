@DEMO-epicNo @DEMO-storyNo
Feature: Fruites - Section - Apples
    Fruits tests


    @TR-C196
    Scenario: Test with no tags apples
        Given I have 5 apples
        When I eat 5 apples
        Then I should have 0 apples

    @TR-C194 @TR-C195 @automated
    Scenario Outline: Test with examples and tags apples
        Given I have <pieces> apples
        When I eat <pieces_eaten> apples
        Then I should have <pieces_left> apples
        Examples:
            | pieces | pieces_eaten | pieces_left |
            | 6      | 3            | 3           |
            | 1      | 1            | 0           |
