# https://leetcode.com/problems/shuffle-the-array/description/

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result_list = []
        for _ in range(n):
            result_list.append(nums[_])
            result_list.append(nums[_+n])
        return result_list