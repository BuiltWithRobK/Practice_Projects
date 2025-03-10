import random
rand_number = random.randint(1,100)

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:

        user_guess = (int(input("\nwhat number do you guess? ")))

        if user_guess < 1 or user_guess > 100:
            print("Invalid Input, chose a number between 1 and 100")

        elif user_guess == rand_number:
            print("Congratulations! you guessed the number!")
            break

        elif user_guess < rand_number:
            print("Too low, try again.")

        elif user_guess > rand_number:
            print("Too high, try again.")

    except ValueError:
        print("Invalid Input, please enter a number.")