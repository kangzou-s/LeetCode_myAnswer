from typing import List


#  当目标元素 target 不存在数组 nums 中时，搜索左侧边界的二分搜索的返回值可以做以下几种解读：
# 1、返回的这个值是 nums 中大于等于 target 的最小元素索引。
# 2、返回的这个值是 target 应该插入在 nums 中的索引位置。
# 3、返回的这个值是 nums 中小于 target 的元素个数。

# 这里采用第二种思路。 所以移动left时， 应该让left更上前一步


# 32.45%， 82.47%
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left = 0  # 左指针
#         right = len(nums)  # 右指针
#         while left < right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 right = mid
#             elif nums[mid] < target:
#                 left = mid + 1
#         return left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0  # 左指针
        right = len(nums) -1  # 右指针
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid + 1
        return left


print(Solution.searchInsert(self=Solution, nums=[1, 3], target=0))
