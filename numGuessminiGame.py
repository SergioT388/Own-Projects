import random as r

number = r.randint(1, 100)
attempts = 0

diffSet = int(input("""Welcome to the Number Guessing Game! Please, select a difficulty level:\n
1. Easy (10 attempts)\n
2. Medium (7 attempts)\n
3. Hard (5 attempts)\n
Enter you choice: """ ))

if diffSet == 1:
    attempts = 10
elif diffSet == 2:
    attempts = 7    
elif diffSet == 3:
    attempts = 5

print(f"You have selected difficulty level number {diffSet}")

guess = int(input("Now, try to guess the number between 1 and 100!\nEnter your guess: "))

for i in range(1, attempts, 1):

    i += 1

    if guess == number:
        print(f"Congratulations! You guessed the number on your attempt: {i}!")
        break
    else:

        if guess < number:
            guess = int(input(f"The number is higher than {guess}. Try again: "))

        if guess > number:
            guess = int(input(f"The number is lower than {guess}. Try again: "))   


if i == attempts:
        print("You've 0 attempts left.")
