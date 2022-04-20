from behave import *
from hamcrest import *
import logging

@given('the kinds of fruits sold in an online fruit shop')
def step_impl(context):
    logging.debug(context.text)
    context.fruit_kinds = context.text

@when('i add a "{fruit}" to my shopping cart')
def step_impl(context, fruit):
    shopping_cart = [fruit]
    context.shopping_cart = shopping_cart
    logging.debug(context.shopping_cart)

@when('add more fruits to my shopping cart')
def step_impl(context):
    for row in context.table:
        context.shopping_cart.append(row["fruit_name"])
    logging.debug(context.shopping_cart)

@then('i have following fruits in my shopping cart')
def step_impl(context):
    expected_fruits = [ row["fruit_name"] for row in context.table ]
    logging.debug(expected_fruits)
    assert_that(expected_fruits, has_items(*context.shopping_cart))

@then('unable to buy "{fruit}" successfully')
def step_impl(context, fruit):
    assert_that(context.fruit_kinds, is_not(contains_string(fruit)))
