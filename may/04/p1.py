# O(n) runtime and O(n) space complexity
# author: Centa

def problem_1(k, arr): 
    seen = set() # stores the numbers that
                 # were already seen
    
    for num in arr:
        if (k-num) in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    # read k and then the array of integers
    k = int(input())
    arr = list(map(int, input().split()))
    
    # get the answer of the problem
    ans = problem_1(k, arr) 

    # print the result
    print(ans)
