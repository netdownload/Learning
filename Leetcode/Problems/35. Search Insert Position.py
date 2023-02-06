# https://leetcode.com/problems/search-insert-position/

nums = [1, 3, 5, 6]
target = 6


class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if target > nums[mid]:
                left = mid+1
            if target < nums[mid]:
                right = mid-1
            if target == nums[mid]:
                return mid
        return left

a = Solution()
print(a.searchInsert(nums, target))