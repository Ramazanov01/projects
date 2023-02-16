import random 

"""def guess(x):
    random_number=random.randint(1, x)
    guess = 0
    # here controlled random number /print("{}".format(random_number)) /
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}:"))
        if(guess > random_number):
            print("Too high number")
        elif(guess < random_number):
            print("Too low number")
    print(f"Qongratulate.Number found {guess}")
guess(10)  """

def camputer_guess(x):
    low = 1
    high = x
    letter = ''
    while letter != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        letter = input(f"Is { guess } is too high h,too low l,or correct c :").lower()
        if letter == 'l':
            low = guess + 1
        elif letter == 'h':
            high = guess - 1
    print("Congratulate.Number found {}".format(guess))

camputer_guess(100)
        