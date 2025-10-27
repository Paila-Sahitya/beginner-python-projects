def palindrome_checker():
    print("🔁 Welcome to the Palindrome Checker!")
    is_done=False

    while not is_done:
        try:
            text=input("Enter a set of characters: ").strip()
            
            cleaned_text=''.join(text.lower().split())
            reversed_text=cleaned_text[::-1]
            if cleaned_text==reversed_text:
                print("✅ It's a Palindrome!")
            else:
                print("❌ Not a palindrome.")
        
        except Exception as e:
            print("⚠️ Invalid Input, please try again.")

        check=input("Do you want to check another word? (y/n): ").strip().lower()
        if check=='n':
            is_done=True
            print("✨ Thanks for using Palindrome Checker!")

palindrome_checker()