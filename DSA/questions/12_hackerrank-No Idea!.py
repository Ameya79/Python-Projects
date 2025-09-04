n,m = map(int,input().split())
n_elements = list(map(int,input().split()))
A_elements = set(map(int,input().split()))
B_elements = set(map(int,input().split()))
score = 0
for i in range(n):
    if n_elements[i] in A_elements:
        score= score+1
    elif n_elements[i] in B_elements:
        score= score-1
    
print(score)

#using set here reduces the searching complexity by a ton as set uses hash taable for search

'''
QUESTION

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing
m integers. You like all the integers in set A and dislike all the integers in set B. Your initial
happiness is 0. For each i integer in the array, if i E A, you add 1 to your happiness. If
i E B, you add -1 to your happiness. Otherwise, your happiness does not change.
Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might

contain duplicate elements.

Constraints

1≤ n ≤ 105
1≤ m < 105

1 ≤ Any integer in the input ≤ 109

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.'''
