# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


# 96.97%， 83.8%
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        totalNum = len(nums)
        midPlace = totalNum // 2
        if not totalNum:  # 剩下的长度为0时，可以直接返回空了
            return None

        return TreeNode(       # 递归在这里应用，返回中间的数，并对两边再次调用该函数
            nums[midPlace],
            self.sortedArrayToBST(self=self, nums=nums[:midPlace]),
            self.sortedArrayToBST(self=self, nums=nums[midPlace+1:])
        )

print(Solution.sortedArrayToBST(self=Solution,nums=[-10,-3,0,5,9]))