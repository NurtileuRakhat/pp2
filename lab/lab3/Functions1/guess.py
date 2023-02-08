import random
def guess():
    Number = random.randint(1, 4)
    guess = None
    count = 0
    name = input("Hello! What is your name?\n")
    print("Well, {} , I am thinking of a number between 1 and 20.".format(name))
    while True:
        guess = int(input("Take a guess:\n"))
        count += 1
        if(guess < Number):
            print("Your guess is too low.")
        elif(guess > Number):
            print("Your guess is too big.")
        else:
            print("Good job, {}! You guessed my number in {} guesses!".format(name, count))
            break
guess()