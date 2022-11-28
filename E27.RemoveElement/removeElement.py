from typing import List

# 思路：双指针，一个指向存放的地方A，一个指向要检验的地方B。不需要去除的则存放到A,然后A+1，检验下一个地方，否则直接检验下一个地方。
# （实际上可以认为是做了个左移，但val没有循环到右侧）
# Accept, 41%, 63%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertPlace = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insertPlace] = nums[i]
                insertPlace += 1
        print(nums)
        return insertPlace


print(Solution.removeElement(self=Solution, nums=[0, 1, 2, 2, 3, 0, 4, 2], val=0))
