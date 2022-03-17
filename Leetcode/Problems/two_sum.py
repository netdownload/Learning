# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

NUMS = [2, 7, 11, 15]
TARGET = 9


# Brute Force
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if (nums[i] + nums[j]) == target:
#                 return [i, j]
#
#
# print(two_sum(NUMS, TARGET))

#Hashmao 2 ways
# def two_sum(nums, target):
#     hashmap = {}
#     for i in range(len(nums)):
#         hashmap[nums[i]] = i
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap and hashmap[complement] != i:
#             return [i, hashmap[complement]]
#
# print(two_sum(NUMS, TARGET))

#Hashmap  1 way
def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


print(two_sum(NUMS, TARGET))