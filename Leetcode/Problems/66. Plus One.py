# https://leetcode.com/problems/plus-one/

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

digits = [9,9,2,1]
# result = []
# str_digit = ''
# for num in digits:
#     str_digit += str(num)
#
# new_digit = str(int(str_digit)+1)
#
# for letter in new_digit:
#     result.append(int(letter))
#
# print(result)


rem = 1
for i in range(len(digits)-1, -1, -1):
    total = digits[i] + rem

    res = total % 10
    rem = total // 10

    digits[i] = res

    if rem > 0:
        digits = [rem] + digits




print(digits)
