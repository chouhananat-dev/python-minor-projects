# the following code creates a random password of required length
import random

# creating string containing all the necessary characters
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-_+=\/<>~()[]{!}|:,;@'#$%^&*?."
password=""
length=int(input("Enter the length of password you want to create:\n"))
for i in range(length):
    password+=random.choice(characters)
print("Your required password is:",password)
