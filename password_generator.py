import random
import string

def generate_password(length=12):
    # इसमें ABCD, 1234 और स्पेशल कैरेक्टर्स शामिल हैं
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("--- Simple Password Generator ---")
    try:
        user_length = int(input("Enter password length (e.g., 8, 12, 16): "))
        if user_length < 4:
            print("Password length should be at least 4 characters.")
        else:
            print("Your secure password is:", generate_password(user_length))
    except ValueError:
        print("Error: Please enter a valid number!")
      
