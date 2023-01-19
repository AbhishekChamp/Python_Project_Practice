import random

def computer_guess(start, stop):
    feedback = ''
    count = 0
    while feedback != 'c':
        if start != stop:
            guess = random.randint(start, stop)
        else:
            guess = start
        count+= 1
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").casefold()
        if feedback == 'h':
            stop = guess - 1
        elif feedback == 'l':
            start = guess + 1
            
    print(f"The computer guessed the number {guess} in {count} chances.")
    
start = int(input("Enter the first number in the range: "))
stop = int(input("Enter the last number in the range: "))
computer_guess(start, stop)