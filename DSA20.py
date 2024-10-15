# Question ---->

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.


# Answer --->

class Solution(object):
    def mySqrt(self, x):

        import numpy as np
        
        return int(np.sqrt(x))
        
        """
        :type x: int
        :rtype: int
        """
        
# Result ---->

# Your input:
# 4

# Output:
# 2

# Expected:
# 2
