'''
Code
Testcase
Test Result
Test Result
1. Two Sum
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
nums = [2,7,11,15]
target = 9

#aim is to get 9
# answer should be [0,1] => 2+7 = 9
# use for loop twice to send 2 variables i and j (1 ahead of i) for iteration, use if for checking the conditions 


def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]== target:
                return [i,j]
            
print(twosum(nums,target))


def twosums(target,nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]== target:
                return[i,j]
            

print(twosums(target,nums))

