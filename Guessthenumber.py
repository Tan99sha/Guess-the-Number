a=1
b=100
computer_number=56
max_attempts=2
attempts=0
print("You are welcome to the Guess the Number game!")
print(f"I have thinked of number between {a} and {b}.")
print(f"You have {max_attempts} attempts to guess the number I have thinked.")
while attempts < max_attempts:
    guess=input("Enter your guess: ")
    try:
        guess=int(guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if guess ==computer_number:
        print("Congratulations, you guessed the number!")
        break
    if guess < computer_number:
        print("Too low. Hint: The Sum of six consecutive prime numbers")
    else:
        print("Too high. Hint: The Sum of six consecutive prime numbers")
    attempts+=1
if attempts==max_attempts:
    print("Sorry, you didn't guess the number.")
    print(f"The number was {computer_number}.")