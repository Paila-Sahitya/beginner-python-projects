import re
from getpass import getpass

def password_strength_checker():
    print("\n🔐 Welcome to Password Strength Checker! ")
    is_done= False

    while not is_done:
        try:
            password=getpass("Enter your password to verify (input hidden): ").strip()
            if not password:
                print("⚠️ Please enter a password!")
                continue
            
            # check password conditions
            length_check=len(password)>=8
            has_lower = re.search(r"[a-z]", password) is not None
            has_upper = re.search(r"[A-Z]", password) is not None
            has_digit = re.search(r"\d", password) is not None
            has_special = re.search(r"[!@#$%^&*(),.?:;{}|<>]", password) is not None

            score=sum([length_check, has_lower, has_upper, has_digit, has_special])

            bar="█"*score + "░"*(5-score)
            print(f"\nPassword Strength: [{bar}] ({score}/5)")

            if score<=2:
                print("❌ Weak Password.")
            elif score==3 or score==4:
                print("⚠️ Moderate Password.")
            else:
                print("✅ Strong Password!")
            

            # Individual feedback
            if not length_check:
                print("- Length must be at least 8 characters.")
            if not has_lower:
                print("- Add lowercase letters (a-z).")
            if not has_upper:
                print("- Add uppercase letters (A-Z).")
            if not has_digit:
                print("- Add digits (0-9).")
            if not has_special:
                print("- Add special characters (!@#$%^&* etc.).")
            
            print()           
        
        except KeyboardInterrupt:
            print("\nExiting Password Checker.")
            break

        check=input("Do you want to verify for another password? (y/n): ").lower().strip()
        if check=='n':
            is_done= True
            print("✨ Thanks for using Password Strength Checker!")

password_strength_checker()