# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1]

class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        while k < len(nums):
            if nums[k] == nums[k-1]:
                nums.pop(k)
            else:
                k += 1
        return k

a = Solution()
print(a.removeDuplicates(nums))