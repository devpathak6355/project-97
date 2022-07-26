import random
print("Number Guessing Game")
num = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9)")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if guess == num:
        print("Congratulation YOU WON!!!")
        break
    elif guess < num:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    chances += 1
if not chances < 5:
    print("YOU LOSE!!! The number is", num)
