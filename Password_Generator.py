import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass1 = []
for n1 in range(0 , nr_letters): #1 as it rejects the very last element
    pass1.append(random.choice(letters))


for n1 in range(0 , nr_symbols): #1 as it rejects the very last element
    pass1.append(random.choice(symbols))

for n1 in range(0 , nr_numbers): #1 as it rejects the very last element
    pass1.append(random.choice(numbers))

#pass1 has all character as a str in order so shuffle it to do that first covert it in a list
random.shuffle(pass1)


pass_list = ""
for n1 in range(0,len(pass1)):
    pass_list = pass1[n1] + pass_list

print(pass_list)

              
