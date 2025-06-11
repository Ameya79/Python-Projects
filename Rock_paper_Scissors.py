import random
import sys
#ROCK PAPER SCISSORS 
'''
Plan:
0 = rock
1 = paper
2 = scissors
#the computer should pull out random choice 
#can make use of random.randint
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_of_choices = [rock,paper,scissors]
#our logic
user_input = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors: \n"))
if user_input>= 0 and user_input<=2:
    print("Your Choice:",list_of_choices[user_input])
else:
    print("Wrong input")
    sys.exit()
 


#computer logic

comp_choice = random.randint(0,2)
     
if user_input>= 0 and user_input<=2:
    print("Computers Choice:",list_of_choices[comp_choice])
else:
    print("Wrong input")
if user_input == 0 and comp_choice == 2:
    print("You won")
elif user_input == 2 and comp_choice == 0:
    print("You lost")
elif user_input>comp_choice:
    print("You won")
elif comp_choice>user_input:
    print("You lost")
elif comp_choice == user_input:
    print("Draw")
else:
    print("Print Enter Valid Input")
 
