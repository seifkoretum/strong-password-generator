#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password? \n"))
num_symbols = int(input(f"How many symbols would you like? \n"))
num_numbers = int(input(f"How many numbers would you like? \n"))

pass_not_shuffled= ""
pass_shuffled = []
final_pass=""
for letter in range(0,num_letters):
    pass_not_shuffled += random.choice(letters)
for number in range(0,num_numbers):
    pass_not_shuffled += random.choice(numbers)
for symbol in range(0,num_symbols):
    pass_not_shuffled += random.choice(symbols)
# print(pass_not_shuffled)

for password in range(0,len(pass_not_shuffled)):
      pass_shuffled.append(pass_not_shuffled[password])
random.shuffle(pass_shuffled)

for elements in range(0,len(pass_shuffled)):
    final_pass += pass_shuffled[elements]

print(f'Your password is: {final_pass}')