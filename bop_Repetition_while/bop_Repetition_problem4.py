import random
secret_number = random.randint(0,100)
print('Guess the number(1-100):')
guess = int(input())
number_of_guesses = 0
while guess != secret_number:
    if guess < secret_number:
        print('too low')
    if guess > secret_number:
        print('too high')
    number_of_guesses +=1
    guess = int(input('Guess the number again:'))
print(f"You guessed it right! it's {secret_number}. Number of guesses: {number_of_guesses}")