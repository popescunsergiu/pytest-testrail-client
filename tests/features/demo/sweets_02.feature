@DEMO-epicNo @DEMO-storyNo
Feature: Sweets - With Examples
    Sweets tests


    @TR-C183 @TR-C184
    Scenario Outline: Test with examples candies
        Given I have <pieces> candies
        When I eat <pieces_eaten> candies
        Then I should have <pieces_left> candies
        Examples:
            | pieces | pieces_eaten | pieces_left |
            | 6      | 3            | 3           |
            | 1      | 1            | 0           |

    @TR-C181 @TR-C182 @automated
    Scenario Outline: Test with examples and tags chocolates
        Given I have <pieces> chocolates
        When I eat <pieces_eaten> chocolates
        Then I should have <pieces_left> chocolates
        Examples:
            | pieces | pieces_eaten | pieces_left |
            | 6      | 3            | 3           |
            | 1      | 1            | 0           |
