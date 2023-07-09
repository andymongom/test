"""
    Program that simulates the game of whomever
    choose the smallest stick, loses
"""

import random


def mix_sticks(sticks_list):
    """
    Function to shuffle a list
    :param sticks_list: list
    :return: list
    """
    random.shuffle(sticks_list)
    return sticks_list


def validate_selection(sticks_list):
    """
    Validate correct selection from the user
    :param sticks_list:list
    :return: int
    """
    option = ""
    while option not in range(1, len(sticks_list)+1):
        # Try and except is used to catch the error if the player's input fails to convert it doesn't break the code
        try:
            option = int(input(f"Please enter a number between 1 and {len(sticks_list)}:\n "))
            # the lenght of the list changes in every try
        except ValueError:
            print("Invalid value, please try again.")
    return option


def choose_stick(sticks_list, choosing):
    """
    Function to choose the stick and see if you lose
    :param sticks_list: list
    :param choosing: int
    """
    stick = sticks_list.pop(choosing - 1)  # we remove the chosen option
    if len(stick) == 1:
        print("Ohhh, you are doomed!")
        print("You wash the dishes")
        return True
    else:
        print("Phew, you are safe...for now")
    print(f"You got {stick}")
    return False


sticks = ["-", "--", "---", "----", "-----"]
mixed_sticks = mix_sticks(sticks)

game_over = False
while not game_over:
    correct_selection = validate_selection(mixed_sticks)
    game_over = choose_stick(mixed_sticks, correct_selection)
