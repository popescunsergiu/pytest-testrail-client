@DEMO-epicNo @DEMO-storyNo
Feature: Fruites - Section - Pears
    Fruits tests


    @TR-C187 @automated
    Scenario: Test with tags pears
        Given I have 5 pears
        When I eat 2 pears
        Then I should have 3 pears

    @TR-C185 @TR-C186
    Scenario Outline: Test with examples pears
        Given I have <pieces> pears
        When I eat <pieces_eaten> pears
        Then I should have <pieces_left> pears
        Examples:
            | pieces | pieces_eaten | pieces_left |
            | 6      | 3            | 3           |
            | 1      | 1            | 0           |
