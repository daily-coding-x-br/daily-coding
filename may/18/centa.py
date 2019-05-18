# O(1) runtime record and lookup with a circular array

class OrderLog:
    def __init__(self, N):
        self.log = [0]*N
        self.N = N

        self.first = 0
        self.num_logs = 0

    def _circulate_index(self, idx, offset):
        if idx + offset >= 0:
            return (idx + offset) % self.N
        else:
            return (idx + offset) + self.N

    def record(self, order_id):
        # Append a record to the start
        self.first = self._circulate_index(self.first, -1)
        self.log[self.first] = order_id

        if self.num_logs < self.N:
            self.num_logs += 1

    
    def get_last(self, i):
        # i is assumed to be 0-based i.e. get_last(0) gets the last element
        # that was added to the log
        print(self.log)
        if i + 1 > self.num_logs:
            raise ValueError

        return self.log[self._circulate_index(self.first, i)]


if __name__ == "__main__":
    ol = OrderLog(10)

    for i in range(15):
        ol.record(i)
        
        print(ol.get_last(0))

    print(ol.get_last(2))
