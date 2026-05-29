inputtt = int(input("Enter the number of passwords to generate: "))
length = int(input("Enter the length of each password: "))

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
for _ in range(inputtt):
    print(generate_password(length))    

    