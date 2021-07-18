from pytest import fail
from pytest_bdd import given, when, then, scenarios, parsers

scenarios('../features/demo/fruits_01.feature',
          '../features/demo/fruits_02.feature',
          '../features/demo/fruits_03.feature',
          '../features/demo/sweets_01.feature',
          '../features/demo/sweets_02.feature',
          '../features/demo/vegetables_01.feature',
          '../features/demo/vegetables_02.feature',
          )


@given("I have <pieces> apples")
@given("I have <pieces> pears")
@given("I have <pieces> cherries")
@given("I have <pieces> onions")
@given("I have <pieces> potatoes")
@given("I have <pieces> carrots")
@given("I have <pieces> chocolates")
@given("I have <pieces> candies")
def i_have_fruites(pieces):
    pass


@given(parsers.re("I have (?P<pieces>.*) apples"),
       converters=dict(fruites=str))
def i_have_fruites_apples(pieces):
    raise Exception('This has to fail for demo purpose')


@when("I eat <pieces_eaten> apples")
@when("I eat <pieces_eaten> pears")
@when("I eat <pieces_eaten> cherries")
@when("I eat <pieces_eaten> onions")
@when("I eat <pieces_eaten> potatoes")
@when("I eat <pieces_eaten> carrots")
@when("I eat <pieces_eaten> chocolates")
@when("I eat <pieces_eaten> candies")
def i_eat_fruites(pieces_eaten):
    pass


@then("I should have <pieces_left> apples")
@then("I should have <pieces_left> pears")
@then("I should have <pieces_left> cherries")
@then("I should have <pieces_left> onions")
@then("I should have <pieces_left> potatoes")
@then("I should have <pieces_left> carrots")
@then("I should have <pieces_left> chocolates")
@then("I should have <pieces_left> candies")
def i_should_have_fruites(pieces_left):
    pass
