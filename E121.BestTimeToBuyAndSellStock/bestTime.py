import sys
from typing import List
import numpy as np


# 简单的遍历，算法复杂度为o（n^2）, 时间过不了
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProfits = 0
#         for buydate in range(len(prices)):
#             if prices[buydate] > prices[buydate -1]:
#                 break
#             for selldate in range(buydate, len(prices)):
#                 profit = prices[selldate] - prices[buydate]
#                 if profit > maxProfits:
#                     maxProfits = profit
#         return maxProfits


# 单遍历，算法复杂度为O(n),
# 从结果上来看，buy是其前面的最小值，sell是（buy）后面的最大值
# 拆解为两部分，buy的价格动态计算，当找到更低值的时候，他后面的利润计算是基于这个值的，但不一定保留，因为可能利润不一定最大了
#  利润有更大时，保留更大利润
# 有一个默认的条件，卖的日期必须在买的日期之后。扫描是，首先会将low置于第一个位置。然后扫描的x一直在low的前面，故一定满足该条件。


# 80.4%, 39.49%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         low, high = sys.maxsize, 0  # 一开始，low应该无穷大
#         profit = 0
#         for x in prices:
#             if x - low > profit:
#                 profit = x - low
#             if x < low:
#                 low = x
#         return profit


# 使用状态机的方法
# 本质上是列了个表格，每一步的上一步有两种情况，这一步取的是这两种情况中的大的那个，以后的更大利润都是基于现在的最大利润的基础上
# 5.1%, 7.4%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = np.empty((n, 2))      # dp的长度与price的长度一致，因为在每一个日期都有一个操作需要存储。
        for i in range(n):
            if i - 1 == -1:  # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return int(dp[n - 1][0])


print(Solution.maxProfit(self=Solution, prices=[7, 1, 5, 3, 6, 4]))
