import random
import string

def generate_password(length):
    #Generate a random password of the given length.
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    #Generate secure passwords based on user input.
    print("Welcome to the Password Generator!")
    length = int(input("Please enter the desired length of your password: "))
    num_passwords = int(input("Please enter the number of passwords to generate: "))

    for _ in range(num_passwords):
        password = generate_password(length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
