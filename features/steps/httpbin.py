from behave import *
from hamcrest import *
import requests
import logging

@given('a web services "{web_services}"')
def step_impl(context, web_services):
    context.web_services = web_services

@when('perform a "{http_method}" http request to the web services')
def step_impl(context, http_method):
    response = requests.request(http_method, context.web_services + '/' + http_method)
    logging.debug(response.status_code)
    context.response = response

@then('verify the response status code "{status_code}"')
def step_impl(context, status_code):
    assert_that(str(context.response.status_code), equal_to(status_code))

@given('an encoded string "{base64_string}" and a web services "{web_services}"')
def step_impl(context, base64_string, web_services):
     context.base64_string = base64_string
     context.execute_steps(u'''
         Given a web services "{web_services}"
     '''.format(web_services=web_services))

@when('perform a http request to decode the encoded string')
def step_impl(context):
    response = requests.get(context.web_services + '/' + context.base64_string)
    logging.debug(response.status_code)
    context.response = response

@then('verify the decoded string "{raw_string}"')
def step_impl(context, raw_string):
    assert_that((context.response.text).strip(), equal_to(raw_string))
