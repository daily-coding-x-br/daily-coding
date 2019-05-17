# https://en.wikipedia.org/wiki/Reservoir_sampling

import random
import time


# sample stream that of the n first pairs
def n_first_pairs(n):
    for i in range(1, n+1):
        yield i*2


def resevoir_sample(k, stream):
    R = []

    try:
        for _ in range(k):
            R.append(next(stream))
        
        i = k + 1
        while True:
            item = next(stream)

            j = random.randint(1, i)
            if j <= k:
                R[j-1] = item
            
            i += 1
    
    except StopIteration:
        pass

    return R
    

if __name__ == "__main__":
    random.seed(time.time())

    n = int(input())

    print(resevoir_sample(1, n_first_pairs(n)))
