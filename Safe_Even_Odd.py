while True:
    try:
        number = int(input("Input a number to determine if it is odd or even. "))

        if number < 0:
            print("Invalid input, please enter a positive number.")
            continue
        else:
            if number % 2 == 0:
                print(f"{number} is even.")
                break
            else:
                print(f"{number} is odd.")
                break
    except ValueError:
        print("Invalid input, please enter a numberical value")

