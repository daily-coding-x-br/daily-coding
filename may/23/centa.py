# Just re-write of the official solution
# O(n log n) time and O(n) space

def max_overlap(intervals):
    starts = sorted(start for start, end in intervals)
    ends =  sorted(end for start, end in intervals)

    max_overlap = 0
    curr_overlap = 0

    i, j = 0, 0
    while i < len(intervals):
        if starts[i] < ends[j]:
            i += 1
            curr_overlap += 1
            max_overlap = max(max_overlap, curr_overlap)
        else:
            j += 1
            curr_overlap -= 1

    return max_overlap