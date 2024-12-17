import string 
import random

# Store characters in lists
s1 = list(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
s2 = list(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ   
s3 = list(string.digits)           # 0123456789
s4 = list(string.punctuation)      # !@#$%^&*()_+

# Take the number of characters from the user
characters_number = input("How many characters for the password? ")

# Validate input to ensure it's a number and at least 6 characters
while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print("You need at least 6 characters.")
            characters_number = input("Please enter the number again: ")
        else:
            break
    except ValueError:
        print("Please enter numbers only.")
        characters_number = input("How many characters for your password? ")

# Shuffle the character lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Generate password with a mix of character types
password = []

# Ensure the password contains at least one character from each category
password.append(random.choice(s1))
password.append(random.choice(s2))
password.append(random.choice(s3))
password.append(random.choice(s4))

# Fill the rest of the password with random characters from all categories
remaining_length = characters_number - 4  # subtract the 4 we already added
all_characters = s1 + s2 + s3 + s4
random.shuffle(all_characters)
password.extend(random.choices(all_characters, k=remaining_length))

# Shuffle the final password list and convert it to a string
random.shuffle(password)
final_password = "".join(password)

# Output the password
print(final_password)
