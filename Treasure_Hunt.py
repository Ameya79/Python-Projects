#TREASURE PROJECT - MULTIPLE IF , ELIF , ESCAPE SEQUENCE ,UPPER CASE AND LOWERCASE

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
next = input('Go \"left" or \"right"? l for left r for right: ') #used escape sequence by using \ key
output = next.lower()
if output == "l":
    next1 = input("swim or wait? ")
    next1lower = next1.lower()
    if next1lower == "wait":
        next2 = input("Which door red yellow or blue? ")
        next2lower = next2.lower()
        if next2lower == "red":
            print("You got burnt in flames, Game Over.")
        elif next2lower =="yellow":
            print("You Win!!!")
        elif next2lower =="blue":
            print("You drowned, Game Over.")
        else:
            "Wrong Choice, Game Over."
    else:
        print("Attacked by sharks! Game Over.")
else:
    print("Fell into a pit, Game Over.")