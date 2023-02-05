# https://leetcode.com/problems/valid-parentheses/


class Solution(object):
    def isValid(self, s):
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        stack = []
        look = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for letter in s:
            if look.get(letter):
                stack.append(letter)
            else:
                try:
                    last_bracket = stack.pop()
                    bracket_from_look = look.get(last_bracket)
                    if letter != bracket_from_look:
                        return False
                except:
                    return False
        return len(stack) == 0


a = Solution()
print(a.isValid('{}{}'))
