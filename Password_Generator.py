import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
