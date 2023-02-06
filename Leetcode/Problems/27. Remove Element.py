# https://leetcode.com/problems/remove-element/
nums = [0,1,2,2,3,0,4,2]
val = 2
# nums = [3,2,2,3]
# val = 3

# class Solution(object):
#     def removeElement(self, nums, val):
#         k = 0
#         i = 0
#         while i < len(nums):
#             if val == nums[i]:
#                 nums.pop(i)
#             else:
#                 i += 1
#                 k += 1
#         return k

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if val == nums[i]:
               i += 1
            else:
                nums[k] = nums[i]
                k += 1
        return k, nums



a = Solution()
print(a.removeElement(nums, val))