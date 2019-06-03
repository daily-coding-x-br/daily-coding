# DP with two dimensions. Let n be the length of the original string
# and m be the length of the final string. The time complexity is
# O(m*n) and the space complexity is O(n) 

def edit_distance(a, b):
    na = len(a)
    nb = len(b)
    
    if nb > na:
        a, b = b, a
        na, nb = nb, na

    prev = [j for j in range(nb+1)] # insert j
    
    for i in range(1, na+1):
        best = [i] # delete i
        
        for j in range(1, nb+1):
            dist = min(best[-1] + 1, prev[j] + 1)
            
            if a[i-1] == b[j-1]:
                dist = min(dist, prev[j-1])
            else:
                dist = min(dist, prev[j-1] + 1)
            
            best.append(dist)

        prev = best


    return best[-1]


if __name__ == "__main__":
    a, b = input(), input()

    print(edit_distance(a, b))