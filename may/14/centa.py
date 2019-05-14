# Use DP, again.
# Time: O(n*|X|)
# Space: O(n)

def num_segment_divisions(N, X):
    dp = [0] * (N + 1)

    for i in range(1, N+1):
        for x in X:
            if i == x:
                dp[i] += 1
            dp[i] += dp[max(i-x, 0)]

    return dp[N]


if __name__ == "__main__":
    N = int(input())
    X = list(map(int, input().split()))

    print(num_segment_divisions(N, X))
