# https://leetcode.com/problems/add-to-array-form-of-integer/

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
#
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455

num = [1, 4, 5, 0]
k = 34

class Solution(object):
    def addToArrayForm(num, k):
        arr = []
        # n = map(str, num)
        # n = ''.join(n)
        # n = int(n)
        n = int(''.join((map(str, num))))
        for letter in str(n + k):
            arr.append(int(letter))
        return arr
    

s = Solution
print(s.addToArrayForm(num, k))