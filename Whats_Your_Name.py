while True:
    try:
        #request users age
        age = int(input("How old are you? "))
        if age < 0:
            #check if users age is a positive number
            print("invalid input, enter a positive number")
            continue
        else:
            #if users age is an accepted value, return users age + 5
            new_age = age + 5
            print(f"In 5 years you will be {new_age} years old!")
            break
    except ValueError:
        #handles if user inputs a non numerical value
        print("Invalid input, choose a numerical value")