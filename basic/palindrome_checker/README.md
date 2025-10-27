# 🔁 Palindrome Checker

A simple **Python** command-line program that checks whether a given word or phrase is a palindrome — reads the same forward and backward!

---

## 🧠 How It Works
- The user enters any word, sentence, or sequence of characters.
- The program removes spaces and ignores letter casing.
- It then reverses the cleaned text and checks if it matches the original.
- The result is displayed instantly, and the user can continue checking multiple inputs.

---

## 🖥️ Example Output
```text
🔁 Welcome to the Palindrome Checker!
Enter a set of characters: RaceCar
✅ It's a Palindrome!
Do you want to check another word? (y/n): y
Enter a set of characters: hello world
❌ Not a palindrome.
Do you want to check another word? (y/n): n
✨ Thanks for using Palindrome Checker!
```

---

## 🧩 Features
- 🔡 Case-insensitive palindrome checking
- 🧹 Ignores spaces for multi-word phrases
- ⚠️ Handles invalid or empty inputs gracefully
- 🔁 Option to check multiple words or phrases
- ✨ Clean and interactive console experience

---

## 🧱 Concepts Used
- string slicing (`[::-1]`) for reversal  
- String methods (`lower()`, `split()`, `join()`)  
- Loops and conditionals for repeated checking  
- Input validation and exception handling  