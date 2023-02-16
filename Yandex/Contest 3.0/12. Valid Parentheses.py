def isValid(s):
    if len(s) == 1:
        return 'no'
    if len(s) == 0:
        return 'yes'

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
                    return 'no'
            except:
                return 'no'
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'

s = input()
print(isValid(s))
