def balance_check(s):
    # Edge case to check even or odd number of brackets. if its odd return False.
    # if len(s) % 2 != 0:
    #     return False
    #
    # openB = set('([{')  # OP: {'(', '[', '{'}
    # matchingB = set([('(', ')'), ('[', ']'), ('{', '}')])  # creating matching tuples of the paranthesis.
    #
    # stack_list = []
    #
    # for par in s:
    #     if par in openB:
    #         stack_list.append(par)
    #     else:
    #         if len(stack_list) == 0:
    #             return False
    #         last_open = stack_list.pop()
    #
    #         if (last_open, par) not in matchingB:
    #             return False
    # return len(stack_list) == 0
    stack = []
    list = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
        list.append(char)
    return stack == []


print(balance_check("()(){]]}"))
