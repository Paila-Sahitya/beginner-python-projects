from datetime import date, datetime

def days_until_birthday():
    print("🎂 Welcome to the Birthday Countdown!")
    is_done=False

    while not is_done:
        try:
            dob_input=input("Enter your date of birth (dd/mm/yyyy): ")
            dob=datetime.strptime(dob_input, "%d/%m/%Y").date()
            today=date.today()
            
            next_birthday=date(today.year, dob.month, dob.day)

            if next_birthday < today:
                next_birthday=date(today.year+1, dob.month, dob.day)
            
            days_left= (next_birthday - today).days

            print(f"🎈 Your next birthday is in {days_left} days! 🎉")
        except ValueError:
            print("⚠️ Invalid date format. Please use dd/mm/yyyy.")
        
        check=input("Do you want to continue? (y/n): ").strip().lower()
        if check=='n':
            is_done=True
            print("🎉 Thanks for using the Birthday Countdown!")
    
days_until_birthday()