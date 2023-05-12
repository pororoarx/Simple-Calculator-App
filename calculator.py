# A simple calculator app


# start
# print a welcome message
print("Hello! Welcome to Ken's Calculator App")

# print the operations that users can pick from
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

# define a function called calculator
def calculator():
    # perform a while loop until the user decided to exit the loop
    while True:
        # ask user to enter an operation
        chosen_operation = input("Choose one of the four operations: ")

        # if user chooses addition
        if chosen_operation == "1":
            # ask the user to enter two numbers
            number_1 = input("Enter your first number: ")
            number_2 = input("Enter your second number: ")

            # try
            try:
                # convert both inputs to float if one or both of the inputs made by user is a float
                if "." in number_1 or "." in number_2:
                    number_1 = float(number_1)
                    number_2 = float(number_2)
                # otherwise, convert both inputs made by user to integers
                else:
                    number_1 = int(number_1)
                    number_2 = int(number_2)

                # calculate the sum and print the result
                result = number_1 + number_2
                print("\nThe sum is:", result)

            # if the user entered an invalid response, catch the exception and print an error message
            except ValueError:
                print("Invalid input")


        # if user chooses subtraction
        elif chosen_operation == "2":
            # ask the user to enter two numbers
            number_1 = input("Enter your first number: ")
            number_2 = input("Enter your second number: ")

            # try
            try:
                # convert both inputs to float if one or both of the inputs made by user is a float
                if "." in number_1 or "." in number_2:
                    number_1 = float(number_1)
                    number_2 = float(number_2)
                # otherwise, convert both inputs made by user to integers
                else:
                    number_1 = int(number_1)
                    number_2 = int(number_2)

                # calculate the difference and print the result
                result = number_1 - number_2
                print("\nThe difference is:", result)
              
            # if the user entered an invalid response, catch the exception and print an error message
            except ValueError:
                print("Invalid input")


        # if user chooses multiplication
            # ask the user to enter two numbers

            # try
                # convert both inputs to float if one or both of the inputs made by user is a float
                # otherwise, convert both inputs made by user to integers

                # calculate the product and print the result

            # if the user entered an invalid response, catch the exception and print an error message


        # if user chooses division
            # perform a while loop until a valid solution for division is performed or user chose to exit

                # ask the user to enter two numbers

                # try
                    # convert both inputs to float if one or both of the inputs made by user is a float
                    # otherwise, convert both inputs made by user to integers

                    # calculate the quotient and print the result
                    # break out of the loop

                # if the user entered a division by zero error, catch the exception and print an error message

                # if the user entered an invalid input, catch the exception made and print an error message

                # perform a while loop to ask the user if they want to divide again
                    # if yes, break out of the inner loop and repeat the division operation
                    # if no, return from the function and exit
                    
                    # if user entered an invalid response, ask the user to enter either 'YES' or 'NO'

        # ask user if they want to solve again

        # if the user answered yes,
            # call the calculator function to repeat the process

        # if the user answered no,
            # print thank you and exit the program

        # if user entered an invalid response, print an error message


        # break out of the loop


# call the function
calculator()