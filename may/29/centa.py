from collections import deque

def is_balanced(string):
    bracket_map = { ")": "(", "]": "[", "}": "{" }
    stack = deque()

    for bracket in string:
        if bracket in bracket_map:
            if not stack or bracket_map[bracket] != stack.pop():
                return False
        else:
            stack.append(bracket)

    if stack:
        return False

    return True

if __name__ == "__main__":
    string = input()

    print(is_balanced(string))


