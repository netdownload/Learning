# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Не понятно решение, так как просят написать функцию, а в решении используют готовую

s = ["h", "e", "l", "l", "o"]


class Solution(object):
    def reverseString(self, s):
        s.reverse()
