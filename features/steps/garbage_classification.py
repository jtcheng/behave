from behave import *
from hamcrest import *
import requests
import logging

@when('perform a "{garbage}" classification http request to the web services')
def step_impl(context, garbage):
    context.garbage = garbage
    response = requests.get(context.web_services + '/?keyword=' + garbage)
    logging.debug(response.status_code)
    context.response = response

@then('verify the result classification "{classification}"')
def step_impl(context, classification):
    response_json = context.response.json()
    logging.debug(response_json)
    newslist = response_json["newslist"]
    for garbage in newslist:
        if garbage["name"] == context.garbage:
            assert_that(garbage["title"], equal_to(classification))
