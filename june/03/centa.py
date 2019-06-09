from math import log

def detect_arbritage(table):
    n = len(table) # number of vertices

    # Calculate the log of each exchange rate
    log_table = [[log(rate) for rate in row] for row in table]

    # Use the Bellman Ford algorithm to find a negative cycle
    # Initialize distances
    distances = [float('inf') for _ in range(n)]

    # Run algorithm from vertex 0
    distances[0] = 0
    for _ in range(n-1):
        for i in range(n):
            for j in range(n):
                if distances[i] + log_table[i][j] < distances[j]:
                    distances[j] = distances[i] + log_table[i][j]

    # Check for negative cycles
    for i in range(n):
        for j in range(n):
            if distances[i] + log_table[i][j] < distances[j]:
                return True

    return False
