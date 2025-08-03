'''a = set([1,2,3,3,4,5,6])
🧮 Problem: Minimum Steps to Zero
Given an integer n, return the minimum number of steps to reduce it to 0.

In each step, you can:
Subtract any one digit (non-zero) from the current number.
You need to repeat this until the number becomes 0.
✏️ Example 1:
Input:
n = 27
Output:
5
Explanation:
One of the best ways to reduce 27 to 0:
27 → 20 (subtract 7)
20 → 18 (subtract 2)
18 → 10 (subtract 8)
10 → 9 (subtract 1)
9 → 0 (subtract 9)

🔒 Constraints:
1 <= n <= 10^6

'''

for i in a:
