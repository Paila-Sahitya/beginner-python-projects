# 🎮 Rock-Paper-Scissors

A fun and interactive **Python** command-line game where you compete against the computer in the classic Rock-Paper-Scissors match!

---

## 🧠 How It Works
- The user chooses between rock, paper, or scissors.  
- The computer randomly picks one of the three options.
- The winner is decided based on the standard game rules:
    - ✊ Rock beats Scissors  
    - ✋ Paper beats Rock  
    - ✌️ Scissors beat Paper  
- The game continues until the user chooses to exit.

---

## 🖥️ Example Output
```text
🎮 Welcome to Rock-Paper-Scissors!
Enter your choice (rock, paper, scissors): paper

🧠 Computer chose: rock
👤 You chose: paper
🎉 You win!
Do you want to play again? (y/n): y
Enter your choice (rock, paper, scissors): paper

🧠 Computer chose: rock
👤 You chose: paper
🎉 You win!
Do you want to play again? (y/n): n
Thanks for playing! 
```

---

## 🧩 Features
- 🎲 Randomized computer choice
- 🧠 Intelligent winner logic
- ⚠️ Input validation for incorrect choices
- 🔁 Replay option until user exits
- ✨ Friendly console messages

---

## 🧱 Concepts Used
- `random.choice()` for generating computer's move
- Conditional statements (`if-elif-else`)
- Loops for repeated gameplay
- String methods (`strip()`, `lower()`)
- User input handling and validation