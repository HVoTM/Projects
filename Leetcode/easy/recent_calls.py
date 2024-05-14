class RecentCounter:

    def __init__(self):
        self.time = [0, 0] # TODO: costs more memory space, just use t-3000 to check the queue instead, which should suffice
        self.requests = [] # queue implementation

    def ping(self, t: int) -> int:
        print('Current ping: ',t)
        self.requests.append(t)
        # set the new time range
        self.time[0] = t - 3000
        self.time[1] = t

        out = 0 # no need for counter
        for request in self.requests: # use while to combine with the below loop for concurrent checking
            # print(request) # tester
            if request < self.time[0]:
                out += 1
        for i in range(out): # TODO: unnecessary, just simultaneously checking and popping at index 0 should do 
            self.requests.pop(0)

        # test code
        # print('Current time range:',self.time)
        # print(self.requests)
        return len(self.requests)
    
# Another solution
from collections import deque

class RecentCounter1:
    def __init__(self):
        self.requests = deque() # uses double-ended queue for faster runtime
    
    def ping(self, t: int) -> int:
        # simultaenously checking if older requests are out of the time range [t-3000, t]
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # then add the new one afterwards
        self.requests.append(t)
        return len(self.requests)
    
if __name__ == '__main__':
    obj = RecentCounter()

    callers = [642, 1849, 4921, 5936, 5957]
    for call in callers:
        print(obj.ping(call))
        print('____________________\n')