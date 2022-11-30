from typing import List


# 生成指定长度的list  []*length
# []+[], 返回的是一个【】
# 【】，【】返回的是tuple
#  【【】，【】】 返回的是list

# 71.56%， 19.8%
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows == 1:
#             triangle = [[1]]
#         elif numRows == 2:
#             triangle = [[1], [1, 1]]
#         else:
#             triangle = [[1], [1, 1]]
#             for i in range(3, numRows + 1):
#                 newlist = [1]
#                 for j in range(len(triangle[-1]) - 1):
#                     newlist.append(triangle[-1][j] + triangle[-1][j + 1])
#                 newlist.append(1)
#                 triangle.append(newlist)
#         return triangle


# 25.91%, 19.8%
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for rowNumber in range(numRows):  # rowNumber is index of row
            # general generate rule, first and last is 1
            row = [None] * (rowNumber + 1)
            # row = [None for _ in range(rowNumber + 1)]
            row[0], row[-1] = 1, 1
            # specific rule
            for place in range(1, len(row) - 1):  # triangle 一开始是空，用-1会报错. 另一个好处是数组不容易越界（通过row）。
                row[place] = triangle[-1][place - 1] + triangle[-1][place]
            triangle.append(row)
        return triangle


# 以上是迭代的方法（没有明显的定义迭代函数，但是实际在重复迭代）


print(Solution.generate(self=Solution, numRows=5))
