'''
Functionality
. Program asks the user to type
the first number.
· Program asks the user to type
a mathematical operator (a
choice of "
. Program asks the user to type
the second number.
· Program works out the result
based on the chosen
mathematical operator.
. Program asks if the user wants to continue working with the previous result.
If yes, program loops to use the previous result as the first number and then repeats the calculation process.
If no, program asks the user for the fist number again and wipes all memory of previous calculations.
Add the logo from art.py
'''

# TODO - dmake a function similarly of subtract , div and mult
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

# TODO - now add these into a dictionary as values whith keys as +,-,/,*   
# what i learnt
dic = {
    '+':add,
    '-':subtract,
    '/':divide,
    '*':multiply
}
# TODO - now do 4*2 only using dic functions 
print(dic['*'](4,2)) # dic['*'](4,2) --> multiply(4,2)
def calculator():
    over = False
    input1 = int(input("Enter 1st number: "))
    while not over:
        for i in dic:
            print(i)
        operator = str(input("Enter operator: "))
        input2 = int(input("Enter 2nd number: "))
        answer = (dic[operator](input1,input2))
        print(f'{input1} {operator} {input2} = {answer}')  #made a mistake here that i kept putting previous we dont need previous here
        yn = input("Continue ? Enter y for yes n for no: ")

        if yn == 'y':
            input1 = answer

        else:
            print('Bye.')
            over = True


calculator()







