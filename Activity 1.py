import random
playing = True
number = str(random.randint(10,50))

while playing:
    print("I will generate a number. Try to guess it")
    guessed_number = input("Enter your guessed number: ")
    if guessed_number == number:
        print("You are right")
        break

    else:
        print("You are wrong")