fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

'''
Sample Input 0

1 = x
1 = y
1 = j
2 = n
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

all pssible combinatons in which
0 <= i <= x
0 <= j <= y
0 <= k <= z
such that i+j+k != n
'''