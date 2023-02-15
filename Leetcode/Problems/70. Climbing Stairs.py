# https://leetcode.com/problems/climbing-stairs/

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# class Solution(object):
#     @cache
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n > 2:
#             return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution(object):
    def climbStairs(self, n):
        memo = {}
        memo[1] = 1
        memo[2] = 2
        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]
        return climb(n)

# def climbStairs(n):
#     memo = {}
#     memo[1] = 1
#     memo[2] = 2
#     def climb(n):
#         if n in memo:
#             return memo[n]
#         else:
#             memo[n] = climb(n-1) + climb(n-2)
#             return memo[n]
#     return climb(n)
#
# print(climbStairs(45))

def climbStairs(n):
    one = 1
    two = 1
    for i in range(n-1):
        ans = one + two
        one = two
        two = ans
    return two

print(climbStairs(3))


