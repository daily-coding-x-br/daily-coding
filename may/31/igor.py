def encode(s):
    cnt = 1
    ret = ""
    for i in range(1, len(s)):
        if (s[i] == s[i-1]):
            cnt = cnt+1;
        else:
            ret += str(cnt) + s[i-1]
            cnt = 1
    ret += str(cnt) + s[-1]
    return ret


def decode(s):
    ret = ""
    for i in range(0, len(s), 2):
        ret += int(s[i]) * s[i+1]
    return ret


if __name__ == "__main__":
    s = input()
    enc = encode(s)
    print(enc)
    print(decode(enc))

