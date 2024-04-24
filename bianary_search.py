def bianary_search():
    print("Pick a number in your mind and I'll try to guess it!")

    low = 1
    high = 100

    while True:
        guess = (low + high) // 2
        print(f"Is it {guess}?")
        response = input("yes or no: ")

        if response == "yes":
            print("I got it! And you thought you were smarter then me?? lol")
            break
        elif response == "no":
            print("Was that too high or too low?")
            feedback = input("too high or too low: ")
            if feedback == "too high":
                high = guess - 1
            elif feedback == "too low":
                low = guess + 1
            else:
                print("Invalid input. Please enter 'too high' or 'too low'.")

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    print("Are you ready (yes or no): ")
    ready = input()
    if ready == "yes":
        bianary_search()
    else:
        print("Okay, let me know when you're ready!")
