@DEMO-epicNo @DEMO-storyNo
Feature: Vegetables - Section 02
    Vegetables tests


    @TR-C190 @TR-C191
    Scenario Outline: Test with examples potatoes
        Given I have <pieces> potatoes
        When I eat <pieces_eaten> potatoes
        Then I should have <pieces_left> potatoes
        Examples:
            | pieces | pieces_eaten | pieces_left |
            | 6      | 3            | 3           |
            | 1      | 1            | 0           |

    @TR-C188 @TR-C189 @automated
    Scenario Outline: Test with examples and tags onions
        Given I have <pieces> onions
        When I eat <pieces_eaten> onions
        Then I should have <pieces_left> onions
        Examples:
            | pieces | pieces_eaten | pieces_left |
            | 6      | 3            | 3           |
            | 1      | 1            | 0           |
