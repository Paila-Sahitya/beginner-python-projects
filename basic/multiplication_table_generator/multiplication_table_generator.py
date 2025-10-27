def multiplication_table():
    print("🔢 Welcome to the Multiplication Table Generator!")
    is_done=False

    while not is_done:
        try:
            number=int(input("Enter a number: "))
            limit=int(input("Generate table up to: "))

            print(f"\n📘 Multiplication Table for {number} (1 to {limit})")
            print("-"*20)

            for i in range(1, limit+1):
                print(f"{number} × {i} = {number*i}")

            print("-"*20)
            
        except ValueError:
            print("🚫 Invalid input. Please enter numeric values only.")
        
        check=input("\nDo you want to generate another table? (y/n): ").strip().lower()
        if check=='n':
            is_done=True
            print("\nThanks for using the Multiplication Table Generator!")


multiplication_table()