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
        elif chosen_operation == "3":
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

                # calculate the product and print the result
                result = number_1 * number_2
                print("\nThe product is:", result)

            # if the user entered an invalid response, catch the exception and print an error message
            except ValueError:
                print("Invalid input")


        # if user chooses division
        elif chosen_operation == "4":
            # perform a while loop until a valid solution for division is performed or user chose to exit
            while True:
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

                    # calculate the quotient and print the result
                    result = number_1 / number_2
                    print("\nThe quotient is:", result)
                    # break out of the loop
                    break

                # if the user entered a division by zero error, catch the exception and print an error message
                except ZeroDivisionError:
                    print("Invalid input, division by zero error.")

                # if the user entered an invalid input, catch the exception made and print an error message
                except ValueError:
                    print("Invalid input")

                # perform a while loop to ask the user if they want to divide again
                while True:
                    another_input = input("Would you like to try dividing again? (YES/NO): ")
                    # if yes, break out of the inner loop and repeat the division operation
                    if another_input.upper() == "YES":
                        break
                    # if no, return from the function and exit
                    elif another_input.upper() == "NO":
                        return
                    
                    # if user entered an invalid response, ask the user to enter either 'YES' or 'NO'
                    else:
                        print("Invalid reply. Please enter 'YES' or 'NO'")
          

        # if user entered an invalid operation,
        else:
            # print an error message
            print("Invalid input")

        # ask user if they want to solve again
        new_computation = str(input("Would you like to solve again? (YES/NO): "))

        # if the user answered yes,
        if new_computation.upper() == "YES":
            # call the calculator function to repeat the process
            calculator()

        # if the user answered no,
            # print thank you and exit the program

        # if user entered an invalid response, print an error message


        # break out of the loop


# call the function
calculator()