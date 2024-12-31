import random

print("Hello Humans")
print("""
    1. Guess a number between 1 to 10
    2. Game will for 3 attempts""")

machine_number = random.randint(1, 10)
# print (f"Machine Number: {machine_number}")
MAX_ATTEMPTS = 3

for attempt in range(MAX_ATTEMPTS):
    user_input = input(f"Round: {attempt} || Please enter your guess: ")
    # print (f"user_input = machine_number {user_input == machine_number}")
    if user_input.isnumeric():
        user_number = int(user_input)
    else:
        print("Please enter a number")
        continue
    if user_number == machine_number:
        print("Congrts, You guessed the correct number.")
        break
    elif user_number > machine_number:
        print("Guess Lower")
    else:
        print("Guess Higher")
else:
    print(f"Thank you for playing the game. \nThe Machine Number is: {machine_number}")