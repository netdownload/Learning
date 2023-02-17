# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

nums = [-1,0,3,5,9,12]
target = 9

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
        return -1

s = Solution()
print(s.search(nums, target))