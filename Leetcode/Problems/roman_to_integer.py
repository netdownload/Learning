# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value I             1 V             5 X             10 L             50 C             100 D
# 500 M             1000 For example, 2 is written as II in Roman numeral, just two one's added together. 12 is
# written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# def roman_to_int(s):
#     to_int = 0;
#     for i in range(len(s)):
#         if s[i] == "M":
#             if i > 0:
#                 if s[i - 1] == "C":
#                     to_int = to_int + 800
#                 else:
#                     to_int = to_int + 1000
#             else:
#                 to_int = to_int + 1000
#         if s[i] == "D":
#             if i > 0:
#                 if s[i - 1] == "C":
#                     to_int = to_int + 300
#                 else:
#                     to_int = to_int + 500
#             else:
#                 to_int = to_int + 500
#         if s[i] == "C":
#             if i > 0:
#                 if s[i - 1] == "X":
#                     to_int = to_int + 80
#                 else:
#                     to_int = to_int + 100
#             else:
#                 to_int = to_int + 100
#         if s[i] == "L":
#             if i > 0:
#                 if s[i - 1] == "X":
#                     to_int = to_int + 30
#                 else:
#                     to_int = to_int + 50
#             else:
#                 to_int = to_int + 50
#         if s[i] == "X":
#             if i > 0:
#                 if s[i-1] == "I":
#                     to_int = to_int + 8
#                 else:
#                     to_int = to_int + 10
#             else:
#                 to_int = to_int + 10
#         if s[i] == "V":
#             if i > 0:
#                 if s[i - 1] == "I":
#                     to_int = to_int + 3
#                 else:
#                     to_int = to_int + 5
#             else:
#                 to_int = to_int + 5
#         if s[i] == "I":
#             to_int = to_int + 1
#     return to_int
#
# print(roman_to_int("MCMXCIV"))

class Solution:
# @param {string} s
# @return {integer}
    def roman_to_int(self, s):
        roman = {'M': 1000,'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]