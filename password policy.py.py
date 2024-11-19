import re

def is_strong_password(password):
    # Define strong password requirements
    length_check = len(password) >= 8
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[_!@#$%^&*(),.?":{}|<>])')
    character_check = bool(pattern.search(password))

    # Check if all requirements are met
    return length_check and character_check

def get_password_from_user():
    return input("Enter a password: ")

def main():
    while True:
        password = get_password_from_user()

        if is_strong_password(password):
            print("Password accepted. It is strong enough.")
            break
        else:
            print("Password is not strong enough. Please address the following:")
            
            if not len(password) >= 8:
                print("- Password should have a minimum length of 8 characters.")
                
            if not re.search(r'[A-Z]', password):
                print("- Password should include at least one uppercase letter.")
                
            if not re.search(r'[a-z]', password):
                print("- Password should include at least one lowercase letter.")
                
            if not re.search(r'\d', password):
                print("- Password should include at least one digit.")
                
            if not re.search(r'[_!@#$%^&*(),.?":{}|<>]', password):
                print("- Password should include at least one special character.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
