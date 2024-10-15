# Question ---->

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# Answer ---->

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        x_str=str(x)
        
        i,j=0,len(x_str)-1
        
        while i < j:
            if x_str[i]!=x_str[j]:
                return False
            
            i+=1
            j-=1
        
        return True
               
        """
        :type x: int
        :rtype: bool
        """
# Result ---->

# Your input:
# 121

# Output:
# true

# Expected:
# true
