# tip_tax_total_enhanced.py
# Exercises selected: Lab 4.6 - Programming Challenge 1 - Tip, Tax, and Total
# Name of program: T3E, Tip Tax Total Enhanced
# Description of program: This program will ask the user to input a meal price
# and displays the cost breakdown of the meal price, tip, tax and the total.
#
# Ivan Boatwright
# February 23, 2016

# Global Constants
SALES_TAX = .06
# baseTips is a Dictionary with the starting price of each range as the key
#   and the tip percent as a float as the value.
BASE_TIPS = {.01: 0.1, 6: 0.13, 12.01: 0.16, 17.01: 0.19,
                       25.01: .22}

def main():
    # Local variables
    mealPrice = 0.0
    mealTax = 0.0
    mealTip = 0.0
    mealTotal = 0.0
    # List used for user prompt and input validation.
    #   The first value is the expected input and second is the prompt.
    requestList = [['float', 'price of the meal']]

    # Display intro to user.
    fluffy_intro()

    # Control loop for main()
        #todo: add a while loop and a menu for 1) calculate another meal,
        #todo:   0) exit
    # Assigns user entered meal price after validating entered value.
    mealPrice = get_valid_inputs(requestList)

    # Assigns meal Tax, Tip and Total to their respective variables
    mealTax, mealTip, mealTotal = calc_meal(mealPrice)

    # Display the costs of the meal to the user.
    display_results(mealPrice, mealTax, mealTip, mealTotal)

    # End of main()
    return None



# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Tip, Tax, Total Enhanced program.'
          'This program requests the price of a meal and then calculates'
          'the meal tip, meal tax, and total cost of the meal.'
          'It then displays the results.')

#todo: add the rest of the functions.