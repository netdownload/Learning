# https://leetcode.com/problems/merge-sorted-array/
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# nums1 = [1, 2, 3, 0, 0, 0]
m = 3
# nums2 = [2, 5, 6]
n = 3
nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        lp = 0
        rp = 0
        while lp < m and rp < n:
            if nums1[lp] > nums2[rp]:
                nums1[lp], nums2[rp] = nums2[rp], nums1[lp]
                lp += 1
            elif nums1[lp] < nums2[rp]:
                rp += 1
            elif nums1[lp] == nums2[rp]:
                lp += 1
                nums1[lp], nums2[rp] = nums2[rp], nums1[lp]
        for i in range(rp, n, 1):
            nums1[lp+i] = nums2[i]
        return nums1

s = Solution()
print(s.merge(nums1, m, nums2, n))