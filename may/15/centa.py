# Sliding window technique
# O(n) runtime with hash tables
# O(k) space complexity

from collections import defaultdict


def longest_k_distinct_substring(k, string):
    char_count = defaultdict(int)

    max_len = 0
    max_start = max_end = 0

    start = 0
    for end in range(len(string)):
        char_count[string[end]] += 1

        n_distinct = len(char_count.keys())
        
        if (n_distinct <= k and
            (end-start+1) > max_len):

            max_len = end-start+1
            max_start = start
            max_end = end

        elif n_distinct > k: 
            if char_count[string[start]] > 1:
                char_count[string[start]] -= 1
            else:
                del char_count[string[start]]

            start += 1

    return string[max_start: max_end+1]


if __name__ == "__main__":
    k = int(input())
    string = input()

    print(longest_k_distinct_substring(k, string))
