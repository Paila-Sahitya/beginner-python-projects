import random

print("🎯 Welcome to the Number Guessing Game!")
number=random.randint(1, 100)
guessed=False
attempts=0

while not guessed:
    try:
        guess=int(input("Enter your guess (1-100): "))
        attempts+=1
        if 1 <= guess <= 100:
            if guess==number:
                print(f"✅ You guessed it in {attempts} tries! The number was {number}.")
                guessed=True
            elif guess<number:
                print("🔼 Try higher!")
            else:
                print("🔽 Try lower!")
        else:
            print("⚠️ Please enter a valid number between 1 and 100.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

print("🎉 Thanks for playing!")