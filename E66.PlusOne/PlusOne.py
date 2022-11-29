from typing import List


# 递归， 但leetcode 识别不了
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         def digitplus(digits: List[int], place: int):
#             if digits[len(digits)-1-place] != 9:
#                 digits[len(digits)-1-place] += 1
#             if digits[len(digits)-1-place] == 9:
#                 digits[len(digits)-1-place] = 0
#                 if place+1 < len(digits):
#                     digitplus(digits, place+1)
#                 else:
#                     digits = [1]+[0]*len(digits)
#             # print(digits)
#             return digits
#         digitplus(digits, 0)

# 先将list颠倒过来，对每位进行计算余数和进位，方便最后一位的进位
# 16.5%, 59.55%
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = list(reversed(digits))
#         carry = 0
#         digits[0] += 1         # 先把最后一位+1，实现carry的统一，便于后续计算
#         for place in range(len(digits)):
#             sum = digits[place] + carry
#             digits[place] = sum % 10
#             carry = sum // 10
#         if carry != 0:
#             digits.append(1)
#         return list(reversed(digits))


# 不颠倒顺序的进行， 最直观的做法
# 79.3%, 59.55%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for place in range(len(digits) - 1, -1, -1):  # 关键在于此处，怎样控制位置！ 倒序遍历的三种方法，：：-1，切片，用-1表示所有
            # range(len-1:-1,-1),  生成序列，所以结尾用-1
            # reversed ， 实际是一个迭代器，object
            sum = digits[place] + carry
            digits[place] = sum % 10
            carry = sum // 10
            if carry == 0:  # 进位为0时，结束计算
                break
        if carry != 0:
            digits = [1] + digits
        return digits


# print(Solution.plusOne(self=Solution, digits=[9]))
a = [1, 2, 3]
# print(a[-1])
# print(a[0:-1])
# print(a[-1:-1])
list(map(lambda x: print(x), range(len(a) - 1, -1, -1)))

# for i in range(len(a) - 1, -1, -1):
#     print(i)
# print(a[len(a) - 1:-1:-1])
