from datetime import datetime
current_year = datetime.now().year
while True:
    try:

        birth_year = int(input("What year were you born? "))
        age = current_year - birth_year

        if birth_year > current_year:
            print("Invalid Input, try again")
            continue
        elif birth_year < 1900:
            print("Invalid Input, try again")
            continue
        else:
            print(f"you are {age} years old!")
            break

    except ValueError:
        print("Invalid input, please enter a number")