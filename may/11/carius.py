def non_adj_sum(v):
    a = b = 0
    for x in v:
        a, b = b, max(b,a,a+x)
    return b

x = [2,4,6,2,5]
y = [5,1,1,5]
z = [1,-2,3,-3,-4,4,-5,-5]

print(non_adj_sum(x), non_adj_sum(y), non_adj_sum(z))