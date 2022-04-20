Feature: step parameters
    we can pass some parameters from feature file to python implementation
    we call this as step data

    @Fruit
    Scenario: buy fruits online
        Given the kinds of fruits sold in an online fruit shop
            '''
            Apple
            banana
            mango
            watermelon
            '''
        When i add a "watermelon" to my shopping cart
        And add more fruits to my shopping cart
            | fruit_name |
            |    Apple   |
            |    mango   |
            |    orange  |
        Then i have following fruits in my shopping cart
            | fruit_name |
            |   Apple    |
            |   mango    |
            |   orange   |
            | watermelon |
        But unable to buy "orange" successfully
