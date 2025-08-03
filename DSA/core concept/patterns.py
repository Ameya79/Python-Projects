"""
***
***
***
***
"""
for i in range(4):
    for j in range(4):
        print("*",end="")
    print("\n")

'''
* 
* *
* * *
'''
for i in range(3):
    for j in range(i+1):
        print("*",end="")
    print("\n")