# https://leetcode.com/problems/sqrtx/
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        low = 1
        high = x
        while low <= high:
            mid = int((low+high)/2)
            if mid*mid == x:
                return mid
            if mid*mid > x:
                high = mid
            if mid*mid < x:
                low = int((low+high)/2)
            if (mid*mid) < x < (mid+1)*(mid+1):
                return mid