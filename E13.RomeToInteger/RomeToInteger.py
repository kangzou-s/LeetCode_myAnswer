## answer1
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         substitution = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }
#         s = s.replace('CM', 'DCD').replace("CD", "CCCC").replace("XC", "LXL").replace("XL", "XXXX").replace("IX",
#                                                                                                             "VIV").replace(
#             "IV", "IIII")
#         number = list(s)
#         for i in range(len(number)):
#             number[i] = substitution[number[i]]
#         number = sum(number)
#         return number


# # answer2
class Solution:
    def romanToInt(self, s: str) -> int:
        substitution = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        s = s.replace('CM', 'DCD').replace("CD", "CCCC").replace("XC", "LXL").replace("XL", "XXXX").replace("IX",
                                                                                                            "VIV").replace(
            "IV", "IIII")
        number = sum(list(map(lambda x: substitution[x], s)))
        return number


print(Solution.romanToInt(self=Solution, s='LVIII'))
