from typing import List


# 这个方法，复杂度是n^2, 能得出正确结果，但是复杂度过高
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return list((i, j))

# 复杂度为O（n）
# 对于nums 中的每个数A，存在一个'互补对'B，把这个互补对(B)的值计入um中，并记录当前值(A)的位置。
class Solution:
    def twoSum(self, nums, target):
        um = dict()
        for i in range(len(nums)):
            # 查找是否存在满足一个数+nums[i]==target,即找到A的值之后
            if nums[i] in um:
                result = [um[nums[i]], i]
                return result
            um[target - nums[i]] = i
        return [0, 0]


print(Solution.twoSum(self=Solution, nums=[2, 7, 7, 7, 11, 15], target=18))
