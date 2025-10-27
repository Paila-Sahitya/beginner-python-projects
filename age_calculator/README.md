# 📅 Age Calculator

A simple **Python** command-line program that calculates a person's age based on their date of birth.

---

## 🧠 How It Works
- The user enters their **date of birth** in the format `dd/mm/yyyy`.
- The program calculates their age in years using the current date.
- Handles invalid date formats gracefully.
- Allows repeated calculations until the user chooses to exit.

---

## 🖥️ Example Output

``` 📅 Welcome to the Age Calculator!
Enter your date of birth (dd/mm/yyyy): 20/03/2000
🎉 You are 25 years old! 🎂
Do you want to calculate another age? (y/n): n
Thanks for using the Age Calculator!
```

---

## 🧩 Features
- 📆 Calculates accurate age based on date of birth
- ⚠️ Handles invalid date formats
- 🔁 Repeat until user exits
- ✨ Clean and friendly console output

---

## 🧱 Concepts Used
- `datetime` module (`datetime.strptime`, `date.today()`)
- Loops
- Conditional statements
- Exception handling (`try-except`)
- String formatting (`f-strings`)