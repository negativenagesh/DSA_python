class Solution(object):
    def singleNumber(self, nums):
        result=0
        
        for num in nums:
            result ^=num
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        
# Result---->

# Your input:
# [2,2,1]

# Output:
# 1

# Expected:
# 1
