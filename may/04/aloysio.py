# Takes 2*n space and o(nlogn) time
# Uses recursive binary products to obtain the result

ranges = {}

def calc(mat, i, j, k):
    if i == j:
        if i == k:
            return 1
        return mat[i]
    elif k >= i and k <= j:
        return calc(mat, i, i+(j-i)//2, k)*calc(mat, i+(j-i)//2+1, j, k)
    elif (i, j) in ranges:
        return ranges[(i, j)]
    else:
        ranges[(i, j)] = calc(mat, i, i+(j-i)//2, k)*calc(mat, i+(j-i)//2+1, j, k)
        return ranges[(i, j)]

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    resp = []
    for i in range(len(arr)):
        resp+=[calc(arr, 0, len(arr)-1, i)]

    print(resp)
