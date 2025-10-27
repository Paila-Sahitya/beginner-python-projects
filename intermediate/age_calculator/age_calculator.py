from datetime import date, datetime

def age_calculator():
    print("📅 Welcome to the Age Calculator!")
    is_done= False

    while not is_done:
        try:
            dob_input=input("Enter your date of birth (dd/mm/yyyy): ")
            dob=datetime.strptime(dob_input, "%d/%m/%Y").date()
            today=date.today()
            
            age=today.year-dob.year-((today.month, today.day) < (dob.month, dob.day))

            print(f"🎉 You are {age} years old! 🎂")
            
        except ValueError:
            print("⚠️ Invalid date format. Please enter in dd/mm/yyyy format.")
            continue

        check=input("Do you want to calculate another age? (y/n): ").strip().lower()
        if check=='n':
            is_done= True
            print("Thanks for using the Age Calculator!")

age_calculator()