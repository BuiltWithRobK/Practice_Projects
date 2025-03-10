while True:
    try:

        UserInput = input("Enter a word or phrase. ").strip()
    

        if UserInput.lower() == "exit":
            print("Exiting Program...")
            break
        
        ReversedIN = "".join(reversed(UserInput))
        print(ReversedIN)
        
    except ValueError:
        print("Invalid input, please enter a word or phrase.")


