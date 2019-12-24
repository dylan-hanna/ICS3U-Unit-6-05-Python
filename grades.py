#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program uses lists to find average


def averageCalculated(numbers, count):
    # This function takes the average of the marks
    # process
    average = round(sum(numbers) / count)
    # returns average
    return average


def main():
    # This function takes input of users marks
    # list of marks
    numbers = []
    # marks they enter
    temp_word = None
    # how many marks they enter
    count = 0

    print("Please enter 1 mark at a time. Enter -1 to end.")

    # input
    temp_word = int(input("Enter your mark: "))
    numbers.append(temp_word)

    try:
        # process
        while temp_word != -1:
            temp_word = int(input("Enter your mark: "))
            count += 1
            numbers.append(temp_word)

        numbers.pop()  # remove the "-1" that was added
        print("")

        # enters average calculator function
        average = averageCalculated(numbers, count)
        # prints average
        print("Your average is", average)
    # prevents crashes
    except ValueError:
        print("")
        print("Invalid Input")


if __name__ == "__main__":
    main()
