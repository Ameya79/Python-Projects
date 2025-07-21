'''Love Calculator
💪 This is a difficult challenge! 💪 

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

2. Then check for the number of times the letters in the word LOVE occurs.   

3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 

R occurs 1 time 

U occurs 2 times 

E occurs 2 times 

Total = 5 

L occurs 1 time 

O occurs 0 times 

V occurs 0 times 

E occurs 2 times 

Total = 3 

Love Score = 53

Example Input 

calculate_love_score("Kanye West", "Kim Kardashian")

Example Output

42

How to test your code and see your output?

Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:

def calculate_love_score(name1, name2):
  # your code here
 
# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")'''

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")

import random

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    t = combined_names.count('t')
    r = combined_names.count('r')
    u = combined_names.count('u')
    e = combined_names.count('e')
    first_digit = t + r + u + e

    l = combined_names.count('l')
    o = combined_names.count('o')
    v = combined_names.count('v')
    e = combined_names.count('e')  # counts again, fine here
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))

    # Message pools
    good_messages = [
        "You're like peanut butter and jelly 🥜🍇",
        "Perfect match made in code ❤️",
        "Cupid's proud of this one 😍",
    ]

    ok_messages = [
        "You're doing okay! Maybe go for a coffee ☕",
        "Could work out with some effort 💪",
        "Not bad, not bad at all 😌",
    ]

    bad_messages = [
        "Like oil and water... 😬",
        "Danger zone! 💣",
        "You may want to run 🏃‍♂️💨",
    ]

    # Pick message based on score range
    if score > 80:
        message = random.choice(good_messages)
    elif 40 <= score <= 80:
        message = random.choice(ok_messages)
    else:
        message = random.choice(bad_messages)

    return f"Your love score is {score}. {message}"


print(calculate_love_score(name1, name2))
