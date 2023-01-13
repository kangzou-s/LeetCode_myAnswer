# # 67.57%, 68.93%

# 利用栈的结构，先进后出
# 遍历结束，左边为0为true； 过程中右边和最近的左不对应，左边个数为0都不行
class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        ref = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                left.append(c)
            else:
                if len(left) == 0:
                    return False
                elif ref[left[-1]] == c:
                    left.pop()
                else:
                    return False
        if len(left) == 0:
            return True


print(Solution.isValid(self=Solution, s='()'))
print(Solution.isValid(self=Solution, s="()[]{}"))
print(Solution.isValid(self=Solution, s="(]"))
