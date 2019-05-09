# Use dynamic programming!
#
# Let n be the length of the string
# and nd(i) the numbers of ways of
# decoding the substring of the i
# i first characters. Then:
#
#         | nd(i-1) + nd(i-2), if str[i-1:i+1] <= 26
# nd(i) = | 
#         | nd(i-1), if not
#
# with nd(0) = 1
#
# This solution gives O(n) runtime and
# O(1) space complexity.

def number_decodings(message):
    prev = 1 # stores the previous number of decodings
             # is initialized to nb(0)
    curr = 1 # stores the current number of decodings

    for i in range(1, len(message)):
        if int(message[i-1:i+1]) <= 26:
            curr, prev = curr + prev, curr
        else:
            prev = curr
    
    return curr


if __name__ == "__main__":
    # get input from stdin
    message = input()

    # get the answer
    ans = number_decodings(message)

    # print the answer
    print(ans)


