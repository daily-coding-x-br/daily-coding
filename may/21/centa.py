def cumul_cost(k, pb, ps, pbc, psc):
    if k == pb:
        return  

def minimum_cost_house_coloring(costs):
    N = len(costs)
    K = len(costs[0])
    
    pb = -1 # previous best and previous second best colors
    pbc = psc = 0 # previous best and previous second best cumulative cost


    def cumul(i, k):
        return (costs[i][k] + pbc if k == pb else costs[i][k] + psc)


    for i in range(N):
        # b is the current best and s is the current second best colors
        # bc is the current best and sc is the current second best cumulative cost
        if cumul(i, 0) <= cumul(i, 1):
            b = 0
            bc, sc = cumul(i, 0), cumul(i, 1)
        else:
            b = 1
            bc, sc = cumul(i, 1), cumul(i, 0)

        for k in range(K):
            if cumul(i, k) < bc:
                b = k
                bc, sc = cumul(i, k), bc
            elif cumul(i, k) < sc:
                sc = cumul(i, k)
    
        pb = b
        pbc, psc = bc, sc


    return pbc


if __name__ == "__main__":
    n = int(input())
    
    costs = []
    for _ in range(n):
        line = list(map(int, input().split()))
        costs.append(line)

    print(minimum_cost_house_coloring(costs))