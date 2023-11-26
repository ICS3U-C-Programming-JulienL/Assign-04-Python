#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 26, 2023
# This program displays a sin or tan table for angles between 0 and 360

import math


def main():
    # ask the user what table they would like to see
    user_table_choice_str = input(
        "This program displays a sin or tan table of all angles from 0 to 360. Press 1 for the sin table and 2 for the tan table: "
    )

    # initialize counter and sin_tan_product to 0
    counter = 0
    sin_tan_product = 0

    try:
        # convert user table choice to an int
        user_table_choice_int = int(user_table_choice_str)

        # if the choice is 1, then use a while loop to find the sin table
        if user_table_choice_int == 1:
            while counter <= 360:
                # calculate the sine of the counter
                sin_tan_product = math.sin(counter)

                # display the sin product
                print("sin {0} = {1}".format(counter, sin_tan_product))

                # increment the counter
                counter = counter + 1
        elif user_table_choice_int == 2:
            # otherwise if the choice is 2, then use a while loop to find the tan table
            while counter <= 360:
                # calculate the tan of the counter
                sin_tan_product = math.tan(counter)

                # display the tan product
                print("tan {0} = {1}".format(counter, sin_tan_product))

                # increment the counter
                counter = counter + 1
        else:
            # otherwise, tell them to enter 1 or 2
            print(" Please enter 1 or 2 for your table choice.")
    except:
        # if user table choice cannot be an int, tell the user to enter one
        print(
            "{} is not valid integer, please enter one.".format(user_table_choice_str)
        )


if __name__ == "__main__":
    main()
