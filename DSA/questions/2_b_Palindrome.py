x = 121

def isPalindrome(x):
    
    new = str(x)  # "121"
    y =list(new)  # ["1","2","1"]
    y.reverse()   # ["1","2","1"]
    reverse = ''.join(y) # "121"
    if new == reverse:  # "121" == # ["1","2","1"]  none return thats why we used join in the dotted part
       return True
    
print(isPalindrome(x))
#Better version
def isPalindrome(x):
    
    new = str(x)  # "121"
    y =list(new)  # ["1","2","1"]
    y.reverse()   # ["1","2","1"]
    reverse = ''.join(y)
    return new == reverse  # "121" == # ["1","2","1"]  none return thats why we used join in the dotted part
    
print(isPalindrome(x))