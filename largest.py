#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program finds the largest of 10 random numbers

import random


def find_largest(list_of_numbers):
    # this function finds the largest number in a list

    largest = list_of_numbers[9]

    for loop_counter in range(0, 9):
        if list_of_numbers[loop_counter] > largest:
            largest = list_of_numbers[loop_counter]
        else:
            largest = largest

    return largest


def main():
    # this function creates 10 random numbers in a list

    list_of_numbers = []

    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)  # a number between 1-100
        list_of_numbers.append(random_number)
        print("The random number is : {0}".format(random_number))
        loop_counter += 1

    largest_number = find_largest(list_of_numbers)

    print("\n\nThe largest number is {0}".format(largest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
