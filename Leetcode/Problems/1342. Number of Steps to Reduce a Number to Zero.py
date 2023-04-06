class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        while num != 0:
            if num % 2 == 0:
                ans += 1
                num = num / 2
            else:
                ans += 1
                num = num - 1
        return ans
