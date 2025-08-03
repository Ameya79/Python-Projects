#static array 
a= [1,2,3,4,5,]
#0 1 2 3 4
a[2] # ans 3 complexity o(1) accessing any element
#they are mutable 
#if we do a[2] = 3 it changes and this operation is also const o(1)

#in:
if 5 in a:
    print('True')
# here the array is manually scanned from index 0 to 4 so this is an o(n)
# this is worst
#insterting, deleting all are o(n)

# Demonstrating list append time complexity
#Dynamic arrays
'''in python dynamic arrays increase their size as it fills up this the size is mostly increased by power of 2 '''
# Append adds to the end (*O(1) average) most of the time it o(1)
lst1 = []
for i in range(5):
    lst1.append(i)
print("After append:", lst1)

# Insert at the beginning or middle (O(n))
lst2 = []
for i in range(5):
    lst2.insert(0, i)
print("After insert at beginning:", lst2)

#other stuff : 
'''
popping is o(1)
deletion not from the end is o(n)
random access is o(1)
checking if and element exisits is o(n)
'''

