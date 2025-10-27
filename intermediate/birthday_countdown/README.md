# 🎂 Birthday Countdown

A simple **Python** command-line program that tells you how many days are left until your next birthday.

---

## 🧠 How It Works
- The user enters their **date of birth** in the format `dd/mm/yyyy`.  
- The program calculates the number of days remaining until the next birthday.  
- If the birthday for the current year has already passed, it will automatically check for the next year.  
- Handles invalid date formats gracefully.  
- Allows repeated calculations until the user chooses to exit.  

---

## 🖥️ Example Output

``` text
🎂 Welcome to the Birthday Countdown!
Enter your date of birth (dd/mm/yyyy): 20/03/2000
🎈 Your next birthday is in 144 days! 🎉
Do you want to continue? (y/n): n
🎉 Thanks for using the Birthday Countdown!
```

---

## 🧩 Features
- 🎂 Calculates days left until next birthday  
- 📅 Handles past and upcoming birthdays automatically  
- ⚠️ Input validation for incorrect formats  
- 🔁 Repeat until user exits  
- ✨ Friendly console messages  

---

## 🧱 Concepts Used
- `datetime` module (`datetime.strptime`, `date.today()`)  
- Loops  
- Conditional statements  
- Exception handling (`try-except`)  
- Date arithmetic  
- String formatting (`f-strings`)  