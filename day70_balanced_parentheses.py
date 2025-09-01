def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expression:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


expr = input("Enter an expression with parentheses: ")
print("Balanced" if is_balanced(expr) else "Not Balanced")
