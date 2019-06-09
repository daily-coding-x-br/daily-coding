def make_palindrime(string):
    n = len(string)
    dp = [['' for l in range(n + 1)] for i in range(n)]

    # Initialize table
    for i in range(n):
        dp[i][1] = string[i]

    # Fill the table
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            first, last = string[i], string[i + l - 1]

            if first == last:
                dp[i][l] = first + dp[i + 1][l - 2] + last
            else:
                first_out = first + dp[i + 1][l - 1] + first
                last_out = last + dp[i][l - 1] + last

                if len(first_out) < len(last_out):
                    dp[i][l] = first_out
                elif len(last_out) > len(first_out):
                    dp[i][l] = last_out
                else:
                    dp[i][l] = min(first_out, last_out)

    return dp[0][n]


if __name__ == "__main__":
    string = input()

    print(make_palindrime(string))


