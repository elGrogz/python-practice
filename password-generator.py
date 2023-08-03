import random
import string

print("\n=====Password Generator=====\n")

chars = list(
    string.ascii_letters + string.digits + "!@#$%^&*("
)  # letters A-Z in lower case and upper case

numberOfPasswordsToGenerate = input("Amount of passwords to generate: ")
numberOfPasswordsToGenerate = int(numberOfPasswordsToGenerate)

lengthOfPasswordsToGenerate = input("Length of passwords to generate: ")
lengthOfPasswordsToGenerate = int(lengthOfPasswordsToGenerate)

print("\nHere are your passwords: ")

for password in range(numberOfPasswordsToGenerate):
    passwords = ""
    for character in range(lengthOfPasswordsToGenerate):
        passwords += random.choice(chars)
    print(passwords)
