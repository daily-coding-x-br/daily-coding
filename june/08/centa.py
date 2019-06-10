def power_set(s):
    if not s:
        return [[]]

    reduced = power_set(s[1:])
    return reduced + [sub + [s[0]] for sub in reduced]


if __name__ == "__main__":
    s = input().split()

    print(power_set(s))