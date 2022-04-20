Feature: garbage classification
    In order to demo the behave test frameworks
    we chose the open source "https://www.api66.cn/api/ljfl.php" as another testing web services

    @wip
    Scenario Outline: garbage classification test
        Given a web services "https://www.api66.cn/api/ljfl.php"
        When perform a "<garbage>" classification http request to the web services
        Then verify the response status code "<status_code>"
        And verify the result classification "<classification>"

        Examples: 有害垃圾测试
        | garbage | status_code | classification |
        | 废电池   | 200         |    有害垃圾     |
        | 过期药品 | 200         |    有害垃圾     |

        Examples: 湿垃圾测试
        | garbage | status_code |classification |
        | 香蕉皮   | 200         |     湿垃圾     |
        | 烂菜叶   | 200         |     湿垃圾     |
