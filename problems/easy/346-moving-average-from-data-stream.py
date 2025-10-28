from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque() 
        self.currentSum = 0
        self.size = size
        
    def next(self, val: int) -> float:        
        if len(self.queue) >= self.size:
            self.currentSum -= self.queue.popleft()
            
        self.queue.append(val)
        self.currentSum += val

        return self.currentSum / len(self.queue)