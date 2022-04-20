Feature: httpbin
    In order to demo the behave test frameworks
    we chose the open source "https://httpbin.org" as the testing web services

    @HTTP_Methods
    Scenario Outline: http method test
        Given a web services "https://httpbin.org"
        When perform a "<http_method>" http request to the web services
        Then verify the response status code "<status_code>"

        Examples: Perform "<http_method>" request to "https://httpbin.org/<http_method>" and verify the response status code "<status_code>"
        | http_method | status_code |
        | delete      | 200         |
        | get         | 200         |
        | patch       | 200         |
        | post        | 200         |
        | put         | 200         |
        | head        | 404         |
        | options     | 404         |

    @Dynamic_Data
    Scenario Outline: Dynamic data test
        Given an encoded string "<base64_string>" and a web services "https://httpbin.org/base64"
        When perform a http request to decode the encoded string
        Then verify the response status code "<status_code>"
        And verify the decoded string "<raw_string>"

        Examples: Perform a http request to "https://httpbin.org/base64/<base64_string>" to decode string "<base64_string>" and verify the response status code "<status_code>" and the original string "<raw_string>"
        | base64_string | status_code | raw_string |
        | SFRUUEJJTgo=  | 200         | HTTPBIN    |
        | QkVIQVZFCg==  | 200         | BEHAVE     |
