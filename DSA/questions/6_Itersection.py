'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''



# def intersection(self, nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
    
# nums1 = [1,2,2,1]
# nums2 = [2,2]

# a = set(nums1)
# b = set(nums2)
# print(list(a & b))

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set(nums1)
        b = set(nums2)
        return (list(a & b))




#PREREQUSITES:

# Create a set
s = set([1, 2, 3, 3])   # duplicate 3 is removed
print(s)                # Output: {1, 2, 3}

# Check membership
print(2 in s)           # True
print(5 in s)           # False

# Add to set
s.add(4)

# Intersection with another set
a = set([1, 2, 3])
b = set([2, 3, 4])
print(a & b)            # Output: {2, 3}

# Convert back to list
list(a & b)             # [2, 3]