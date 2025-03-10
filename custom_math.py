while True:
    try:
        number1 = int(input("Pick a first number: "))
        number2 = int(input("Pick a second number: "))
        operation = input("Pick an operator (+, -, *, /): ")

        # Check and perform the operation
        if operation == "+":
            outcome = number1 + number2
        elif operation == "-":
            outcome = number1 - number2
        elif operation == "*":
            outcome = number1 * number2
        elif operation == "/":
            if number2 == 0:
                print("Cannot divide by 0. Try again.")
                continue  # Skip to next iteration if division by zero
            else:
                outcome = number1 / number2
        else:
            print("Invalid operator. Try again.")
            continue  

        # Display the result
        print(f"Result: {number1} {operation} {number2} = {outcome}")

        # Exit the loop after printing the result
        break

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
