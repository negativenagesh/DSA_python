# Question:

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# Answer---->

class Solution(object):
    def majorityElement(self, nums):
        count=0
        candidate=None
        
        for num in nums:
            if count==0:
                candidate=num
            count+=(1 if num==candidate else -1)
        return candidate
        """
        :type nums: List[int]
        :rtype: int
        """
        
# Result ---->

# Your input:
# [3,2,3]

# Output:
# 3

# Expected:
# 3
