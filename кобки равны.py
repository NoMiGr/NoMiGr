




def is_correct_bracket(text):
    stack = []
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print(is_correct_bracket('())'))