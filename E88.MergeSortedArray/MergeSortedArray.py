from typing import List


# 68.77%, 6.41%
# 直接复制，会导致覆盖元素，产生错误。从后往前，覆盖的元素一定是已经用过的元素
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        flag1 = m - 1  # 指针1， 指向nums1的查找位
        flag2 = n - 1  # 指针2， 指向nums2的查找位
        flag3 = m + n - 1  # 指针3， 指向nums1的插入位
        while flag1 >= 0 and flag2 >= 0:
            if nums1[flag1] >= nums2[flag2]:
                nums1[flag3] = nums1[flag1]
                flag3 -= 1
                flag1 -= 1
            else:
                nums1[flag3] = nums2[flag2]
                flag3 -= 1
                flag2 -= 1
        # 本质是把nums2 往nums1中插入，所以只需要考虑nums2是否全插入了
        # 当flag>=0时，都说明没插入完全
        while flag2 >= 0:
            nums1[flag3] = nums2[flag2]
            flag3 -= 1
            flag2 -= 1


print(Solution.merge(self=Solution, nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
