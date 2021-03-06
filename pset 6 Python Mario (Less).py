"""
    [PROGRAM] :  Super Mario Brothers,
    [AUTHOR]  :  Saddam Arbaa
    [Email]   :  <saddamarbaas@gmail.com>
    Python Program to Implement CS50x 2020 Problem Set 6
    Super Mario Brothers(the less comfortable)
    Link to the Week 6 lecture
    CS50 2019 - Lecture 6 - Python
    https://youtu.be/fL308_-Kbt0  """

from cs50 import get_int  # include  get_int function

# define main function
def main():
    # asking user input (positive number)
    userIput = get_positive_int()  # call get_positive_int() function
    # Draw Mario
    # call mario function
    Mario(userIput)

# function to implement Super Mario Brothers
def Mario(Height):

    # iterate over the user input(outer loop)
    for Row in range(Height):
        # first inner loop to print spaces
        for spaces in range(Height - Row - 1):
            # print spaces
            print(' ', end="")
        # second inner loop to print hashes
        for hashes in range(Row + 1):
            # print hashes
            print("#", end="")
        # new line
        print()

# function to get positive integer number between 1 and 8
def get_positive_int():
    while True:
        # prompt the user for positive Number
        number = get_int("Enter a positive Number : ")
        # number must be between 1 and 8, inclusive.
        if number >= 1 and number <= 8:
            break
    return number

# call main
main()
