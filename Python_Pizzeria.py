#PIZZA PROJECT AND LOGICAL OPERATORS
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
new_size = size.capitalize()
new_pep = pepperoni.capitalize()
new_cheese = extra_cheese.capitalize()
if new_size == "S":
    bill= 15
elif new_size == "M":
    bill= 20
else :
    bill = 25  #use if elif else in situations where there is 1 outcome after the action
    #use if multiple times when there is a whole new unrelated question independent from previous causes
if new_pep == "Y":
    if new_size == "S":
        bill += 2
    else:
        bill += 3
if new_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


'''WHAT IF WE HAVE TO CHECK FOR MULTIPLE CONDITIONS AT THE SAME TIME?'''
# they are and or not
#and: all are needed to be true
#or: any 1 should be true
#not: in the out put false becomes true and true becomes false (Output becomes opposite)