# tip_tax_total_enhanced.py
# Exercises selected: Lab 4.6 - Programming Challenge 1 - Tip, Tax, and Total
# Name of program: Tip Tax Total Enhanced
# Description of program: This program will ask the user to input a meal price
# and displays the cost breakdown of the meal price, tip, tax and the total.
#
# Ivan Boatwright
# February 27, 2016

# Global Constants
SALES_TAX = .06
# BASE_TIPS is a Constant Dictionary with the starting price of each range
#   as the key and the tip percent as a float as the value.
BASE_TIPS = {.01: 0.1, 6: 0.13, 12.01: 0.16, 17.01: 0.19,
                       25.01: .22}

def main():
    # Dictionary array to hold meal cost values
    mealCosts = {'price': 0.0,
                 'tip': 0.0,
                 'tax': 0.0,
                 'total': 0.0}
    # List Constant used for user prompt and input validation.
    #   The first value is the expected input and second is the prompt.
    REQUEST_LIST = [['float and nonnegative', 'price of the meal']]

    # Displays the intro to user.
    fluffy_intro()

    # Assigns user entered meal price after validating entered value.
    mealCosts['price'] = float(get_valid_inputs(REQUEST_LIST))

    # Calculates the meal tax, tip and total and assigns the values
    #   to their respective variables in the mealCosts Dict.
    calc_meal(mealCosts)

    # Displays the costs of the meal to the user.
    display_results(mealCosts)

    # End of main()
    return None



# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('\nWelcome to the Tip, Tax, Total Enhanced program.\n'
          'This program requests the price of a meal and then calculates\n'
          'the meal tip, meal tax, and total cost of the meal.\n'
          'It then displays the results.\n')


# get_valid_inputs requests input from the user then tests the input.
#   If invalid, it will alert the user and request the correct input.
# The parameter is a nested List of ordered pair Lists.
#   First value is the validation test and second is the user prompt.
def get_valid_inputs(requestsList):
    # local List to hold user inputs for return to calling module
    userInputs = []

    # Loop through each entry in requestsList assigning each List pair
    #  to request.
    for request in requestsList:
        # untestedInput is a holding variable for testing user input validity.
        # First user prompt before testing loop.
        untestedInput = prompt_user_for_input(request[1])

        # If test_value returns True, Not converts it to False and the While
        #   Loop will not execute.
        # If test_value returns False, the While executes and the user is
        #   prompted to enter a valid value.
        while (not test_value(request[0], untestedInput)):

            print('!!! Error: {} is not a valid value.'.format(untestedInput))
            untestedInput = (prompt_user_for_input(request[1]))

        # The user input tested valid and is appended to the userInputs List.
        userInputs.append(untestedInput)
    # for loop terminates and userInputs are returned to calling Module.
    # With only a single test run in this program, only the first value
    #   in userInputs is returned.
    return userInputs[0]


# prompt_user_for_item is passed a String to print to screen as part of a user
#   prompt.  Then returns it to the calling module.
def prompt_user_for_input(promptTerm):
    # promptTerm is a local variable to hold the value passed from the
    #   calling module.
    print('Please enter your {}.'.format(promptTerm))
    return input('  >> ')


# test_value uses the testCondition to select the proper test.
# It returns True or False to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition == 'float and nonnegative':
        # If float(testItem) is greater than or equal to zero True is
        #  returned.  If float(testItem) creates an error or is less than
        #  zero False is returned.
        try:
            if float(testItem) >= 0:
                return True
            else:
                return False
        except:
            return False
    else:
        return None
    

# calc_meal is passed a reference to the mealCosts array which now contains
#   the validated user input meal price.
def calc_meal(mCosts):
    mCosts['tax'] = mCosts['price'] * SALES_TAX
    mCosts['tip'] = mCosts['price'] * calc_tip(mCosts['price'])
    mCosts['total'] = mCosts['tax'] + mCosts['tip']
    return None
    

# calc_tip is passed the meal price and returns the tip multiplier in
#   in decimal form to the calling function.
def calc_tip(mPrice):
    # This creates a List of the keys from the BASE_TIPS global dict and
    # sorts them in reverse order from highest to lowest (25.01 to 0.01).
    tipRanges = sorted(BASE_TIPS.keys(),reverse=True)

    # The for loop uses reverse() to start at the end of the keys list
    #   and assigns the current key to the variable range.
    for range in tipRanges:

        # If the meal price is greater than or equal to the current
        #   BASE_TIP key then return the value associated with that key.
        if mPrice >= range:
            return BASE_TIPS[range]
    # Should never get to this statement.
    return None


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(mCosts):
    # This formats the values stored in mCosts before printing to the screen.
    for key in list(mCosts.keys()):
        mCosts[key] = '${:,.2f}'.format(mCosts[key])

    # This shows the meal cost breakdown and total.
    print('\nThe meal breakdown is as follows:\n')
    print('   Price {:>27}'.format(mCosts['price']))
    print('   Tax {:>29}'.format(mCosts['tax']))
    print('   Tip {:>29}'.format(mCosts['tip']))
    print('   {:-<33}'.format(''))
    print('   Total {:>27}'.format(mCosts['total']))
    return None
    
# Call the main module.    
main()