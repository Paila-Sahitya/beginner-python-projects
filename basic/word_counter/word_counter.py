def word_counter():
    print("📝 Welcome to Word Counter:")
    is_done= False

    while not is_done:
        try: 
            text=input("Enter your text: ").strip()
            if not text:
                print("⚠️ Please enter some text!")
                continue

            words=text.split()
            count=len(words)

            print(f"🔢 Word Count: {count}")

        except Exception:
            print("⚠️ Invalid Input! Please try again.")
        
        check=input("Do you want to continue? (y/n): ").lower().strip()
        if check=='n':
            is_done=True
            print("✨ Thanks for using Word Counter!")
        
word_counter()