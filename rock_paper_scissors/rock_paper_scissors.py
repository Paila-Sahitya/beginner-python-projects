import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    choices=['rock', 'paper', 'scissors']
    is_done=False

    while not is_done:
        try:
            computer_choice=random.choice(choices)
            user_choice=input("Enter your choice (rock, paper, scissors): ").strip().lower()

            if user_choice not in choices:
                print("❌ Invalid choice! Please choose rock, paper, or scissors.")
                continue

            print(f"\n🧠 Computer chose: {computer_choice}")
            print(f"👤 You chose: {user_choice}")

            if computer_choice == user_choice:
                print("🤝 It's a draw!")
            elif((computer_choice == 'rock' and user_choice == 'scissors') or 
                 (computer_choice == 'scissors' and user_choice == 'paper') or 
                (computer_choice == 'paper' and user_choice == 'rock')
            ):
                print("💻 Computer wins!")
            else:
                print("🎉 You win!")

        except ValueError:
            print("⚠️ Invalid input!")
        
        check=input("Do you want to play again? (y/n): ").strip(). lower()
        if check == 'n':
            is_done=True
            print("Thanks for playing! ")

rock_paper_scissors()