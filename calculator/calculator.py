def calculator():
    print("🧮 Welcome to the Calculator!")
    is_done=False

    while not is_done :
        try:
            op=input("Choose an operation (+, -, *, /): ").strip()
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))

            if op=='+':
                print(f"✅ Result: {a+b}")
            elif op=='-':
                print(f"✅ Result: {a-b}")
            elif op=='*':
                print(f"✅ Result: {a*b}")
            elif op=='/':
                if b==0:
                    print("⚠️ Cannot divide by Zero!")
                else:
                    print(f"✅ Result: {a/b}")
            else: 
                print("⚠️ Invalid operator. Please choose +, -, * or /.")
        
        except ValueError:
            print("🚫 Invalid input. Please enter numeric values.")
        
        check=input("Do you want to continue? (y/n): ").strip().lower()
        if(check=='n'):
            is_done=True
            print("👋 Thanks for using the calculator.")

calculator()