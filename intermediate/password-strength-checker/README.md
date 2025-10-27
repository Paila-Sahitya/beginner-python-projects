# 🔐 Password Strength Checker

A **Python** based command-line tool that helps users evaluate the strength of their passwords based on multiple security factors such as length, character variety, and use of special symbols.

---

## 🧠 How It Works
- The user securely enters a password (input is hidden for privacy).
- The program analyzes the password for:
    - Minimum length (8+ characters)  
    - Presence of lowercase letters  
    - Presence of uppercase letters  
    - Presence of digits  
    - Presence of special characters  
- Displays a **visual strength bar** and provides *personalized feedback* for improvement.

---

## 🖥️ Example Output
```text
🔐 Welcome to Password Strength Checker!
Enter your password to verify (input hidden):

Password Strength: [███░░] (3/5)
⚠️ Moderate Password.
- Add digits (0-9).
- Add special characters (!@#$%^&* etc.).

Do you want to verify for another password? (y/n): n       
✨ Thanks for using Password Strength Checker!
```

---

## 🧩 Features
- 🛡️ Hidden password input using getpass
- 🧮 Visual strength bar for easy understanding
- 💬 Detailed feedback for weak points
- 🔁 Option to check multiple passwords in one session
- ✨ User-friendly CLI interface

---

## 🧱 Concepts Used
- Regular Expressions (`re` module) for pattern detection
- Conditional logic and scoring system
- String manipulation and secure input handling
- Loops and exception handling for smooth UX

## 🛠️ Tech Stack
- Python 3.x
- `re` module
- `getpass` module