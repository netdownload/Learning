class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans = 0
        ans_temp = 0
        for i in range(len(accounts)):
            ans_temp = 0
            for j in range(len(accounts[i])):
                ans_temp += accounts[i][j]
            if ans_temp > ans:
                ans = ans_temp
        return ans