
# Solution using backtracking

def regex_match(string, regex):
    ans = True
    si, ri = 0, 0

    while ans and si < len(string) and ri < len(regex):
        if regex[ri] == "*":
            break

        elif regex[ri] == "." or regex[ri] == string[si]:
            ri += 1
            si += 1

        else:
            ans = False
    
    if ri < len(regex)-1 and regex[ri] == "*":
        ans = False
        ri += 1

        while not ans and si < len(string):
            while si < len(string) and regex[ri] != string[si]:
                si += 1
            ans = regex_match(string[si:], regex[ri:])

    elif ri != len(regex) or si != len(string):
        ans = False

    return ans 

if __name__ == "__main__":
    string = input()
    regex = input()

    print(regex_match(string, regex))
