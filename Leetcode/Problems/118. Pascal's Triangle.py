# https://leetcode.com/problems/pascals-triangle/
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

numRows = 6


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]*i for i in range(1, numRows+1)]

        for i in range(2, numRows, 1):
            dp = [1]*(i+1)
            for j in range(i-1):
                dp[j+1] = ans[i - 1][j] + ans[i - 1][j + 1]
            ans[i] = dp
        return ans


s = Solution()
print(s.generate(numRows))
