# DO NOT CHANGE THIS FILE
# CHANGING THIS WILL BREAK 'driver.py'

BATTING_CHOICES = [1, 2, 3, 4, 5, 6]
BOWLING_CHOICES = [1, 2, 3, 4]

batting_schema = {
        1: 1, #one
        2: 2, #two
        3: 3, #three
        4: 4, #four
        5: 0, #out
        6: 6  #six
    }

bowling_schema = {
    1: 0, #ball
    2: 1, #wide
    3: 1, #no_ball
    4: 0, #bouncer
}