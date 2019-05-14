# Aloysio


def solve(k, ns, m):
    if k < 0:
        return 0
    if k == 0:
        return 1
    if m[k] >= 0:
        return m[k]
    sol = 0
    for n in ns:
        sol+= solve(k-n, ns, m)
    m[k] = sol

    return sol


if __name__ == "__main__":
    n = 2
    ns = [1, 2]
    m = [-1 for i in range(n+1)]

    print(solve(n, ns, m))
