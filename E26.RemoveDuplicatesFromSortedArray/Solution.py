# non-decreasing order 指的是增长顺序，但是允许有相同元素
from typing import List


#  Accept, Beats 38.45%, 20.6%
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         K = len(nums)
#         for i in range(len(nums)):
#             if nums[i] != '_':
#                 for j in range(i + 1, len(nums)):
#                     if nums[j] == nums[i]:
#                         nums[j] = '_'
#                         K -= 1
#                     elif nums[j] > nums[i]:
#                         break
#         i = 0
#         while (nums[i] != '_') and (i < len(nums) - 1):
#             i += 1
#         for j in range(i, len(nums)):
#             if nums[j] != '_':
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#                 j += 1
#         print(nums)
#         return K

# Accept 82.99%, 66.47
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertPlace = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[insertPlace] = nums[j]
                insertPlace += 1
        return insertPlace


print(Solution.removeDuplicates(self=Solution, nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
