# https://leetcode.com/problems/add-binary/

# Input: a = "11", b = "1"
# Output: "100"
#
# Input: a = "1010", b = "1011"
# Output: "10101"

a = '1010'
b = '1011'


class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        ans = ''
        i = 0

        a = a[::-1]
        b = b[::-1]

        while i < len(a) or i < len(b) or carry !=0:
            x = 0
            if i < len(a) and a[i] == '1':
                x = 1
            y = 0
            if i < len(b) and b[i] == '1':
                y = 1
            ans = str((x+y+carry)%2) + ans
            carry = (x+y+carry)//2
            i += 1
        return ans


c = Solution()
c.addBinary(a, b)